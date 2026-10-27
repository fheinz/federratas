.PHONY: preview push

preview: hugo.toml
	hugo server -D

hugo.toml: categories.json sync_categories.py
	python3 sync_categories.py

push: hugo.toml
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "Error: Uncommitted changes detected. Please commit them before pushing."; \
		exit 1; \
	fi
	git push origin main
