"""Extract reviewed release notes from the project changelog."""

import argparse
import re
from pathlib import Path

VERSION_PATTERN = re.compile(r'^\d+\.\d+\.\d+$')
RELEASE_HEADING_PATTERN = re.compile(
    r'(?m)^## \[(?P<version>\d+\.\d+\.\d+)\]'
    r'(?:\([^\n)]+\))?(?: - [^\n]+)?\s*$'
)


def parse_version(version: str) -> tuple[int, int, int]:
    """Parse the project's strict X.Y.Z release format."""
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f'invalid version {version!r}; expected X.Y.Z')
    major, minor, patch = version.split('.')
    return int(major), int(minor), int(patch)


def extract_release_notes(content: str, version: str) -> str:
    """Return the body of one generated changelog release section."""
    parse_version(version)
    headings = list(RELEASE_HEADING_PATTERN.finditer(content))
    matches = [heading for heading in headings if heading.group('version') == version]
    if len(matches) != 1:
        raise RuntimeError(
            f'expected exactly one CHANGELOG.md section for {version}, found {len(matches)}'
        )

    match = matches[0]
    next_heading = next((heading for heading in headings if heading.start() > match.start()), None)
    end = next_heading.start() if next_heading else len(content)
    notes = content[match.end() : end].strip()
    if not notes:
        raise RuntimeError(f'CHANGELOG.md section for {version} is empty')
    return f'{notes}\n'


def write_release_notes(version: str, changelog: Path, output: Path) -> None:
    """Write one version's reviewed changelog body to a release-notes file."""
    output.write_text(extract_release_notes(changelog.read_text(), version))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('version')
    parser.add_argument('--changelog', type=Path, default=Path('CHANGELOG.md'))
    parser.add_argument('--output', type=Path, default=Path('release-notes.md'))

    args = parser.parse_args()
    write_release_notes(args.version, args.changelog, args.output)


if __name__ == '__main__':
    main()
