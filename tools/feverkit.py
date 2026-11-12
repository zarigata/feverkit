#!/usr/bin/env python3
"""FeverKit: safe, stdlib-only environment plans for AI coding projects.

This CLI never runs third-party installers. Optional `vendor` only clones a selected
GitHub repository into an isolated directory after an explicit `--execute`.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- feverkit:start -->'
END = '<!-- feverkit:end -->'
VERSION = '0.1.0'
VALID_NAME = re.compile(r'^[a-z][a-z0-9-]*$')


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def manifests():
    return (read_json(ROOT / 'manifest/profiles.json')['profiles'],
            read_json(ROOT / 'manifest/tools.json')['tools'])


def detect(project: Path):
    """Non-invasive local heuristics; never reads credential files."""
    results = {'core': 'Default development workflow'}
    if any((project / name).exists() for name in
           ('package.json', 'pyproject.toml', 'requirements.txt', 'manage.py')):
        results['fullstack'] = 'Detected a Node.js or Python application'
    if (project / 'project.godot').exists() or (project / 'ProjectSettings/ProjectVersion.txt').exists():
        results['game'] = 'Detected Godot or Unity project metadata'
    cargo = project / 'Cargo.toml'
    if cargo.exists():
        # A Rust app alone is not assumed to be a game.
        results['core'] = 'Rust project detected'
        try:
            snippet = cargo.read_text(encoding='utf-8')[:12000].lower()
            if any(s in snippet for s in ('bevy', 'macroquad', 'ggez', 'godot', 'rapier')):
                results['game'] = 'Rust game framework detected'
        except (OSError, UnicodeError):
            pass
    if any((project / name).exists() for name in
           ('compose.yaml', 'compose.yml', 'docker-compose.yml', 'Dockerfile', 'kubernetes')):
        results['devops'] = 'Found container or deployment assets'
    if any((project / name).exists() for name in
           ('mcp.json', '.mcp.json', 'ollama', 'agents', 'langgraph.json')):
        results['ai-agents'] = 'Found agent/MCP configuration'
    if any((project / name).exists() for name in
           ('platformio.ini', 'arduino', 'firmware', 'idf_component.yml')):
        results['robotics'] = 'Found embedded/firmware project files'
    return results


def selected_profiles(project: Path, arg: str):
    definitions, _ = manifests()
    if arg.strip() == 'auto':
        return detect(project)
    names = [x.strip() for x in arg.split(',') if x.strip()]
    if 'all' in names:
        names = list(definitions)
    names = list(dict.fromkeys(['core', *names]))
    unknown = [n for n in names if n not in definitions]
    if unknown:
        raise ValueError(f'Unknown profiles: {", ".join(unknown)}')
    return {n: 'Explicit profile selection' for n in names}


def make_plan(project: Path, profile_arg: str):
    definitions, tools = manifests()
    selected = selected_profiles(project, profile_arg)
    skills = sorted({s for name in selected for s in definitions[name]['skills']})
    agents = sorted({a for name in selected for a in definitions[name]['agents']})
    chosen = sorted((t for t in tools if any(p in selected for p in t['profiles'])),
                    key=lambda t: (t['priority'], t['name'].casefold()))
    return {
        'schema_version': 1, 'feverkit_version': VERSION,
        'project': str(project.resolve()), 'selection': profile_arg,
        'profiles': selected, 'skills': skills, 'agents': agents,
        'external_tools': [t['id'] for t in chosen],
        'notes': [
            'Plan is a proposal; no third-party package has been installed.',
            'Applying copies only first-party FeverKit Markdown instructions into the project.',
            'Review upstream repositories and licenses separately before installation.'
        ]
    }


def validate():
    profiles, tools = manifests()
    ids = set()
    for t in tools:
        ident = t['id']
        if not VALID_NAME.fullmatch(ident) or ident in ids:
            raise ValueError(f'Invalid or duplicated tool id: {ident}')
        ids.add(ident)
        if t['url'] != f"https://github.com/{t['repo']}":
            raise ValueError(f"Unexpected GitHub URL for {ident}")
        if not t['profiles'] or any(x not in profiles for x in t['profiles']):
            raise ValueError(f"Invalid profiles for {ident}")
    for profile, spec in profiles.items():
        if not VALID_NAME.fullmatch(profile):
            raise ValueError(f'Invalid profile name: {profile}')
        for skill in spec['skills']:
            if not (ROOT / '.claude/skills' / skill / 'SKILL.md').is_file():
                raise ValueError(f'Missing skill: {skill}')
        for agent in spec['agents']:
            if not (ROOT / '.claude/agents' / (agent + '.md')).is_file():
                raise ValueError(f'Missing agent: {agent}')
    return len(profiles), len(tools)


def block_for(project: Path, profiles: dict, filename: str) -> str:
    where = '.claude/skills/feverkit-*/SKILL.md' if filename == 'CLAUDE.md' else '.agents/skills/feverkit-*/SKILL.md'
    return (f'{START}\n'
            '## FeverKit project workflow (managed block)\n'
            'Before major changes: inspect the repository, explain a plan, and choose a relevant specialist.\n'
            'Use tests and security checks; do not claim checks passed without running them.\n'
            f'Available project skills: `{where}`.\n'
            f'Active profiles: {", ".join(profiles)}.\n'
            'External tools in `.feverkit/selected-tools.md` are **recommendations**, not installed dependencies.\n'
            'Never execute remote install scripts or push/deploy without explicit approval.\n'
            'Prefer the smallest set of agents and dependencies that solves the task.\n'
            f'{END}\n')


def ensure_inside(project: Path, candidate: Path):
    """Reject symlinks that would redirect a project write outside its boundary."""
    if not candidate.resolve().is_relative_to(project.resolve()):
        raise ValueError(f'Refusing path outside project: {candidate}')


def managed_write(path: Path, content: str, backups: Path, force: bool):
    """Writes managed files; never destroys an unowned file without --force + backup."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding='utf-8')
        if existing == content:
            return 'unchanged'
        if not force:
            return 'skipped(existing file; add --force to back up and replace)'
        rel = path.relative_to(backups.parents[2])  # project root
        dest = backups / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
    path.write_text(content, encoding='utf-8')
    return 'written'


def managed_block_write(path: Path, insert: str, backups: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    original = path.read_text(encoding='utf-8') if path.exists() else ''
    if START in original or END in original:
        if original.count(START) != 1 or original.count(END) != 1 or original.index(START) > original.index(END):
            raise ValueError(f'Malformed FeverKit markers in {path}; refusing to modify')
        new = original[:original.index(START)] + insert + original[original.index(END) + len(END):].lstrip('\n')
    else:
        new = original.rstrip() + ('\n\n' if original.strip() else '') + insert
    if original == new:
        return 'unchanged'
    if path.exists():
        dest = backups / path.relative_to(backups.parents[2])
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
    path.write_text(new, encoding='utf-8')
    return 'updated'


def tools_md(ids: list[str]) -> str:
    _, all_tools = manifests()
    by_id = {t['id']: t for t in all_tools}
    lines = ['# FeverKit recommended external tools', '',
             '> No tools in this list are automatically installed by `apply`.',
             '> Audit upstream instructions, versions, permissions and licenses.', '',
             '| Tool | What it is for | Repo | Provenance |', '|---|---|---|---|']
    for ident in ids:
        t = by_id[ident]
        lines.append(f"| {t['name']} | {t['summary']} | [GitHub]({t['url']}) | {t['source']} |")
    return '\n'.join(lines) + '\n'


def install_plan(project: Path, plan: dict, execute: bool, force: bool):
    if str(project.resolve()) != plan.get('project'):
        raise ValueError('Plan belongs to a different project; regenerate it for this path')
    if plan.get('schema_version') != 1:
        raise ValueError('Unsupported plan schema')
    definitions, catalog = manifests()
    if not isinstance(plan.get('profiles'), dict) or any(p not in definitions for p in plan['profiles']):
        raise ValueError('Unknown profiles in plan')
    all_skills = {s for spec in definitions.values() for s in spec['skills']}
    all_agents = {a for spec in definitions.values() for a in spec['agents']}
    all_tools = {t['id'] for t in catalog}
    if any(x not in all_skills for x in plan.get('skills', [])) or \
       any(x not in all_agents for x in plan.get('agents', [])) or \
       any(x not in all_tools for x in plan.get('external_tools', [])):
        raise ValueError('Plan includes an unknown item; refusing to apply')
    jobs = []
    for skill in plan['skills']:
        source = ROOT / '.claude/skills' / skill / 'SKILL.md'
        for folder in ('.claude/skills', '.agents/skills'):
            jobs.append((source, project / folder / ('feverkit-' + skill) / 'SKILL.md'))
    for agent in plan['agents']:
        jobs.append((ROOT / '.claude/agents' / (agent+'.md'),
                     project / '.claude/agents' / ('feverkit-' + agent + '.md')))
    jobs.append((None, project / '.feverkit/selected-tools.md'))
    # Preflight before writing: reject symlink escape and malformed managed markers.
    for _, dst in jobs:
        ensure_inside(project, dst)
    for filename in ('CLAUDE.md', 'AGENTS.md'):
        dst = project / filename
        ensure_inside(project, dst)
        if dst.exists():
            prior = dst.read_text(encoding='utf-8')
            if START in prior or END in prior:
                if prior.count(START) != 1 or prior.count(END) != 1 or prior.index(START) > prior.index(END):
                    raise ValueError(f'Malformed FeverKit markers in {dst}; refusing to modify')
    if not execute:
        print(f'DRY RUN: {len(jobs)} managed files + CLAUDE.md + AGENTS.md')
        for _, dst in jobs:
            print('  PLAN', dst.relative_to(project))
        print('  PLAN CLAUDE.md (managed block, preserves existing text)')
        print('  PLAN AGENTS.md (managed block, preserves existing text)')
        print('Use `apply --plan ... --yes` after reviewing the plan.')
        return
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    backups = project / '.feverkit/backups' / stamp
    failures = []
    for src, dst in jobs:
        content = src.read_text(encoding='utf-8') if src is not None else tools_md(plan['external_tools'])
        result = managed_write(dst, content, backups, force=force)
        print(result, dst.relative_to(project))
        if result.startswith('skipped'):
            failures.append(str(dst.relative_to(project)))
    for filename in ('CLAUDE.md', 'AGENTS.md'):
        dst = project / filename
        status = managed_block_write(dst, block_for(project, plan['profiles'], filename), backups)
        print(status, filename)
    if failures:
        print('Some unowned files were preserved. Review and use --force to back them up and replace.', file=sys.stderr)
    print('Installed FeverKit Markdown skills and agents. No third-party code was executed.')


def command_vendor(project: Path, tool_ids: list[str], execute: bool):
    _, catalog = manifests()
    by_id = {t['id']: t for t in catalog}
    for ident in tool_ids:
        if ident not in by_id:
            raise ValueError(f'Unknown tool: {ident}')
    if execute and not shutil.which('git'):
        raise ValueError('Git is required to clone external repositories')
    for ident in tool_ids:
        t = by_id[ident]
        dst = project / '.feverkit/vendor' / ident
        ensure_inside(project, dst)
        print(('CLONE' if execute else 'PLAN'), t['url'], '→', dst)
        if not execute:
            continue
        if dst.exists():
            print('  SKIPPED: existing checkout, will not overwrite')
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        # Never execute install/setup scripts from upstream repos, even if cloned.
        subprocess.run(['git', '-c', 'protocol.file.allow=never', 'clone', '--depth=1',
                        '--', t['url'], str(dst)], check=True)
    if not execute:
        print('Nothing cloned. Add --execute to opt in. Cloning is not installing.')


def main(argv=None):
    parser = argparse.ArgumentParser(description='FeverKit selective AI dev setup; safe by default')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validate', help='Validate catalog and all profile templates')
    sub.add_parser('doctor', help='Check local prerequisites')
    c = sub.add_parser('catalog', help='List curated external projects')
    c.add_argument('--profile', help='Filter by profile name')
    p = sub.add_parser('plan', help='Detect a project and write an inspectable plan')
    p.add_argument('--project', default='.', help='Target project directory')
    p.add_argument('--profile', default='auto', help='auto or comma-separated profiles or all')
    p.add_argument('--out', default='.feverkit-plan.json', help='Path to output JSON (relative to project)')
    a = sub.add_parser('apply', help='Preview or install selected local Markdown skills')
    a.add_argument('--project', default='.')
    a.add_argument('--plan', default='.feverkit-plan.json')
    a.add_argument('--yes', action='store_true', help='Execute project-local file writes')
    a.add_argument('--force', action='store_true', help='Back up and replace pre-existing unmanaged FeverKit files')
    v = sub.add_parser('vendor', help='Optionally clone approved catalog GitHub repos only')
    v.add_argument('--project', default='.')
    v.add_argument('--tool', action='append', required=True, help='Catalog ID; can be repeated')
    v.add_argument('--execute', action='store_true', help='Actually git clone; never runs installer')
    args = parser.parse_args(argv)
    try:
        if args.command == 'validate':
            n, m = validate()
            print(f'OK: {n} profiles, {m} verified GitHub links, all skills and agents present')
        elif args.command == 'doctor':
            print('Python', sys.version.split()[0], '(>=3.10 required)')
            print('Git:', shutil.which('git') or 'not installed (required only for vendor)')
            print('Repo root:', ROOT)
        elif args.command == 'catalog':
            profiles, tools = manifests()
            if args.profile and args.profile not in profiles:
                raise ValueError('Unknown profile: '+args.profile)
            for t in tools:
                if not args.profile or args.profile in t['profiles']:
                    print(f"{t['id']:20} [{t['source']}] {t['url']}")
        elif args.command == 'plan':
            project = Path(args.project).resolve()
            if not project.is_dir():
                raise ValueError(f'Project directory does not exist: {project}')
            plan = make_plan(project, args.profile)
            dest = Path(args.out)
            if not dest.is_absolute():
                dest = project / dest
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(json.dumps(plan, indent=2)+'\n',encoding='utf-8')
            print('Plan:', dest)
            print('Profiles:', ', '.join(plan['profiles']))
            print(f"Skills: {len(plan['skills'])}; agents: {len(plan['agents'])}; external candidates: {len(plan['external_tools'])}")
            print('No dependencies installed. Review JSON, then run apply.')
        elif args.command == 'apply':
            project = Path(args.project).resolve()
            if not project.is_dir():
                raise ValueError('Project directory does not exist')
            f = Path(args.plan)
            if not f.is_absolute():
                f = project / f
            plan = read_json(f)
            install_plan(project, plan, args.yes, args.force)
        elif args.command == 'vendor':
            project = Path(args.project).resolve()
            if not project.is_dir():
                raise ValueError('Project directory does not exist')
            command_vendor(project, args.tool, args.execute)
    except (OSError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())
