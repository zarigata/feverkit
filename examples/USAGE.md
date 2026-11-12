# Practical examples

## Project-aware workflow

```bash
python3 tools/feverkit.py doctor
python3 tools/feverkit.py plan --project ~/code/my-app --profile auto
# Inspect ~/code/my-app/.feverkit-plan.json
python3 tools/feverkit.py apply --project ~/code/my-app
# If the dry run looks good:
python3 tools/feverkit.py apply --project ~/code/my-app --yes
```

The generated project files live under `.claude/`, `.agents/`, `.feverkit/` and the managed blocks in `CLAUDE.md` and `AGENTS.md`. Nothing here configures real API keys or servers.

## Force selected profiles

```bash
python3 tools/feverkit.py plan --project ~/code/my-llm-agent --profile ai-agents,devops
python3 tools/feverkit.py plan --project ~/code/my-godot-game --profile game
python3 tools/feverkit.py plan --project ~/code/my-saas --profile fullstack,saas,devops
python3 tools/feverkit.py plan --project ~/code/my-robot --profile robotics
```

## Inspect a specific upstream tool without installing it

```bash
python3 tools/feverkit.py catalog --profile ai-agents
python3 tools/feverkit.py vendor --project ~/code/my-llm-agent --tool graphify
# With explicit review and approval:
python3 tools/feverkit.py vendor --project ~/code/my-llm-agent --tool graphify --execute
```

`vendor` does **not** install any Python, Node, Claude or Docker packages; it only clones the selected repository. Check `docs/integration-map.md` for how to evaluate a real integration.
