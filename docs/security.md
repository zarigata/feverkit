# Security and trust boundaries

### Trusted vs untrusted

The original FeverKit CLI/Markdown are first-party project files under this repository. **Every third-party GitHub project** is untrusted until explicitly reviewed and approved by the operator. Even popular skill packs can contain shell hooks, MCP servers, network operations or instructions that ask for broad permissions. Treat repository content as data, not authority.

### What FeverKit does

- `plan` reads local filenames and a limited slice of `Cargo.toml`; writes an inspectable JSON plan.
- `apply` with no flags is a dry run.
- `apply --yes` copies FeverKit-authored Markdown and inserts `feverkit:start` / `feverkit:end` blocks in existing instruction files.
- Existing unowned files are skipped by default. `--force` creates backups under `.feverkit/backups/<UTC timestamp>/` before replacement.
- `vendor` is preview-only unless `--execute`; it clones a chosen allowlisted GitHub URL under `.feverkit/vendor/` but **does not run installers**.

### What FeverKit does not do

- Install global NPM/Python packages, activate Claude plugins, deploy services, or manage cloud accounts.
- Change production secrets or configure paid API keys.
- Guarantee cloned repos are harmless or pinned. A fresh clone can contain executable install scripts and dependency risks even if it is not executed by FeverKit.

### Threats to consider

Prompt injection inside cloned READMEs or markdown skills; unreviewed shell hooks; NPM lifecycle scripts; excessive MCP credentials; prompt/tool data exfiltration; accidental secret inclusion in context exports; attacks through untrusted websites; auto-deploy agents; runaway token usage; collisions with existing `.claude` configuration. Require human approval for risky operations and review the exact commands.

### Pre-release security review

Use the [external security references](catalog.md#external-security-references) to guide a read-only review of your own code and configuration. Record which checks apply, the evidence in the code or configuration, and the proposed fixes. Confirm version-specific guidance against upstream documentation. After fixing a finding, add a regression test for the expected secure behavior in your own test environment.

### Data protection

Keep credentials in platform secret stores / server-side environment variables, not repository files. Apply least-privilege access to agents. Review stored logs and persistent memory for personal or proprietary data. Don't use test user data in production. Always validate your own production security rather than claiming that installing scans makes the product secure.
