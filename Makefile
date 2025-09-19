brain-games:
	uv run brain-games
build:
	uv build
install:
	uv sync
lint:
	uv run ruff check brain_games
lint-fix:
	uv run ruff check brain_games --fix
package-install:
	uv tool install dist/*.whl
package-reinstall:
	uv tool install --force dist/*whl