# ⚡ FeverKit — AI Developer Arsenal

**A curated, project-aware tool catalog + portable agent instructions + a safe setup CLI.**

> **From one repository URL to a tailored AI coding environment.** FeverKit helps Claude Code, Codex, OpenCode, and other coding agents *plan* what a project needs and install a small set of portable, local Markdown skills. Heavy third-party tools remain opt-in and independently reviewed.

**44 reviewed GitHub repository destinations · 9 profiles · 14 original skills · 13 original Claude subagents · Python standard library only.**

Created by the FeverDream ecosystem · [feverdream.dev](https://feverdream.dev/)  
Research inspiration: [Daily Dev Drops](https://devdailydrops.pages.dev/) by [@hayderdotdev](https://www.instagram.com/hayderdotdev/). This is an **independent** project, not endorsed by those upstream maintainers.

## Hand one URL to Claude Code

When this repository has been published, give Claude Code its GitHub URL and this prompt:

> Read the entire FeverKit repository at `https://github.com/zarigata/feverkit` starting with `START_HERE.md`. Inspect **my current project** and select only relevant FeverKit profiles. First produce a plan; then, if I approve local file writes, install the appropriate project-scoped Markdown skills and agents. Show me any external repositories and their security/compatibility implications; never run upstream installers, change my global environment, or deploy without my approval. Run the relevant tests and report what really happened.

This repository is published at **`zarigata/feverkit`**.

If Claude Code can read your local repository directly, the prompts in `START_HERE.md` work without network access.

## Quick start

```bash
# After publishing this repository:
git clone https://github.com/zarigata/feverkit.git
cd feverkit
python3 tools/feverkit.py validate
python3 tools/feverkit.py doctor

# From any directory, plan against a separate project:
python3 tools/feverkit.py plan --project /path/to/my-app --profile auto
python3 tools/feverkit.py apply --project /path/to/my-app --plan .feverkit-plan.json

# Review the proposed file changes; then explicitly approve them:
python3 tools/feverkit.py apply --project /path/to/my-app --plan .feverkit-plan.json --yes
```

`apply` **only copies FeverKit's own Markdown skills and agent definitions** and adds a clearly marked, replaceable block to existing `CLAUDE.md` and `AGENTS.md` files. It never automatically installs external software or executes third-party setup commands. Existing unowned agent files are preserved unless you explicitly request `--force` (which makes backups).

## Pick a profile

| Profile | Good for | Examples |
|---|---|---|
| `core` | Every repository | Planning, reviews, secrets, repo exploration |
| `fullstack` | React, Node.js, Python, APIs | Frontend quality, API contracts, Playwright |
| `ai-agents` | Multi-agent systems, MCP, RAG, local AI | Model routing, agent evaluation, memory, Ollama |
| `game` | Godot, Unity, Rust games | Physics, rendering, controls, game testing |
| `devops` | Docker, operations | Deploy safety, monitoring, vulnerability scans |
| `saas` | Multi-tenant SaaS | Billing, tenant isolation, auth, privacy |
| `robotics` | ESP32, Arduino, motion control | Hardware safety, watchdogs, HIL testing |
| `marketing` | Product launches | Docs, developer relations, short-form video |
| `career` | Developer job searches | Posting verification, truthful CV tailoring |

For a project-aware starter plan use `--profile auto`; detection is intentionally conservative. For a deliberate stack, specify multiple: `--profile fullstack,ai-agents,saas` (core is always included). `--profile all` is for exploration, not a recommended routine installation.

## How it works

```text
Your project ───► FeverKit detector ───► JSON plan (review)
     │                   │                     │
     │                   └── language/engine    ▼
     │                       Docker/MCP         selected profiles
     │                                             │
     │                              approval ──────┤
     ▼                                             ▼
existing files ◄────── additive CLAUDE.md / AGENTS.md
                             + .claude/agents/feverkit-*
                             + .claude/skills/feverkit-*
                             + .agents/skills/feverkit-*
                             + .feverkit/selected-tools.md
                             (no remote installer executed)
```

### What is actually installed?

**Bundled:** agent/skill Markdown files, project-level instruction blocks, and a tool-selection report. **Optional:** `vendor` can clone a specific catalog repo into `.feverkit/vendor/` after approval; cloning does **not** install or activate it. **Manual/integration:** Claude plugins, MCP servers, browser tools, container services, local LLMs and third-party dependencies require their own audited setup.

```bash
python3 tools/feverkit.py catalog --profile ai-agents
python3 tools/feverkit.py vendor --project /path/to/my-app --tool graphify
# Review; this command only downloads the chosen upstream repository:
python3 tools/feverkit.py vendor --project /path/to/my-app --tool graphify --execute
```

## Repository layout

```text
README.md                        Start here, workflow and profiles
START_HERE.md                    Instructions specifically for coding agents
CLAUDE.md / AGENTS.md           Instructions for working on FeverKit itself
manifest/
  tools.json                     Machine-readable repository catalog
  profiles.json                  Skills and agents selected per profile
  site-routes.json               Daily Dev Drops route status with caveats
.claude/agents/                 13 original specialist subagents
.claude/skills/                 14 original reusable project skills
 tools/feverkit.py               Stdlib-only CLI: plan/apply/catalog/vendor
 tools/crawl_daily_dev_drops.py  Optional web-browser research crawler
 docs/
  catalog.md                     Searchable descriptions and recommendations
  DAILY_DEV_DROPS_INVENTORY.md   Original research inventory and caveats
  agent-prompt.md                One-link prompts for coding agents
  recipes/                       Example stacks and decision guides
  security.md                    Trust, backups, install safety
  publishing.md                  How to publish the GitHub repository
 tests/                          Offline automated tests
 .github/workflows/ci.yml        Validation and smoke tests on every push/PR
```

## Best starter integrations (not auto-installed)

- **Coding method:** [Superpowers](https://github.com/obra/superpowers), [Spec Kit](https://github.com/github/spec-kit), [Ponytail](https://github.com/DietrichGebert/ponytail)
- **Context & memory:** [Graphify](https://github.com/Graphify-Labs/graphify), [Context7](https://github.com/upstash/context7), [claude-mem](https://github.com/thedotmack/claude-mem), [Repomix](https://github.com/yamadashy/repomix)
- **AI systems:** [OmniRoute](https://github.com/cheaper-inference/OmniRoute), [Hermes Agent](https://github.com/NousResearch/hermes-agent), [LangGraph](https://github.com/langchain-ai/langgraph), [Ollama](https://github.com/ollama/ollama)
- **Testing & security:** [Playwright MCP](https://github.com/microsoft/playwright-mcp), [Semgrep](https://github.com/semgrep/semgrep), [Trivy](https://github.com/aquasecurity/trivy), [Gitleaks](https://github.com/gitleaks/gitleaks), [Promptfoo](https://github.com/promptfoo/promptfoo)
- **Knowledge & automation:** [WeKnora](https://github.com/Tencent/WeKnora), [n8n](https://github.com/n8n-io/n8n), [GitHub MCP](https://github.com/github/github-mcp-server)
- **Interface polish:** [Unslop](https://github.com/heydamir/unslop), [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)

See [the full catalog](docs/catalog.md), [recipes](docs/recipes/), [trust model](docs/security.md), and [the original Daily Dev Drops research](docs/DAILY_DEV_DROPS_INVENTORY.md).

## Scope and limitations

- This repository indexes third-party projects **by reference**; it does not copy or bundle their code, licenses, or tools.
- Daily Dev Drops `/launch`, `/unslop`, and several guide bodies could not be independently retrieved. Their presence in the route inventory is **not** evidence of their contents. No unknown pages are fabricated.
- Repo links were verified to resolve on 2026-11-12. APIs, versions, licensing, compatibility and upstream install commands can change; audit before use.
- The CLI cannot infer your stack perfectly, safely automate every third-party installer, grant cloud credentials, or guarantee agent compliance. Review the plan.
- **License:** MIT applies to the original FeverKit materials and CLI, **not** to linked third-party repositories.

Maintained as a practical engineering starting point, not as a promise that 44 tools must all be installed.
