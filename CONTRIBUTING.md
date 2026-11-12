# Contributing to FeverKit

Before proposing a new project, confirm its canonical public GitHub URL, name, purpose, license, maintenance, platform compatibility and privacy/security considerations. Include an exact provenance category: `ddd-repos`, `ddd-plugins`, `independent` or `curated`. Never claim an inaccessible Daily Dev Drops route confirms a specific tool.

New profiles must declare a useful purpose and reference existing (or newly authored) skill/agent files. Avoid duplicative skills and overly broad automatic setup. Keep installer actions deterministic and dry-run first.

Test every change:

```bash
python3 tools/feverkit.py validate
python3 -m unittest discover -s tests -v
```

No secrets, vendored third-party code or GPL/AGPL code should be silently mixed into the original MIT-licensed CLI. Linked projects retain their own licenses.
