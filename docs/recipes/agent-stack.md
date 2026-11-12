# Recipe: local / remote AI coding team

Profiles: `core,ai-agents,devops`

1. Define coordinator, minimal subagents and role-specific permissions. Start with FeverKit's architect, implementer, reviewer, agent-integrator and LLM infrastructure roles.
2. Choose **one** model gateway (consider OmniRoute) with explicit providers and credential handling.
3. Choose **one** primary code-context solution (Graphify or Repomix) and add Context7 for current external docs when needed.
4. Choose memory deliberately (e.g. claude-mem) only after retention/privacy review.
5. Choose an orchestrator only if a basic agent loop is insufficient (LangGraph, PydanticAI or Hermes Agent; avoid stacking all three).
6. Evaluate via a fixed benchmark of coding tasks and Promptfoo; record correctness, latency, tokens and failed tool calls.
7. Separate internet/browsing permissions from shell/deployment; place tools in a sandbox.

**Anti-pattern:** installing 10 unrelated agent runtimes and trusting them with the same production credentials.
