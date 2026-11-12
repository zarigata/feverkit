# Daily Dev Drops — Route & Developer Tool Inventory

**Site:** https://devdailydrops.pages.dev/  
**Research date:** 2026-11-12  
**Goal:** collect developer tools, repos, guides, and subpages useful for multi-agent AI coding, local AI, app security, DevOps, SaaS, and game-development workflows.

> **Scope / honesty note:** This is an *evidence-based inventory*, not a claim that every route on the host was exhaustively crawled. The public `/repos` and `/plugins` pages were retrieved and all their listed GitHub destinations were inspected. The live homepage was read in a connected browser and supplied links to seven guides. Automated access to those guide bodies, plus `/launch` and `/unslop`, failed. No unseen contents or undiscovered routes have been invented. A companion crawler is provided to finish discovery from a normal browser environment.

## 1. Known routes and verification

Legend: **Read** = page body successfully retrieved; **Homepage link** = destination appears in the browser-rendered homepage, but its page body couldn't be read here; **User supplied** = path provided by user, not independently confirmed to load.

| Route | Link | Evidence/status | What is known |
|---|---|---|---|
| `/` | https://devdailydrops.pages.dev/ | **Read (live browser)** | Home feed; video/repo cards; AI tricks; Claude kit; guide links. |
| `/repos` | https://devdailydrops.pages.dev/repos | **Read** | Eleven individually linked GitHub repositories; one link to the five-plugin collection. |
| `/plugins` | https://devdailydrops.pages.dev/plugins | **Read** | Five named Claude Code tools with installation commands. |
| `/secure` | https://devdailydrops.pages.dev/secure | **Homepage link** | “Ship-safe checklist”: five security issues to check before launch and a prompt. Exact checklist inaccessible. |
| `/unmac` | https://devdailydrops.pages.dev/unmac | **Homepage link** | “Your Android app on iPhone”: seven-step guide without a Mac/iPhone; site claims $0. Details inaccessible. |
| `/hosting` | https://devdailydrops.pages.dev/hosting | **Homepage link** | Free hosting recommendations and three less-obvious options. Names inaccessible. |
| `/design` | https://devdailydrops.pages.dev/design | **Homepage link** | Five design plugins for Claude Code, including installation commands. Names inaccessible. |
| `/crew` | https://devdailydrops.pages.dev/crew | **Homepage link** | Five-agent crew with prompts/configuration. Exact agents inaccessible. |
| `/fix` | https://devdailydrops.pages.dev/fix | **Homepage link** | Six legal/compliance pitfalls for vibe-coded apps and fixes. Exact list inaccessible. |
| `/launch` | https://devdailydrops.pages.dev/launch | **User supplied; unverified** | Page contents could not be retrieved. Do not assume what the page contains. |
| `/unslop` | https://devdailydrops.pages.dev/unslop | **User supplied; unverified** | Page contents could not be retrieved. A separately verified GitHub project called `heydamir/unslop` is listed below, but its presence on this route is **not verified**. |

**Verified page-body coverage:** 3 routes (`/`, `/repos`, `/plugins`).  
**Additional linked guide destinations:** 7 routes.  
**User-supplied additional paths:** 2 routes.  
**Total catalogued paths:** 11; **total existence or content confirmation is NOT claimed**.

### Discoverability caveat

- Attempts to read `/robots.txt` and `/sitemap.xml` did not return usable content.
- Direct automated requests to `/secure`, `/unmac`, `/hosting`, `/design`, `/crew`, `/fix`, `/launch` and `/unslop` failed in this environment.
- The homepage's dynamically rendered links were visible in the browser tab and are more comprehensive than the simplified search-tool rendering.
- Other unlinked pages may exist. See the companion `crawl_daily_dev_drops.py` for a browser-based discovery approach.

## 2. GitHub repos listed on `/repos` — 11 verified links

All eleven names/links came from the page itself. Descriptions are based on its summaries and the destination repositories' public descriptions.

| Tool | GitHub source | Purpose | Relevance | Recommended use |
|---|---|---|---|---|
| **Copy4AI** | https://github.com/LeonKohli/copy4ai | Copy code files/folders, tree and diffs to an AI prompt in VS Code-compatible editors. | **High** | Useful for exporting targeted context to coding agents or sharing diagnostic snippets. Beware copying secrets. |
| **javascript-tetris** | https://github.com/jakesgordon/javascript-tetris | Small browser Tetris game in JavaScript. | Low | Reference/demo project for testing web/game controls; not infrastructure. |
| **ai-job-search** | https://github.com/ai-job-search-dev/ai-job-search | Local Claude Code-assisted workflow for evaluating job ads, tailoring CVs, cover letters and interview prep. | **High** | Adapt to engineering/AI job search; review each application before submission. |
| **Boop** | https://github.com/chrisgreg/boop | Self-hosted notification inbox for developer app events. | **High** | Send alerts from deployment jobs, AI agents and server monitors. |
| **AutoClip** | https://github.com/artbyjazi/autoclip | Offline-first AI clipper for long video to captioned vertical clips; Whisper/Ollama support. | Medium–High | Repurpose demo videos for software marketing. |
| **jev-ultrafast** | https://github.com/browser-use/jev-ultrafast | Fast browser/web automation agent. | **High** | Evaluate for autonomous research and browser task execution with sandboxing/permissions. |
| **Laya** | https://github.com/NandhaKishorM/laya | Fast text classification/decisions/routing (typed choice, score, yes/no), 100+ languages. | **High** | Low-latency task classification and routing before larger LLM calls. |
| **OpenStock** | https://github.com/Open-Dev-Society/OpenStock | Open-source live market tracking, charts and alerts. | Medium | Market/portfolio dashboard reference. Verify quote-feed costs and licensing. |
| **Plexo** | https://github.com/anmolkapil/plexo | Download acceleration across multiple network connections. | Medium | Large model or artifact downloads when multiple connections are available. |
| **Stemkit** | https://github.com/danielravina/stemkit | Split songs/audio into separate stems. | Medium | Audio experiments. Respect licensing of music inputs/outputs. |
| **WeKnora** | https://github.com/Tencent/WeKnora | Open-source knowledge/RAG platform for searchable documents, agents and auto-updating wiki. | **Very high** | Knowledge backend for a self-hosted assistant or documentation-aware coding team. |

**Notes:** The site previously linked `MadsLorentzen/ai-job-search`; the link currently redirects to `ai-job-search-dev/ai-job-search`. Canonical current destination is shown above.

## 3. Five plugins listed on `/plugins` — 5 verified links

| Tool | GitHub source | Function | Relevance |
|---|---|---|---|
| **OmniRoute** | https://github.com/cheaper-inference/OmniRoute | Multi-provider AI gateway, model routing and failover for coding clients. Former source link redirects to this repository. | **Very high** |
| **Ponytail** | https://github.com/DietrichGebert/ponytail | Skill/plugin encouraging minimal, maintainable implementations rather than excessive code. | High |
| **Graphify** | https://github.com/Graphify-Labs/graphify | Local deterministic AST-based codebase knowledge graph for context-aware coding agents. | **Very high** |
| **Agent Skills** | https://github.com/addyosmani/agent-skills | Engineering skill collection for planning, implementation, testing and reviews. | **Very high** |
| **claude-mem** | https://github.com/thedotmack/claude-mem | Session memory/context capture and retrieval across agent sessions. | **Very high** |

### Commands displayed on the site's `/plugins` page

The snippets below are **transcribed from the source page**, not executed or security-audited. Verify exact current installation instructions in each GitHub README before use.

```bash
# OmniRoute
npm install -g omniroute

# Ponytail: run these inside Claude Code (slash commands, NOT shell commands)
# /plugin marketplace add DietrichGebert/ponytail
# /plugin install ponytail@ponytail

# Graphify
uv tool install graphifyy
graphify install

# Agent Skills
npx skills add addyosmani/agent-skills

# claude-mem
npx claude-mem install
```

**Warning:** Plugin compatibility and permissions can change; never run arbitrary third-party installers against production secrets without reviewing their code and permissions first.

## 4. Separately verified tool possibly related to `/unslop`

**Unslop** — https://github.com/heydamir/unslop  
**Provenance:** Independent public GitHub verification, **not** retrieved from the site's `/unslop` page. This is a Claude Code/Codex/Antigravity skill that audits generic AI-created interfaces, proposes a visual direction, and works through spacing, typography, palette, copy, layout and UI polish.

**Why useful:** Useful for making developer-created SaaS dashboards and company websites feel intentionally designed. It does not replace security, performance, accessibility or usability testing. The GitHub repository lists installation for Claude Code using a copy of `skills/unslop` into `~/.claude/skills/` and invocation via `/unslop`.

**Do not conflate:** This repo is a relevant candidate, not proof that the Daily Dev Drops `/unslop` route links to it.

## 5. Additional homepage content (verified in browser)

These resources appeared *inside the homepage*, not as separate verified routes:

1. **Give Claude a memory:** Use a project `CLAUDE.md`, or `~/.claude/CLAUDE.md` for cross-project instructions. Define coding rules, project shape and guardrails.
2. **Teach Claude a job once:** Define a `.claude/skills/<skill-name>/SKILL.md` with a description and repeatable steps.
3. **Understand any repo in 2 minutes:** Repo cards have a “Use with Claude” helper prompt that asks for a plain-language explanation, prerequisites and staged install steps.
4. **Run AI offline:** The site's example uses Ollama and `ollama run llama3.2`.
5. **CLAUDE.md starter:** Home includes a simple project skeleton with project description, collaboration preferences and locations of main code/tests.
6. **Skill: repo-scout:** Home includes a skill template instructing an agent to inspect the README, update date, issues, license, prerequisites, installation steps and conclude “worth trying?”
7. **Prompt: explain like I'm new:** A reusable prompt requesting accessible technical explanation, one analogy, and concrete action.

### Quick `repo-scout` template adapted from the site's homepage

```markdown
---
name: repo-scout
description: Use when evaluating a GitHub repository before installing it.
---
1. Read the README and explain what it does and for whom.
2. Check last updates, unresolved issues, license, maintenance and security risks.
3. List software, RAM/VRAM, services and API keys needed.
4. Recommend a minimally invasive trial in a sandbox.
5. Give a one-line verdict: install / investigate / avoid, and why.
```

## 6. Best-fit integration priorities

### Priority A — Multi-agent coding CLI and local AI

1. **OmniRoute** — Use for provider abstraction and failover across cloud/local endpoints; do not assume every provider exposes exactly the same API/tool-call support.
2. **Graphify** — Build structural knowledge about large repos to reduce repeated searches.
3. **claude-mem** — Persist useful task outcomes and decisions; verify stored data and retention policies.
4. **Agent Skills** — Establish repeatable testing, review, security and release procedures.
5. **Ponytail** — Reduce overengineering and token waste.
6. **Laya** — Explore a lightweight decision/router stage before invoking more expensive models.
7. **jev-ultrafast** — Test only within an isolated browser account with safe approvals.

### Priority B — SaaS platform & production operations

1. **WeKnora** — Document knowledge and RAG for support, developer docs and user-facing explanations.
2. **Boop** — Push operational alerts for Docker services, agents, webhooks and deploy pipelines.
3. **Unslop (independent project)** — Audit the look and feel of dashboards and landing pages.
4. **`/secure`, `/fix`, `/launch`** — High-interest guides, but details are **not retrieved**. Must inspect before acting on specific claims.
5. **`/hosting`** — Potential options, but confirm free quotas, region and data handling yourself.

### Priority C — Dev marketing, demos, career and experimentation

1. **AutoClip** — Turn product demos into short vertical clips.
2. **Copy4AI** — Transfer the minimum code required for a precise review.
3. **ai-job-search** — Organize applications with human review.
4. **javascript-tetris** — Lightweight test fixture for browser/game automation.
5. **OpenStock**, **Plexo**, **Stemkit** — Niche utilities depending on project.

## 7. Suggested architecture (integration idea, not claimed site content)

```text
User request
     │
     ▼
Laya / routing logic ────────────────┐
     │                              │
     ▼                              ▼
Multi-agent controller       OmniRoute model gateway
     │                              │
     ├── Graphify: code map         ├── cloud APIs
     ├── claude-mem: memory         └── local LLM servers
     ├── Agent Skills: quality
     ├── Ponytail: simplicity
     ├── jev-ultrafast: browser actions (sandbox)
     └── WeKnora: docs/RAG
                   │
                   ▼
           CI tests + security scan
                   │
                   ▼
             Boop alerts
```

Keep secrets server-side; enforce per-agent permission scopes, prompt-injection defenses, external-action approvals, and audit logs.

## 8. Coverage checklist for a truly exhaustive crawl

- [x] Read homepage in browser and enumerate its visible guide links.
- [x] Read `/repos`; verify the eleven GitHub destination URLs.
- [x] Read `/plugins`; verify the five GitHub destination URLs and collect installation snippets.
- [x] Record user-provided `/launch` and `/unslop` paths.
- [ ] Open each guide page with a navigable browser and extract its complete contents.
- [ ] Test `/launch` and `/unslop` in the browser; confirm actual content and all outbound links.
- [ ] Parse site JavaScript chunks for non-linked routes; distinguish route candidates from asset paths.
- [ ] Retrieve/parse any sitemap and `robots.txt` if present.
- [ ] Crawl internal anchors breadth-first until no unseen internal paths remain.
- [ ] Deduplicate external GitHub repositories and verify all additional links.
- [ ] Re-run periodically to capture newly published pages.

## 9. Provenance and source links

Primary site:
- https://devdailydrops.pages.dev/
- https://devdailydrops.pages.dev/repos
- https://devdailydrops.pages.dev/plugins

Additional routes: links above were read from the live homepage except the two user-supplied paths `/launch` and `/unslop`.

Independent GitHub verification:
- All 16 linked repos in sections 2 and 3.
- https://github.com/heydamir/unslop (not site-confirmed).

**Caution:** GitHub owners, install commands, features and security properties can change. Verify upstream before deploying, especially with account/API permissions.
