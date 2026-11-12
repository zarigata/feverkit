---
name: feverkit-saas-production
description: Review a real SaaS for operational and privacy readiness.
---

# Saas Production

Use this skill when the task matches its purpose. Adapt to the project; it is guidance, not executable code.

1. Map user roles, organizations/tenants, billing events and personally identifiable data.
2. Design isolation tests and per-resource permission checks; no trust in client-supplied tenant IDs.
3. Verify authentication, payments, webhook verification, refunds and idempotent event handling.
4. Add retention, deletion, backup and observability practices appropriate to jurisdiction and product.
5. Replace any production mock data with genuine configured persistence; test migrations.
6. Do not assert legal compliance without competent review; document unanswered issues.

**Deliverable:** short evidence-based findings, changed files (if any), tests executed, risks, and next steps.
