.PHONY: preview push

preview: hugo.toml
	python3 sync_categories.py
	hugo server -D

push: hugo.toml
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "Error: Uncommitted changes detected. Please commit them before pushing."; \
		exit 1; \
	fi
	git push origin main
