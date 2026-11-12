---
name: feverkit-local-llm
description: Evaluate and deploy local LLM inference deliberately.
---

# Local Llm

Use this skill when the task matches its purpose. Adapt to the project; it is guidance, not executable code.

1. Inspect hardware: GPU architecture, driver support, VRAM, RAM, CPU, storage and power.
2. Clarify target use: code editing, tool calling, chat, long context or vision.
3. Choose supported inference runtime and quantization; do not invent tokens/s benchmarks.
4. Test a representative prompt set for quality, tool calls, stability, memory and latency.
5. Put endpoint credentials behind a server process, isolate local network access and avoid exposed admin APIs.
6. Benchmark under expected concurrency, document tradeoffs and have a rollback plan.

**Deliverable:** short evidence-based findings, changed files (if any), tests executed, risks, and next steps.
