.PHONY: preview push

preview: hugo.toml
	hugo server -D

hugo.toml: categories.json
	python3 sync_categories.py

push: hugo.toml
	@read -p "Enter commit message: " msg; \
	git add .; \
	git commit -m "$$msg" || true; \
	git push origin main
