#!/usr/bin/env python3
"""Small, offline, heuristic review aid; not legal or secret-free certification."""
import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

EXPECTED = {
    "macos-service-maintenance": ["macos"],
    "social-content-candidate-operations": ["macos", "linux", "windows"],
    "local-messaging-gateway-operations": ["macos", "linux", "windows"],
}
SECTIONS = (
    "When to use", "When not to use", "Prerequisites", "Safety boundaries",
    "Workflow", "Verification checklist", "Synthetic worked example", "Known limitations",
)
REQUIRED = ("README.md", "ATTRIBUTION.md", "LICENSE", "scripts/validate_public_pack.py",
            "tests/test_validate_public_pack.py")
PATTERNS = {
    "personal-absolute-path": re.compile(
        r"/(?:Users|home)/[^\s/<>]+|[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]", re.I),
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----"),
    "credential-token": re.compile(
        r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
        r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16})\b"),
    "credential-assignment": re.compile(
        r"\b(?:api[_-]?key|password|secret|access[_-]?token)\s*[:=]\s*[\"']?[A-Za-z0-9_+/=-]{16,}", re.I),
    "bearer-credential": re.compile(r"\bBearer\s+[A-Za-z0-9_.~+/-]{20,}", re.I),
    "authenticated-url": re.compile(
        r"https?://[^\s<>]+(?:[?&](?:password|token|api_key|secret)=)[^\s<>]+|"
        r"https?://[^\s/:@]+:[^\s/@]+@", re.I),
}


def scan_text(text, markers=()):
    categories = {category for category, pattern in PATTERNS.items() if pattern.search(text)}
    if any(marker.casefold() in text.casefold() for marker in markers):
        categories.add("private-marker")
    return sorted(categories)


def scan_document(text, relative, markers=()):
    # Only the approved whole credit line in these two public fields may
    # contain the maintainer-name marker. All credential patterns still run.
    categories = set(scan_text(text))
    public_name = 'Deve' + 'roax'
    credit = public_name + ' — prepared with Hermes Agent assistance.'
    for marker in markers:
        checked = text
        if relative in {'README.md', 'ATTRIBUTION.md'} and marker.casefold() == public_name.casefold():
            checked = '\n'.join(line for line in text.splitlines() if line != credit)
        if marker.casefold() in checked.casefold():
            categories.add('private-marker')
    return sorted(categories)


def metadata(text):
    """Parse only this edition's flat YAML subset; reject unsupported syntax."""
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("frontmatter")
    header, body = text[4:].split("\n---\n", 1)
    result = {}
    for line in header.splitlines():
        match = re.fullmatch(r"([a-z]+): (.+)", line)
        if not match or match[1] in result:
            raise ValueError("metadata")
        key, value = match.groups()
        if value.startswith(('"', '[')):
            value = json.loads(value)
        elif not re.fullmatch(r"[a-z][a-z0-9-]*", value):
            raise ValueError("metadata")
        result[key] = value
    if set(result) != {"name", "description", "version", "platforms"}:
        raise ValueError("metadata")
    if not isinstance(result['name'], str) or not re.fullmatch(r"[a-z][a-z0-9-]{0,63}", result['name']):
        raise ValueError("metadata")
    if not isinstance(result['description'], str) or not 1 <= len(result['description']) <= 1024:
        raise ValueError("metadata")
    if result['version'] != '0.1.0' or not isinstance(result['platforms'], list):
        raise ValueError("metadata")
    if not body.strip():
        raise ValueError("body")
    return result, body


def markdown_targets(text):
    # Fenced code is illustrative, not Markdown navigation.
    prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
    targets = re.findall(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", prose)
    definitions = dict(re.findall(r"^\s*\[([^\]]+)\]:\s*(\S+)", prose, re.M))
    targets.extend(definitions.values())
    for label, reference in re.findall(r"\[([^\]\n]+)\]\[([^\]\n]*)\]", prose):
        if (reference or label) not in definitions:
            targets.append("__undefined_reference__")
    # Literal backtick paths, not arbitrary command strings or conceptual roots.
    targets.extend(re.findall(
        r"`((?:references|examples|scripts|tests)/[^`\s]+\.(?:md|py|json|yaml|txt))`", prose))
    return targets


def validate(root, markers=()):
    try:
        root = Path(root).resolve()
        root_is_dir = root.is_dir()
    except (OSError, RuntimeError, ValueError):
        return [{"file": ".", "category": "invalid-root"}]
    findings = set()
    def add(path, category):
        findings.add((path, category))
        # Also detect paths skipped before content scanning (e.g. symlinks).
        for sensitive_category in scan_text(path, markers):
            findings.add((path, sensitive_category))
    if not root_is_dir:
        return [{"file": ".", "category": "missing-root"}]
    texts = {}
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in list(dirs):
            p = Path(directory) / name
            if p.is_symlink():
                add(p.relative_to(root).as_posix(), 'symlink'); dirs.remove(name)
        for name in files:
            p = Path(directory) / name
            relative = p.relative_to(root).as_posix()
            if p.is_symlink():
                add(relative, 'symlink'); continue
            if relative != 'LICENSE' and p.suffix not in {'.md', '.py', '.json', '.txt'}:
                add(relative, 'unsupported-file'); continue
            try:
                text = p.read_text(encoding='utf-8')
            except (OSError, UnicodeError):
                add(relative, 'unreadable-text'); continue
            texts[relative] = text
            for category in set(scan_text(relative, markers)) | set(scan_document(text, relative, markers)):
                add(relative, category)
    for required in REQUIRED:
        if required not in texts or not texts[required].strip():
            add(required, 'required-file')
    names = set()
    seen = set()
    for relative, text in texts.items():
        p = Path(relative)
        if p.name == 'SKILL.md':
            try:
                meta, body = metadata(text)
                name = meta['name']
                if name in names:
                    add(relative, 'duplicate-skill-name')
                names.add(name)
                if relative != 'skills/' + name + '/SKILL.md' or name not in EXPECTED:
                    add(relative, 'skill-identity')
                elif meta['platforms'] != EXPECTED[name]:
                    add(relative, 'platform-metadata')
                seen.add(relative)
                sections = dict(re.findall(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", body, re.M | re.S))
                for section in SECTIONS:
                    if not sections.get(section, '').strip():
                        add(relative, 'required-section')
                for folder in ('references', 'examples'):
                    prefix = p.parent.as_posix() + '/' + folder + '/'
                    if not any(f.startswith(prefix) and v.strip() for f, v in texts.items()):
                        add(relative, 'required-support-file')
            except (ValueError, TypeError, KeyError):
                add(relative, 'invalid-metadata')
        if p.suffix == '.md':
            for target in markdown_targets(text):
                target = target.strip('<>')
                try:
                    url = urlsplit(target)
                    if url.scheme in {'http', 'https', 'mailto'}:
                        continue
                    if url.scheme or target.startswith('/'):
                        add(relative, 'nonrelative-link'); continue
                    if not url.path:
                        continue  # Anchor validation is intentionally out of scope.
                    candidate = (root / p.parent / unquote(url.path)).resolve()
                    if not candidate.is_relative_to(root):
                        add(relative, 'escaping-link')
                    elif not candidate.is_file() or candidate.relative_to(root).as_posix() not in texts:
                        add(relative, 'broken-link')
                except (ValueError, OSError, RuntimeError):
                    add(relative, 'invalid-link')
    for name in EXPECTED:
        required = 'skills/' + name + '/SKILL.md'
        if required not in seen:
            add(required, 'required-skill')
    # One output boundary for every category and for direct validate() callers.
    # Opaque, per-run labels reveal neither path fragments nor path hashes.
    labels = {}
    for path in sorted({path for path, _ in findings}):
        if scan_text(path, markers):
            labels[path] = '<redacted-path-' + str(len(labels) + 1) + '>'
    return [{'file': labels.get(f, f), 'category': c} for f, c in sorted(findings)]


class BoundedArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # argparse's default error echoes untrusted argv, potentially a secret.
        self.exit(2, 'Invalid arguments; use --help.\n')


def main(argv=None):
    parser = BoundedArgumentParser(prog='validate_public_pack', description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--markers-file', type=Path)
    args = parser.parse_args(argv)
    markers = []
    if args.markers_file:
        try:
            markers = json.loads(args.markers_file.read_text())
            if not isinstance(markers, list) or not all(isinstance(m, str) and m.strip() for m in markers):
                raise ValueError('markers')
        except (OSError, UnicodeError, ValueError, RuntimeError):
            print(json.dumps({'file': '<marker-file>', 'category': 'invalid-marker-file'}))
            return 2
    findings = validate(args.root, markers)
    print(json.dumps({'findings': findings, 'finding_count': len(findings),
                      'status': 'FAIL' if findings else 'PASS',
                      'scope': 'Limited heuristic documentation checks; no legal or operational clearance.'}, indent=2))
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main())
