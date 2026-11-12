# Prompt pack — one URL, selected tools

## Simple prompt for Claude Code

> Read `START_HERE.md` from this FeverKit GitHub repository: `<URL>`. Inspect my current project and recommend which profiles apply. Use FeverKit to create a plan, then show what would be written or installed. Only after I approve, apply its project-local Markdown agents and skills. External tools require separate review and permission. Preserve existing code and verify results.

## More autonomous (still approval-based)

> You are the lead of a small engineering team. Use `<URL>` as a tool-selection catalog and skill source. Inspect the repository at your current working directory and select appropriate FeverKit profiles (core + targeted specializations). Create an implementation plan with milestones, test strategy and rollback. After local-file approval, apply only relevant FeverKit skills and agents. For outside dependencies, evaluate license, maintenance, compatibility and security; show installation steps and request specific approval before executing. Delegate to specialists only when their work can be tested. Preserve all existing features, do not invent test results, and report changed files at the end.

## Examples

- **Local Hermes coding cluster:** choose `core,ai-agents,devops`. Consider routing, context, memory and evaluation tools; avoid automatically activating every agent framework.
- **School SaaS:** choose `core,fullstack,saas,ai-agents,devops`. Prioritize auth, tenant boundaries, billing integrity and production-like tests.
- **Godot/Rust game:** choose `core,game,devops`. Prioritize physics/reproducible visual testing before adding plugins.
- **ESP32 / robot:** choose `core,robotics`. Keep hardware control safe and separated from LLM outputs.

## If only a browser URL is available

An agent should first read the repo and ask for permission to clone it locally or provide the install plan in chat. A bare URL is **not** permission to execute code or install tools.
