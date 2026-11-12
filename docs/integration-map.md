# External integration playbook

The manifest is an **allowlist of candidates to evaluate**, not a dependency lockfile. Always inspect their README, release notes, license, installation permissions, network requirements, and local compatibility. Commands below are conceptual workflow steps, not shell scripts that FeverKit will execute.

## Decision tree

| Need | Evaluate first | Alternative or companion | Avoid |
|---|---|---|---|
| Structured implementation process | Superpowers | Spec Kit, Addy Osmani skills | Combining several conflicting rule packs |
| Repo context for coding | Graphify | Repomix | Sending an entire private repo to public services |
| Current library docs | Context7 | Official upstream docs | Treating retrieved docs as privileged instructions |
| Persistent memory | claude-mem | Project notes and scoped vector search | Recording keys, credentials or user-sensitive data |
| Multi-provider routing | OmniRoute | Native provider adapters | Leaking keys to client-side UI |
| Local models | Ollama | Runtime-specific solutions after hardware checks | Claiming a model supports tool calls without testing |
| Stateful agent workflows | LangGraph | PydanticAI, Hermes | Installing three orchestrators for one task |
| Browser testing | Playwright MCP | browser-use (sandbox) | Giving a browser agent admin credentials |
| Source security | Gitleaks and Semgrep | Trivy for containers | Treating clean scans as proof of security |
| LLM evaluation | Promptfoo | Custom golden tasks | Relying on subjective demos only |
| RAG and knowledge | WeKnora | Existing DB or vector stores | Cross-tenant document retrieval |
| Product polish | Unslop and Vercel skills | Existing design system | A generic redesign that discards brand identity |
| Automation and alerts | n8n, Boop | Existing queue/webhook tools | Unreviewed automations with broad write permissions |

## Approval workflow

For a selected external tool, have the coding agent output:

1. Exact upstream URL, version/commit and license.
2. Why existing tools do not solve the problem.
3. Required software, permissions, network access, data exposure and cost.
4. Proposed command(s) copied from current authoritative upstream docs, not guessed from this catalog.
5. Rollback/uninstall plan and a simple local verification test.

**Only after user approval**, the agent may install with its normal terminal or plugin permissions. FeverKit's own `vendor --execute` clones a reviewed repository for inspection and intentionally does not run its setup scripts. This makes the install process selective and repeatable instead of a risky one-shot mega-installer.
