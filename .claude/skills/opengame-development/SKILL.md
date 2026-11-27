---
name: feverkit-opengame-development
description: Evaluate and use OpenGame's agent skills, local Studio, and MCP for HTML5/Three.js game prototyping, game-design references and verified playtesting without disrupting existing engines.
---

# OpenGame development

Upstream: https://github.com/nexu-io/opengame (Apache-2.0 repository; independently check asset and dependency licenses). This is original FeverKit integration guidance, not the upstream skill.

1. Inspect the current project and its engine, target devices, controls, architecture, existing tests, assets and performance budgets. Choose a narrow playable milestone and measurable acceptance criteria.
2. For HTML5/Canvas/Three.js prototypes, consider OpenGame Studio and the upstream opengame and openmotion-game skills. For Godot, Unity, Unreal, native or multiplayer projects, use its design handbooks and isolated prototypes as references; retain the current engine, networking and asset pipeline unless the owner explicitly approves a migration.
3. Before installation, review the upstream setup at https://github.com/nexu-io/opengame/blob/main/docs/opengame-setup.md, pin a reviewed revision, inspect package scripts, lockfile, MCP entry point, permissions and asset downloads. Check Node.js 22.18+, Git, Git LFS, npm, Chrome and available disk. Never execute a remote installer, enable a plugin or start an unreviewed MCP server automatically.
4. With explicit setup approval, install the reviewed upstream skills and connect the local stdio MCP following the upstream guide. Use a project-scoped configuration, absolute paths, a separate MOTION_DATA_DIR, minimal privileges and no secrets in git. In Claude Code check /mcp; inspect the actual tool schemas and confirm connectivity before writing files. Keep external model calls and spending disabled unless approved.
5. In an isolated owned prototype, use create/get/read_file/write_files/update_meta as appropriate in the openmotion_game_* namespace. Make original assets and gameplay; check third-party rights, no unlicensed copies of commercial games. Preserve real user work and avoid arbitrary writes outside the prototype.
6. Run validate, simulate and playtest if available. Verify actual input, camera, collision, controls, frame pacing, responsive UI, console and loading behavior. Capture real screenshots or gameplay; do manual playtesting for enjoyment and feel. Use existing engine-native tests and independent review for production games, including server-authoritative multiplayer, synchronization, persistence, load and latency tests where relevant. Never equate a browser smoke test with production readiness.
7. Iterate on failures, keep evidence and compare against agreed budgets. Do not declare AAA quality, multiplayer correctness, or production readiness without evidence. Cover/trailer generation is optional; publishing (including local catalog, public share or store upload) requires explicit approval.

Deliver a scope decision, changed files, test results and screenshots, performance observations, rights/provenance, blockers and next milestone. If Studio or MCP cannot run, report that and continue with existing engine-native tools and upstream design references instead.
