# Agent Architecture Manual

## Purpose

This manual defines the baseline architecture for a modern incident-triage agent project.  
It specifies:

1. The expected directory layout and file responsibilities.
2. The core layering principles.
3. The key design decisions that make the system production-ready.

The goal is to keep the system modular, auditable, and easy to evolve.

## Core Layering Principles

The project is organized by separation of concerns.  
Each layer should own one responsibility:

1. `agents/`: Behavior logic and orchestration.
2. `llm/`: Model access and prompt assembly.
3. `rag/`: Knowledge ingestion and retrieval.
4. `tools/`: External capabilities and tool protocol integration.
5. `memory/`: State and memory lifecycle.
6. `api/`: External service exposure.
7. `infra/`: Runtime environment, deployment, and observability.

Guiding rule: avoid mixing concerns across layers unless there is a clear and documented interface boundary.

## Directory Tree

```text
incident-triage-agent/
|
|- agents/
|  |- base_agent.py
|  |- research_agent.py
|  |- coding_agent.py
|  `- orchestrator.py
|
|- llm/
|  |- client.py
|  |- prompt_builder.py
|  `- cache.py
|
|- rag/
|  |- ingestion/
|  |  `- chunker.py
|  |- embedder.py
|  |- retriever.py
|  `- reranker.py
|
|- tools/
|  |- mcp_server.py
|  |- web_search.py
|  |- code_executor.py
|  |- browser.py
|  `- file_ops.py
|
|- memory/
|  |- working_memory.py
|  `- episodic_memory.py
|
|- eval/
|  |- benchmarks/
|  |  `- llm_judge.py
|  `- metrics.py
|
|- api/
|  |- routes/
|  `- middleware.py
|
|- infra/
|  |- docker/
|  |- k8s/
|  `- observability/
|
|- config/
|  |- settings.py
|  `- prompts/
|
|- tests/
|- pyproject.toml
`- .env.example
```

## Key Design Decisions

### 1) MCP-first tool integration

`tools/mcp_server.py` is a first-class component.  
By implementing the MCP protocol once, any MCP-compatible client can reuse the same tools without duplicate integration work.

### 2) Unified model client abstraction

`llm/client.py` should abstract provider differences (recommended through `litellm` or an equivalent adapter).  
Business logic should not directly depend on a single vendor SDK.

### 3) Decomposed RAG pipeline

Split RAG into independent modules:

1. `chunker`
2. `embedder`
3. `retriever`
4. `reranker`

This enables targeted replacement and optimization. In practice, reranking is often the highest-leverage quality control point.

### 4) Evaluation as an engineering lane, not only tests

`eval/` is peer-level with business code, not hidden inside `tests/`.  
LLM evaluation requires dataset versioning, metric governance, and continuous regression tracking.

### 5) Prompt assets are versioned configuration

Store prompts in `config/prompts/` as structured files (for example YAML) and version them.  
Treat prompts as production assets, not inline strings spread across code.

## Directory and File Contract

The following contract reflects the architecture defined in `agent_project_directory_structure.html`.

### `agents/` (Core behavior layer)

- `base_agent.py`: Abstract base interface for agent execution lifecycle (`run`, `think`, `act`), tool registration, and retry/error behavior.
- `research_agent.py`: Research-focused agent that combines web search and RAG workflows.
- `coding_agent.py`: Coding-focused agent using execution sandbox and iterative repair loops.
- `orchestrator.py`: Multi-agent coordinator for routing, DAG-style task planning, parallel execution, and output consolidation.

### `llm/` (Model integration layer)

- `client.py`: Unified `chat()`, `stream()`, and `embed()` facade across providers.
- `prompt_builder.py`: Role-aware prompt composition and template variable resolution.
- `cache.py`: Semantic response caching with TTL to reduce cost and latency.

### `rag/` (Knowledge retrieval layer)

- `ingestion/`: Data loaders and document intake workflow.
- `ingestion/chunker.py`: Chunking strategies (windowed, recursive, semantic).
- `embedder.py`: Embedding generation with batch processing and retries.
- `retriever.py`: Hybrid retrieval combining dense and sparse search.
- `reranker.py`: Cross-encoder style ranking to refine top candidates.

### `tools/` (External capability layer)

- `mcp_server.py`: MCP server exposing tool interfaces over `stdio`/`SSE`.
- `web_search.py`: Search providers adapter with normalized structured results.
- `code_executor.py`: Isolated sandbox execution with timeout and output capture.
- `browser.py`: Browser automation (navigation, interaction, screenshot).
- `file_ops.py`: Controlled filesystem operations with path safety boundaries.

### `memory/` (State and memory layer)

- `working_memory.py`: Short-lived runtime state for the current task/session.
- `episodic_memory.py`: Long-term compressed history for cross-session retrieval.

### `eval/` (Evaluation layer)

- `benchmarks/`: Curated benchmark datasets by capability class.
- `benchmarks/llm_judge.py`: LLM-as-judge scoring pipeline and rubric handling.
- `metrics.py`: Metric computation (faithfulness, relevance, safety, and task metrics).

### `api/` (Service interface layer)

- `routes/`: Endpoint modules for chat/task/tool APIs.
- `routes/middleware.py`: Authentication, rate limiting, logging, CORS, and request guards.

### `infra/` (Runtime and operations layer)

- `docker/`: Container images and local-compose runtime definitions.
- `k8s/`: Kubernetes manifests and scaling topology.
- `observability/`: Tracing, metrics, and prompt/version observability integration.

### `config/` (Configuration layer)

- `settings.py`: Type-safe central settings loaded from environment.
- `prompts/`: Versioned prompt templates with environment/experiment controls.

### `tests/` (Quality gate layer)

- Unit, integration, and end-to-end tests.
- LLM/tool behavior should be mocked where deterministic reproducibility is required.

### Root project files

- `pyproject.toml`: Build metadata, dependencies, developer tooling.
- `.env.example`: Required environment variable template.

## Interface Boundaries and Dependency Direction

Recommended high-level dependency direction:

1. `api/` depends on `agents/`.
2. `agents/` depends on `llm/`, `rag/`, `tools/`, and `memory/`.
3. `rag/` and `tools/` may depend on shared config/utilities, but should stay independent of API concerns.
4. `eval/` depends on the same runtime components but should not become a production request path.
5. `infra/` and `config/` support all layers but should not embed business logic.

Avoid reverse coupling (for example, `llm/` importing API routes, or `tools/` importing orchestrator internals).

## Operational and Governance Notes

1. Keep model outputs separated from deterministic business rules.
2. Preserve decision auditability for triage actions.
3. Put production write actions behind explicit approvals and configuration flags.
4. Keep secrets out of source code and use environment/secret management.
5. Prefer incremental architectural changes with corresponding tests and evaluation updates.

## Definition of Done for New Modules

A new module is considered complete when:

1. It is placed in the correct layer and does not blur boundaries.
2. Its public interface is explicit and typed.
3. Failure modes are visible and handled.
4. It has tests for regressible behavior.
5. If prompt-dependent, prompt assets are externalized and versioned.
6. If quality-sensitive, the change is reflected in `eval/` benchmarks or metrics.

---

This manual is the baseline contract.  
Teams can extend it for domain-specific needs, but should document and review any cross-layer exception explicitly.
