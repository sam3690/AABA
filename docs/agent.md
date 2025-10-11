# Agent System Overview

This document explains how autonomous agents are structured inside the AABA backend, how they coordinate their work, and where to extend them.

## Core components

### Orchestrator (`app/agents/orchestrator.py`)
- Acts as the central dispatcher for all autonomous agents.
- Maintains a registry mapping agent names (e.g., `"lead"`) to executable callables (usually Celery tasks).
- Receives API requests and enqueues Celery jobs via `.delay(payload)`.
- Returns a task identifier and the current queue status.

### Lead Generation Agent (`app/agents/lead_agent.py`)
- Demonstrates how to wrap domain logic or LLM-powered workflows.
- Provides a `fetch_lead_tool` OpenAI tool (currently mocked) that returns sample job leads.
- `run_leads_agent_llm` sketches integration with the OpenAI Agents API (note: response call requires further implementation corrections).
- For production use you would replace the mock responses with calls to Upwork, Freelancer, LinkedIn, etc., and manage credentials in `.env`.

### Worker layer (`app/workers/job_tasks.py`)
- Celery worker that instantiates the orchestrator tasks.
- Exposes `run_lead_agent` which depends on the lead agent module, plus a sample `add` task for smoke testing.
- Instrumented with OpenTelemetry (`setup_tracing("aaba-worker")`) so distributed traces include worker spans when OTEL packages are installed.

## Control flow

```text
API request -> FastAPI router -> Orchestrator.dispatch -> Celery task -> Worker executes agent -> Persists or emits events
```

1. A client hits `POST /agents/run-lead`.
2. `OrchestratorAgent.dispatch("lead", payload)` looks up the Celery task.
3. The task is queued (`run_lead_agent.delay(payload)`), Redis acts as broker/result backend.
4. Celery worker pulls the job, runs lead-agent logic, and returns the result asynchronously.
5. Clients query `GET /agents/status/{task_id}` to check status/result using Celery AsyncResult.

## Data stores & integration points

- **Redis** – Broker/backend for Celery tasks.
- **Postgres/Mongo** – Currently unused by demo agents but ready for storing results and audit logs.
- **NATS** – Planned event distribution; leverage `app/core/events.py` once `nats-py` is installed.
- **MinIO / Weaviate** – Optional persistence for documents or vectorised knowledge bases.

## Logging & observability

- API and workers call `setup_tracing` to export spans to the OpenTelemetry Collector (`otel-collector` service). Ensure OTEL packages are installed when running outside Docker.
- Prometheus scraping uses `/metrics` (graceful fallback if `prometheus-client` is missing).
- Grafana dashboard (`AABA Overview`) visualises request throughput, with Loki ingesting logs when Promtail runs alongside Docker.

## Extending the agent roster

1. **Create a new agent module** under `app/agents/` with your business logic.
2. **Expose a Celery task** in `app/workers/job_tasks.py` that calls the agent implementation.
3. **Register the task** in the orchestrator registry (`self.agents["new-agent"] = run_new_agent_task`).
4. **Add API routes** in `app/api/agents.py` to accept input payloads and validate schema.
5. **Document env vars** or external secrets in `.env.example` and README if new integrations are required.

### Suggested template

```python
# app/agents/example_agent.py
from typing import Dict, Any

def run(payload: Dict[str, Any]) -> Dict[str, Any]:
    # TODO: implement logic
    return {"message": "success"}

# app/workers/job_tasks.py
@celery_app.task
def run_example_agent(payload):
    return example_agent.run(payload)

# app/agents/orchestrator.py
self.agents["example"] = run_example_agent
```

## Current limitations

- The orchestrator’s dispatch logic contains a bug (`if agent_name in self.agents:` should reject when missing). Fixing this is recommended before production use.
- Lead agent’s LLM integration is illustrative; `client.beta.agents.resoinse.create` is misspelled and likely needs adjustment to the latest OpenAI SDK methods.
- Agent results are not persisted; add database writes or event publishing as you flesh out workflows.

## Roadmap ideas

- Implement multi-step automations (e.g., lead enrichment, CRM updates) using task chains or NATS subjects.
- Capture agent transcripts in MongoDB and vectorise with Weaviate for memory retrieval.
- Add streaming progress updates via WebSockets or Server-Sent Events.
- Harden security with role-based access, encrypted secrets, and audit trails.
