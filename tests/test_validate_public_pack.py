"""Synthetic fixtures only; no services, accounts or networks are accessed."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PACK = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('validator', PACK / 'scripts/validate_public_pack.py')
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='pack-fixture-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'pack'
        shutil.copytree(PACK, self.root, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))

    def extra(self, text):
        (self.root / 'fixture.md').write_text(text)

    def categories(self, markers=()):
        return {f['category'] for f in v.validate(self.root, markers)}

    def assert_path_diagnostics(self, sensitive, category, markers=(), safe_path=None):
        argv = [sys.executable, '-B', str(PACK / 'scripts/validate_public_pack.py'), str(self.root)]
        if markers:
            marker_file = Path(self.tmp.name) / 'markers.json'
            marker_file.write_text(json.dumps(list(markers)))
            argv.extend(['--markers-file', str(marker_file)])
        result = subprocess.run(argv, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        for stream in (result.stdout, result.stderr):
            self.assertFalse(any(value in stream for value in sensitive),
                             'Sensitive fixture value disclosed in CLI output')
        findings = json.loads(result.stdout)['findings']
        self.assertIn(category, {f['category'] for f in findings})
        structured = v.validate(self.root, markers)
        self.assertFalse(any(value in json.dumps(structured) for value in sensitive),
                         'Sensitive fixture value disclosed by validate()')
        self.assertEqual(findings, structured)
        if safe_path:
            self.assertIn({'file': safe_path, 'category': category}, structured)
        return structured

    def test_sensitive_basename_is_not_disclosed(self):
        fake = 'gh' + 'p_' + 'B' * 36
        (self.root / (fake + '.md')).write_text('Synthetic fixture')
        self.assert_path_diagnostics([fake], 'credential-token')

    def test_sensitive_parent_is_not_disclosed(self):
        fake = 'gh' + 'p_' + 'C' * 36
        parent = self.root / fake
        parent.mkdir()
        (parent / 'ordinary.md').write_text('[missing](absent.md)')
        findings = self.assert_path_diagnostics([fake], 'broken-link')
        self.assertIn('credential-token', {f['category'] for f in findings})

    def test_private_marker_basename_and_parent(self):
        marker = 'private-' + 'synthetic-review-marker'
        (self.root / (marker + '.md')).write_text('Synthetic fixture')
        parent = self.root / marker
        parent.mkdir()
        (parent / 'ordinary.md').write_text('[missing](absent.md)')
        findings = self.assert_path_diagnostics([marker], 'private-marker', [marker])
        paths = {f['file'] for f in findings if f['category'] == 'private-marker'}
        self.assertEqual(len(paths), 2)  # Opaque labels must still distinguish files.

    def test_sensitive_symlink_path(self):
        fake = 'gh' + 'p_' + 'D' * 36
        for name, target in [(fake + '.md', self.root / 'README.md'),
                             (fake + '-dir', self.root / 'skills')]:
            try:
                (self.root / name).symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest('Platform cannot create test symlinks')
        self.assert_path_diagnostics([fake], 'symlink')

    def test_sensitive_unsupported_file(self):
        fake = 'gh' + 'p_' + 'E' * 36
        (self.root / (fake + '.bin')).write_bytes(b'synthetic')
        self.assert_path_diagnostics([fake], 'unsupported-file')

    def test_sensitive_metadata_path(self):
        fake = 'gh' + 'p_' + 'F' * 36
        parent = self.root / fake
        parent.mkdir()
        (parent / 'SKILL.md').write_text('Invalid synthetic metadata')
        self.assert_path_diagnostics([fake], 'invalid-metadata')

    def test_sensitive_unreadable_text_path(self):
        fake = 'gh' + 'p_' + 'G' * 36
        (self.root / (fake + '.md')).write_bytes(bytes([255]))
        self.assert_path_diagnostics([fake], 'unreadable-text')

    def test_sensitive_cli_argument_error(self):
        fake = 'gh' + 'p_' + 'H' * 36
        result = subprocess.run([sys.executable, '-B', str(PACK / 'scripts/validate_public_pack.py'),
                                 str(self.root), '--unknown-' + fake],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(fake in result.stdout or fake in result.stderr,
                         'Sensitive fixture value disclosed by argument error')
        self.assertIn('Invalid arguments', result.stderr)

    def test_sensitive_root_error(self):
        fake = 'gh' + 'p_' + 'I' * 36
        root = Path(self.tmp.name) / fake
        try:
            root.symlink_to(root)
        except (OSError, NotImplementedError):
            self.skipTest('Platform cannot create test symlinks')
        result = subprocess.run([sys.executable, '-B', str(PACK / 'scripts/validate_public_pack.py'), str(root)],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertFalse(fake in result.stdout or fake in result.stderr,
                         'Sensitive fixture value disclosed by root error')
        self.assertIn('invalid-root', result.stdout)
        self.assertEqual(v.validate(root), [{'file': '.', 'category': 'invalid-root'}])

    def test_safe_filename_remains_useful(self):
        self.extra('[missing](absent.md)')
        self.assert_path_diagnostics([], 'broken-link', safe_path='fixture.md')

    def test_root_license_is_supported(self):
        (self.root / 'LICENSE').write_text('MIT License\nSynthetic license fixture.\n')
        self.assertEqual(v.validate(self.root), [])

    def test_missing_license_is_rejected(self):
        (self.root / 'LICENSE').unlink(missing_ok=True)
        self.assertIn({'file': 'LICENSE', 'category': 'required-file'}, v.validate(self.root))

    def test_empty_license_is_rejected(self):
        (self.root / 'LICENSE').write_text('  \n')
        self.assertIn({'file': 'LICENSE', 'category': 'required-file'}, v.validate(self.root))

    def test_other_extensionless_files_are_rejected(self):
        # Remove the fixture's uppercase file first: on case-insensitive
        # filesystems writing lowercase would otherwise reuse its name.
        (self.root / 'LICENSE').unlink()
        for relative in ('UNRELATED', 'license', 'references/LICENSE'):
            with self.subTest(relative=relative):
                p = self.root / relative
                p.parent.mkdir(exist_ok=True)
                p.write_text('Synthetic text')
                self.assertIn({'file': relative, 'category': 'unsupported-file'}, v.validate(self.root))
                p.unlink()

    def test_license_content_is_scanned(self):
        fake = 'gh' + 'p_' + 'J' * 36
        marker = 'synthetic-' + 'license-private-marker'
        (self.root / 'LICENSE').write_text(fake + '\n' + marker)
        findings = self.assert_path_diagnostics([fake, marker], 'credential-token', [marker])
        self.assertIn({'file': 'LICENSE', 'category': 'private-marker'}, findings)

    def test_approved_credit_exact_public_fields(self):
        name = 'Deve' + 'roax'
        credit = name + ' — prepared with Hermes Agent assistance.'
        for relative in ('README.md', 'ATTRIBUTION.md'):
            (self.root / relative).write_text(credit + '\n')
        self.assertEqual(v.validate(self.root, [name]), [])
        # Approval never suppresses a different configured marker.
        self.assertIn('private-marker', self.categories(['Hermes Agent']))

    def test_approved_credit_does_not_exempt_other_occurrences(self):
        name = 'Deve' + 'roax'
        credit = name + ' — prepared with Hermes Agent assistance.'
        for relative, text in [('README.md', name), ('ATTRIBUTION.md', credit + '\n' + name),
                               ('README.md', 'Prefix ' + credit),
                               ('README.md', credit + ' suffix'), ('fixture.md', credit),
                               ('LICENSE', credit)]:
            with self.subTest(relative=relative):
                p = self.root / relative
                previous = p.read_text() if p.exists() else None
                p.write_text(text)
                self.assertIn({'file': relative, 'category': 'private-marker'},
                              v.validate(self.root, [name]))
                if previous is None:
                    p.unlink()
                else:
                    p.write_text(previous)

    def test_approved_credit_keeps_credentials_and_paths_scanned(self):
        name = 'Deve' + 'roax'
        credit = name + ' — prepared with Hermes Agent assistance.'
        fake = 'gh' + 'p_' + 'K' * 36
        (self.root / 'README.md').write_text(credit + '\n' + fake)
        self.assert_path_diagnostics([fake], 'credential-token', [name])
        (self.root / (name + '.md')).write_text(credit)
        self.assert_path_diagnostics([fake, name], 'private-marker', [name])

    def test_clean_pack(self):
        self.assertEqual(v.validate(self.root), [])

    def test_clean_synthetic_fixture(self):
        self.extra('# Synthetic fixture\n[Readme](README.md)\nNo live data.\n')
        self.assertEqual(v.validate(self.root), [])

    def test_broken_link(self):
        self.extra('[missing](missing.md)')
        self.assertIn('broken-link', self.categories())

    def test_broken_literal_reference(self):
        self.extra('Read `references/missing.md`.')
        self.assertIn('broken-link', self.categories())

    def test_reference_style_link(self):
        self.extra('[guide][g]\n\n[g]: missing.md\n')
        self.assertIn('broken-link', self.categories())

    def test_private_absolute_path(self):
        self.extra('/' + 'Users/' + 'synthetic_person/private.txt')
        self.assertIn('personal-absolute-path', self.categories())

    def test_windows_absolute_path(self):
        self.extra('C:' + '\\' + 'Users' + '\\' + 'synthetic_person')
        self.assertIn('personal-absolute-path', self.categories())

    def test_private_marker(self):
        marker = 'fictional-' + 'account-marker'
        self.extra(marker.upper())
        self.assertIn('private-marker', self.categories([marker]))

    def test_fake_credential_cli_suppresses_value(self):
        fake = 'gh' + 'p_' + 'A' * 36
        self.extra('Synthetic secret shape: ' + fake)
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            status = v.main([str(self.root)])
        self.assertEqual(status, 1)
        self.assertFalse(fake in output.getvalue() or fake in errors.getvalue(),
                         'Sensitive fixture value disclosed in CLI output')
        result = json.loads(output.getvalue())
        self.assertIn({'file': 'fixture.md', 'category': 'credential-token'}, result['findings'])
        for finding in result['findings']:
            self.assertEqual(set(finding), {'file', 'category'})

    def test_private_key(self):
        self.extra('-----BEGIN ' + 'PRIVATE KEY-----')
        self.assertIn('private-key', self.categories())

    def test_credential_assignment(self):
        self.extra('password' + '=' + 'Z' * 24)
        self.assertIn('credential-assignment', self.categories())

    def test_authenticated_url(self):
        self.extra('https://example.invalid/callback?' + 'password=' + 'Z' * 24)
        self.assertIn('authenticated-url', self.categories())

    def test_missing_section(self):
        p = self.root / 'skills/macos-service-maintenance/SKILL.md'
        p.write_text(p.read_text().replace('## When not to use', '## Omitted boundary'))
        self.assertIn('required-section', self.categories())

    def test_invalid_metadata_and_missing_file(self):
        p = self.root / 'skills/macos-service-maintenance/SKILL.md'
        p.write_text(p.read_text().replace('version: "0.1.0"', 'version: [1]'))
        (self.root / 'ATTRIBUTION.md').unlink()
        self.assertTrue({'invalid-metadata', 'required-file'} <= self.categories())

    def test_duplicate_name(self):
        p = self.root / 'skills/duplicate/SKILL.md'
        p.parent.mkdir()
        p.write_text((self.root / 'skills/macos-service-maintenance/SKILL.md').read_text())
        self.assertIn('duplicate-skill-name', self.categories())

    def test_escaping_link(self):
        self.extra('[outside](../outside.md)')
        self.assertIn('escaping-link', self.categories())

    def test_symlink_is_rejected(self):
        p = self.root / 'alias.md'
        try:
            p.symlink_to(self.root / 'README.md')
        except (OSError, NotImplementedError):
            self.skipTest('Platform cannot create test symlinks')
        self.assertIn('symlink', self.categories())

    def test_invalid_private_marker_file_is_bounded(self):
        p = Path(self.tmp.name) / 'markers.json'
        p.write_text('{}')
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = v.main([str(self.root), '--markers-file', str(p)])
        self.assertEqual(status, 2)
        self.assertEqual(json.loads(out.getvalue()), {'file': '<marker-file>', 'category': 'invalid-marker-file'})


if __name__ == '__main__':
    unittest.main()
