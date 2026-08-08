import pytest

from scripts.prepare_release import extract_release_notes
from scripts.prepare_release import parse_version


def test_parse_version() -> None:
    assert parse_version('1.2.3') == (1, 2, 3)


@pytest.mark.parametrize('version', ['v1.2.3', '1.2', '1.2.3rc1', 'one.two.three'])
def test_rejects_non_release_version(version: str) -> None:
    with pytest.raises(ValueError):
        parse_version(version)


def test_extracts_linked_release_section_body() -> None:
    changelog = """# Changelog

## [0.2.0](https://example.test/compare/v0.1.0..v0.2.0) - 2026-08-07

### Changes

- algorithms: improve crossover

## [0.1.0] - 2026-08-01

### Changes

- project: initial release
"""
    assert (
        extract_release_notes(changelog, '0.2.0')
        == '### Changes\n\n- algorithms: improve crossover\n'
    )


def test_requires_nonempty_release_section() -> None:
    with pytest.raises(RuntimeError):
        extract_release_notes('## [0.1.0] - 2026-08-07\n', '0.1.0')
