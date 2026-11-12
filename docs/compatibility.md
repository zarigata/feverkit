# AI agent compatibility

| Agent/tool | Primary integration | Notes |
|---|---|---|
| Claude Code | `CLAUDE.md`, `.claude/skills/`, `.claude/agents/` | Bundled agents are written for Claude; confirm active version and configuration |
| OpenAI Codex | `AGENTS.md`, `.agents/skills/` | Agent definitions in `.claude/agents` are not automatically portable subagents |
| OpenCode | `AGENTS.md` and portable skill instructions | Read project documentation and adapt to OpenCode's native config format |
| Cursor | `AGENTS.md` / project rules and manual skill import | Do not assume Claude-specific plugin commands work |
| Hermes Agent | Markdown instructions and explicit custom integration | May require manual tool and memory integration |

This repository does **not** claim automatic plugin installation across every agent platform. `SKILL.md` portability is helpful, but MCP, runtime permissions, remote credentials and agent metadata differ.
