set default-list

check: lint typecheck fmt-check test

test:
    uv run pytest

lint:
    uv run ruff check

typecheck:
    uv run ty check

fmt-check:
    uv run ruff format --check

fmt:
    uv run ruff format

install:
    uv sync --extra visual

build:
    uv build --clear --no-sources
