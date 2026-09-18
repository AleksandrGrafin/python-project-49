.PHONY: install test lint build

install:
	pip install --user .
brain-games:
	brain-games
build:
	python3 -m build
package-install:
	pip install --user dist/*.whl
lint:
	ruff check brain_games
test:
	uv run pytest || [ $$? -eq 5 ]

