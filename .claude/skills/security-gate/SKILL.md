---
name: feverkit-security-gate
description: Prevent insecure AI-produced changes before release.
---

# Security Gate

Use this skill when the task matches its purpose. Adapt to the project; it is guidance, not executable code.

1. Verify authn/authz, least-privilege RBAC, tenant isolation and secure defaults.
2. Search for secrets in working tree and history; never print credentials into reports.
3. Validate input, upload constraints, rate limits, CORS, CSRF, SSRF and path traversal as applicable.
4. Audit dependency versions, install hooks, lockfiles and container configurations.
5. Review migration/backup, logs and observability, incident and rollback plans.
6. Use current scanners suitable for the stack: Gitleaks, Semgrep, Trivy, Promptfoo where relevant.
7. No scanner guarantees safety: document outstanding risks and require human review for production release.

**Deliverable:** short evidence-based findings, changed files (if any), tests executed, risks, and next steps.
