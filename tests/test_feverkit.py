import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import feverkit


class FeverKitTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_manifest_valid_and_repos_reachable_metadata_recorded(self):
        profiles, links = feverkit.validate()
        self.assertEqual(profiles, 9)
        self.assertGreaterEqual(links, 40)
        _, catalog = feverkit.manifests()
        self.assertEqual(len(catalog), len(set(x['id'] for x in catalog)))

    def test_auto_detects_multiple_stacks(self):
        (self.project / 'package.json').write_text('{}')
        (self.project / 'project.godot').write_text('')
        (self.project / 'compose.yml').write_text('services: {}')
        plan = feverkit.make_plan(self.project, 'auto')
        self.assertEqual(set(plan['profiles']), {'core','fullstack','game','devops'})
        self.assertIn('game-testing', plan['skills'])

    def test_detects_rust_game_framework_not_every_rust_repo(self):
        (self.project / 'Cargo.toml').write_text('[package]\nname="sample"')
        self.assertNotIn('game', feverkit.detect(self.project))
        (self.project / 'Cargo.toml').write_text('[dependencies]\nbevy="0.16"')
        self.assertIn('game', feverkit.detect(self.project))

    def test_explicit_profile_includes_core_and_rejects_typo(self):
        plan = feverkit.make_plan(self.project, 'robotics')
        self.assertIn('core', plan['profiles'])
        self.assertIn('robotics', plan['profiles'])
        with self.assertRaises(ValueError):
            feverkit.make_plan(self.project, 'nonexistent')

    def test_dry_run_does_not_modify_project(self):
        plan = feverkit.make_plan(self.project, 'core')
        with contextlib.redirect_stdout(io.StringIO()):
            feverkit.install_plan(self.project, plan, execute=False, force=False)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_installs_scoped_skills_and_preserves_existing_markdown(self):
        (self.project / 'CLAUDE.md').write_text('# User rules\n\nKeep my style.\n')
        (self.project / 'AGENTS.md').write_text('# Agent rules\n\nDo not erase.\n')
        plan = feverkit.make_plan(self.project, 'core')
        with contextlib.redirect_stdout(io.StringIO()):
            feverkit.install_plan(self.project, plan, execute=True, force=False)
        self.assertTrue((self.project / '.claude/skills/feverkit-repo-scout/SKILL.md').exists())
        self.assertTrue((self.project / '.agents/skills/feverkit-repo-scout/SKILL.md').exists())
        self.assertTrue((self.project / '.claude/agents/feverkit-architect.md').exists())
        contents = (self.project / 'CLAUDE.md').read_text()
        self.assertTrue(contents.startswith('# User rules'))
        self.assertIn('Keep my style.', contents)
        self.assertIn('feverkit:start', contents)
        self.assertIn('Do not erase.', (self.project / 'AGENTS.md').read_text())
        self.assertIn('FeverKit recommended external tools', (self.project / '.feverkit/selected-tools.md').read_text())
        # Same plan should be idempotent and keep exactly one managed instruction block.
        with contextlib.redirect_stdout(io.StringIO()):
            feverkit.install_plan(self.project, plan, execute=True, force=False)
        self.assertEqual((self.project / 'CLAUDE.md').read_text().count('feverkit:start'), 1)

    def test_does_not_clobber_unknown_file_without_force(self):
        dst = self.project / '.claude/skills/feverkit-repo-scout/SKILL.md'
        dst.parent.mkdir(parents=True)
        dst.write_text('CUSTOM CONTENT')
        plan = feverkit.make_plan(self.project, 'core')
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            feverkit.install_plan(self.project, plan, execute=True, force=False)
        self.assertEqual(dst.read_text(), 'CUSTOM CONTENT')
        with contextlib.redirect_stdout(io.StringIO()):
            feverkit.install_plan(self.project, plan, execute=True, force=True)
        self.assertNotEqual(dst.read_text(), 'CUSTOM CONTENT')
        backups = list((self.project / '.feverkit/backups').glob('*/.claude/skills/feverkit-repo-scout/SKILL.md'))
        self.assertTrue(backups)
        self.assertEqual(backups[0].read_text(), 'CUSTOM CONTENT')

    def test_rejects_plan_for_another_project(self):
        plan = feverkit.make_plan(self.project, 'core')
        plan['project'] = '/wrong/project'
        with self.assertRaises(ValueError):
            feverkit.install_plan(self.project, plan, execute=True, force=False)

    def test_malformed_instruction_block_preflight(self):
        (self.project / 'CLAUDE.md').write_text('<!-- feverkit:start -->\nunclosed')
        plan = feverkit.make_plan(self.project, 'core')
        with self.assertRaises(ValueError):
            feverkit.install_plan(self.project, plan, execute=True, force=False)
        self.assertFalse((self.project / '.claude').exists())

    def test_symlink_escape_refused(self):
        with tempfile.TemporaryDirectory() as outside:
            (self.project / '.claude').symlink_to(outside, target_is_directory=True)
            plan = feverkit.make_plan(self.project, 'core')
            with self.assertRaises(ValueError):
                feverkit.install_plan(self.project, plan, execute=True, force=False)

    def test_vendor_preview_does_not_clone(self):
        with contextlib.redirect_stdout(io.StringIO()):
            feverkit.command_vendor(self.project, ['graphify'], execute=False)
        self.assertFalse((self.project / '.feverkit').exists())

    def test_source_routes_mark_uncertain_pages(self):
        data = json.loads((ROOT / 'manifest/site-routes.json').read_text())
        mapping = {r['path']:r['status'] for r in data['routes']}
        self.assertEqual(mapping['/unslop'], 'user-supplied')
        self.assertEqual(mapping['/launch'], 'user-supplied')


if __name__ == '__main__':
    unittest.main()
