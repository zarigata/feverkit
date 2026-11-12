# Working on the FeverKit repository

FeverKit is a curated and independently maintained toolkit **not a mirror of upstream packages**. Maintain the contract:

1. Safe by default: `plan` and `apply` dry runs never install code. `apply --yes` may write only local Markdown files and managed instruction blocks.
2. Preserve existing user files and make backups before explicitly requested replacements.
3. Never imply that GitHub repo creation or upstream installation is available when it is not.
4. Keep `manifest/tools.json` provenance accurate (`ddd-repos`, `ddd-plugins`, `independent`, `curated`).
5. Every tool entry needs a real repository URL and a narrowly stated role.
6. New skills require a `SKILL.md` with frontmatter and a profile mapping; new agents need corresponding `.claude/agents/<name>.md`.
7. Run `python3 tools/feverkit.py validate` and `python3 -m unittest discover -s tests -v` after changes.
8. Document compatibility and never execute untrusted third-party installers in tests.
9. Do not invent the content of Daily Dev Drops routes whose bodies were inaccessible.
