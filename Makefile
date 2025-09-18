brain-games:
	uv run brain-games
build:
	uv build
install:
	uv sync
lint:
	uv run ruff check brain_games
package-install:
	uv tool install dist/*.whl