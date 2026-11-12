# Recipe: production SaaS / education platform

Profiles: `core,fullstack,saas,ai-agents,devops`

1. Audit authorization and tenant boundaries before adding agents.
2. Build real database-backed CRUD, migration and audit logging; reject fake production data.
3. Implement validated payment webhooks and idempotent billing state updates.
4. Use Playwright MCP for UI flows on isolated test accounts, Semgrep/Gitleaks/Trivy for targeted checks.
5. Use WeKnora for RAG only when document permissions are enforced throughout retrieval.
6. Add logs, alerting, backups and rollback before launch.
7. Run both success-path and cross-tenant negative tests in CI.

External tools are examples to evaluate; FeverKit does not configure payment processors or process student data.
