# OpenGame coding integration

Use the FeverKit game profile to install the original integration guidance:

```bash
python3 tools/feverkit.py plan --project /path/to/game --profile game
```

Review the plan and follow the README apply workflow. This does not install OpenGame or modify MCP configuration.

## Upstream setup (manual, opt-in)

- Repository: https://github.com/nexu-io/opengame
- Setup guide: https://github.com/nexu-io/opengame/blob/main/docs/opengame-setup.md
- Requirements documented upstream: Node.js 22.18+, Git, Git LFS and npm; Chrome for playtests.
- Review and pin the code, dependencies, upstream skills and assets. After approval, follow the upstream setup and configure local stdio MCP with absolute paths and separate MOTION_DATA_DIR. Confirm the server with Claude Code /mcp; keep providers and secrets out of source control.

## Prompt for a coding agent

> Read feverkit-opengame-development and game-testing. Inspect my existing game and establish a baseline. Evaluate OpenGame's upstream design references and playtesting tools. Keep my existing engine and build pipeline intact. If I approve setup, create an isolated prototype and demonstrate a measurable improvement in controls, camera, gameplay, UI, animation or performance. Validate, simulate and playtest with evidence, and continue with native-engine tests and manual review. Do not publish or spend money without approval.

## Decision matrix

| Project | Recommended use |
|---|---|
| New browser game | Isolated OpenGame prototype and automated QA |
| Existing Godot, Unity or Unreal project | Design references, independent prototypes; native engine remains authoritative |
| MMORPG or open-world game | Prototype individual systems; native performance, networking and persistence tests remain required |
| Game promotion | Optional real gameplay capture, cover or trailer with explicit approval |

Verify actual tools and licenses at the reviewed revision. Headless simulation does not prove game feel or scalability. OpenGame is a new upstream project and its advertised quality is not independently demonstrated by FeverKit.
