import os
import re
import json
import unicodedata

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def generate_taxonomy_index(canonical_es_name, lang, localized_name):
    # Hugo lowercases taxonomy folders by default but retains non-ASCII accents
    folder_name = canonical_es_name.lower()
    dir_path = os.path.join('content', 'categories', folder_name)
    
    # Safely create the directory structure
    os.makedirs(dir_path, exist_ok=True)
    
    # Write the language-specific _index file
    file_path = os.path.join(dir_path, f'_index.{lang}.md')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f'---\ntitle: "{localized_name}"\n---\n')

def main():
    with open('categories.json', 'r', encoding='utf-8') as f:
        hierarchy = json.load(f)

    langs = ['es', 'en', 'de']
    parent_to_child = {lang: {} for lang in langs}
    child_to_parent = {lang: {} for lang in langs}
    display_trees = {lang: {} for lang in langs}

    es_to_lang = {}
    slug_to_es_proper = {} # Fuzzy matching dictionary

    # 1. Build logic maps and the fuzzy translation dictionary
    for es_parent, data in hierarchy.items():
        es_to_lang[es_parent] = {l: data.get(l, es_parent) if l != 'es' else es_parent for l in langs}

        for lang in langs:
            parent_name = es_to_lang[es_parent][lang]
            parent_to_child[lang][parent_name] = set()
            display_trees[lang][parent_name] = []

            # Map ANY language's slug back to the master Spanish proper name
            slug_to_es_proper[slugify(parent_name)] = es_parent 

            for es_child, child_translations in data.get('children', {}).items():
                es_to_lang[es_child] = {l: child_translations.get(l, es_child) if l != 'es' else es_child for l in langs}
                child_name = es_to_lang[es_child][lang]

                parent_to_child[lang][parent_name].add(child_name)
                child_to_parent[lang][child_name] = parent_name
                display_trees[lang][parent_name].append(child_name)

                # Map ANY language's slug back to the master Spanish proper name
                slug_to_es_proper[slugify(child_name)] = es_child

    # 2. Enforce Taxonomy Logic & Master-Slave Translation
    for root, _, files in os.walk('content/posts'):
        for filename in files:
            if not filename.endswith('.md'): continue

            filepath = os.path.join(root, filename)
            lang = 'es'
            base_filename = filename

            for l in ['en', 'de']:
                if filename.endswith(f'.{l}.md'):
                    lang = l
                    base_filename = filename.replace(f'.{l}.md', '.md')
                    break

            master_filepath = os.path.join(root, base_filename) if lang != 'es' else filepath
            if not os.path.exists(master_filepath): continue

            # Read the master (Spanish) categories
            with open(master_filepath, 'r', encoding='utf-8') as f:
                master_content = f.read()

            # Extract frontmatter block securely
            master_match = re.search(r'^(---\s*\n)(.*?\n)(---\s*\n)', master_content, re.DOTALL)
            if not master_match: continue
            master_fm = master_match.group(2)

            # Extract the raw categories string (handles multi-line YAML)
            cat_match = re.search(r'^categories:\s*(.*?)(?=\n[a-zA-Z]|\Z)', master_fm, re.MULTILINE | re.DOTALL)
            if not cat_match: continue

            raw_cats = cat_match.group(1).strip()
            extracted_cats = []

            # Smart Parse: YAML Bulleted List vs Inline Array
            if '\n' in raw_cats or raw_cats.startswith('-'):
                extracted_cats = re.findall(r'^[ \t]*[-*]\s*["\']?(.*?)["\']?$', raw_cats, re.MULTILINE)
            else:
                raw_cats = raw_cats.strip('[]')
                extracted_cats = [c.strip(' "\'') for c in raw_cats.split(',') if c.strip()]

            # Fuzzy match extracted categories against the master list
            es_categories = set()
            for cat in extracted_cats:
                slug = slugify(cat)
                if slug in slug_to_es_proper:
                    es_categories.add(slug_to_es_proper[slug])
                else:
                    es_categories.add(cat) # Preserve unknown categories

            # Apply "iff" hierarchy logic
            processed_es_categories = set(es_categories)
            for cat in es_categories:
                if cat in child_to_parent['es']:
                    processed_es_categories.add(child_to_parent['es'][cat])

            for parent, children in parent_to_child['es'].items():
                if parent in processed_es_categories:
                    if children and not any(child in processed_es_categories for child in children):
                        processed_es_categories.remove(parent)

            # Translate correctly
            target_categories = set()
            for es_cat in processed_es_categories:
                if es_cat in es_to_lang:
                    target_categories.add(es_to_lang[es_cat][lang])
                else:
                    target_categories.add(es_cat)

            # Overwrite the target file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            match = re.match(r'^(---\s*\n)(.*?\n)(---\s*\n)', content, re.DOTALL)
            if not match: continue
            pre, fm, post = match.groups()

            # Format cleanly as an inline array
            new_cat_str = 'categories: ["' + '", "'.join(sorted(list(target_categories))) + '"]'

            # Swap out the entire old category block
            new_fm = re.sub(r'^categories:\s*(?:\[.*?\]|.*?(?=\n[a-zA-Z]|\Z))', new_cat_str, fm, flags=re.MULTILINE | re.DOTALL)

            # Ensure the frontmatter block safely ends with a newline
            if not new_fm.endswith('\n'):
                new_fm += '\n'

            if new_fm != fm:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(pre + new_fm + post + content[match.end():])
                print(f"Cleaned, Synced, and Translated: {filename}")

    # 3. Inject Multilingual Menu into hugo.toml & Generate Index Files
    toml_lines = []
    menu_labels = {'es': 'Categorías', 'en': 'Categories', 'de': 'Kategorien'}

    for lang in langs:
        base_url = f'/{lang}/categories/' if lang != 'es' else '/categories/'
        
        toml_lines.append(f'[[languages.{lang}.menu.main]]\n  name = "{menu_labels[lang]}"\n  identifier = "menu-cats"\n  url = "/categories/"\n  weight = 15\n')
        
        weight_counter = 1
        for parent, children in display_trees[lang].items():
            parent_id = f"cat-{lang}-{slugify(parent)}"
            
            # Lookup canonical Spanish name and generate taxonomy folder/index
            es_parent = slug_to_es_proper.get(slugify(parent), parent)
            generate_taxonomy_index(es_parent, lang, parent)
            es_parent_folder = es_parent.lower()
            
            # Write parent category using the Spanish folder path
            toml_lines.append(f'[[languages.{lang}.menu.main]]\n  name = "{parent}"\n  identifier = "{parent_id}"\n  url = "{base_url}{es_parent_folder}/"\n  parent = "menu-cats"\n  weight = {weight_counter}\n')
            
            # Write child categories attached to this specific parent
            child_weight = 1
            for child in children:
                # Lookup canonical Spanish name and generate taxonomy folder/index
                es_child = slug_to_es_proper.get(slugify(child), child)
                generate_taxonomy_index(es_child, lang, child)
                es_child_folder = es_child.lower()
                
                toml_lines.append(f'[[languages.{lang}.menu.main]]\n  name = "{child}"\n  url = "{base_url}{es_child_folder}/"\n  parent = "{parent_id}"\n  weight = {child_weight}\n')
                child_weight += 1
            
            weight_counter += 1

    menu_block = '\n'.join(toml_lines)

    with open('hugo.toml', 'r', encoding='utf-8') as f:
        hugo_config = f.read()

    pattern = r'(# BEGIN MENU CATEGORIES\n)(.*?)(# END MENU CATEGORIES)'
    updated_config = re.sub(pattern, f'\\1{menu_block}\\3', hugo_config, flags=re.DOTALL)

    with open('hugo.toml', 'w', encoding='utf-8') as f:
        f.write(updated_config)
        
    print("\nSuccessfully injected updated menu directly into hugo.toml and generated taxonomy indexes.")

if __name__ == "__main__":
    main()
