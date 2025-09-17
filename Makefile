brain-games:
	uv run brain-games
build:
	uv build
install:
	uv sync
package-install:
	uv tool install dist/*.whl