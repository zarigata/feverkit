---
name: feverkit-repo-scout
description: Evaluate third-party repositories before integration.
---

# Repo Scout

Use this skill when the task matches its purpose. Adapt to the project; it is guidance, not executable code.

1. Read the upstream README and license; do not rely on star count alone.
2. Inspect maintenance, releases, security policy, dependencies, permissions, supported platforms and known issues.
3. Check compatibility with the target runtime, editor and model provider.
4. Assess supply-chain risk: install hooks, GitHub Actions, token access, telemetry and network calls.
5. Distinguish **candidate** from **verified working integration**. Favor a sandbox proof-of-concept.
6. Return: summary, suitability, security notes, resource requirements, alternatives, and adopt / trial / avoid recommendation.
7. Never run `curl | sh`, an arbitrary `npx`, or privilege escalation as part of evaluation.

**Deliverable:** short evidence-based findings, changed files (if any), tests executed, risks, and next steps.
