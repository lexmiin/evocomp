import unittest

from scripts.prepare_release import extract_release_notes
from scripts.prepare_release import parse_version


class PrepareReleaseTests(unittest.TestCase):
    def test_parse_version(self) -> None:
        self.assertEqual(parse_version('1.2.3'), (1, 2, 3))

    def test_rejects_non_release_version(self) -> None:
        for version in ('v1.2.3', '1.2', '1.2.3rc1', 'one.two.three'):
            with self.subTest(version=version), self.assertRaises(ValueError):
                parse_version(version)

    def test_extracts_linked_release_section_body(self) -> None:
        changelog = """# Changelog

## [0.2.0](https://example.test/compare/v0.1.0..v0.2.0) - 2026-08-07

### Changes

- algorithms: improve crossover

## [0.1.0] - 2026-08-01

### Changes

- project: initial release
"""
        self.assertEqual(
            extract_release_notes(changelog, '0.2.0'),
            '### Changes\n\n- algorithms: improve crossover\n',
        )

    def test_requires_nonempty_release_section(self) -> None:
        with self.assertRaises(RuntimeError):
            extract_release_notes('## [0.1.0] - 2026-08-07\n', '0.1.0')


if __name__ == '__main__':
    unittest.main()
