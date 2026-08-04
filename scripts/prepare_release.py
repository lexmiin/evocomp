"""Prepare package versions and extract reviewed release notes."""

import argparse
import re
from pathlib import Path

VERSION_PATTERN = re.compile(r'^\d+\.\d+\.\d+$')
PROJECT_PATTERN = re.compile(r'(?ms)^\[project\]\n(?P<body>.*?)(?=^\[|\Z)')
PROJECT_VERSION_PATTERN = re.compile(r'(?m)^version = "(?P<version>[^"]+)"$')
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


def update_project_version(content: str, version: str) -> str:
    """Update exactly one version inside the pyproject [project] table."""
    new_version = parse_version(version)
    project_match = PROJECT_PATTERN.search(content)
    if project_match is None:
        raise RuntimeError('pyproject.toml has no [project] table')

    project_body = project_match.group('body')
    version_matches = list(PROJECT_VERSION_PATTERN.finditer(project_body))
    if len(version_matches) != 1:
        raise RuntimeError(
            'expected exactly one version in the pyproject [project] table, '
            f'found {len(version_matches)}'
        )

    current = version_matches[0].group('version')
    if new_version < parse_version(current):
        raise ValueError(f'new version {version} must not be lower than current version {current}')

    updated_body = PROJECT_VERSION_PATTERN.sub(f'version = "{version}"', project_body)
    return (
        content[: project_match.start('body')] + updated_body + content[project_match.end('body') :]
    )


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


def prepare(version: str, pyproject: Path) -> None:
    """Update the package version file in place."""
    content = pyproject.read_text()
    pyproject.write_text(update_project_version(content, version))


def write_release_notes(version: str, changelog: Path, output: Path) -> None:
    """Write one version's reviewed changelog body to a release-notes file."""
    output.write_text(extract_release_notes(changelog.read_text(), version))


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', required=True)

    prepare_parser = subparsers.add_parser('prepare')
    prepare_parser.add_argument('version')
    prepare_parser.add_argument('--pyproject', type=Path, default=Path('pyproject.toml'))

    notes_parser = subparsers.add_parser('notes')
    notes_parser.add_argument('version')
    notes_parser.add_argument('--changelog', type=Path, default=Path('CHANGELOG.md'))
    notes_parser.add_argument('--output', type=Path, default=Path('release-notes.md'))

    args = parser.parse_args()
    if args.command == 'prepare':
        prepare(args.version, args.pyproject)
    else:
        write_release_notes(args.version, args.changelog, args.output)


if __name__ == '__main__':
    main()
