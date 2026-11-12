---
name: feverkit-plan-first
description: Design a bounded plan before making broad changes.
---

# Plan First

Use this skill when the task matches its purpose. Adapt to the project; it is guidance, not executable code.

1. Define goal, known constraints, non-goals, success criteria and rollback.
2. Inventory existing architecture; **do not rebuild working features**.
3. Choose the minimum dependencies and agents; document why each is necessary.
4. For changes touching public APIs, storage or credentials, propose migration and backwards-compatibility checks.
5. Break implementation into small auditable phases with tests and checkpoints.
6. Obtain approval before installing third-party code, changing infrastructure or deploying.
7. Keep the plan in the project's existing issue or document convention.

**Deliverable:** short evidence-based findings, changed files (if any), tests executed, risks, and next steps.
