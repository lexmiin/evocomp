set default-list

check: lint typecheck format-check test

test:
    uv run pytest

lint:
    uv run ruff check

typecheck:
    uv run ty check

format-check:
    uv run ruff format --check

format:
    uv run ruff format

install:
    uv sync --extra visual

build:
    uv build --clear --no-sources
