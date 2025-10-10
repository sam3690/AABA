# Backend Service

The backend is a FastAPI application that orchestrates business automation workflows, dispatches Celery jobs, and integrates with the data and messaging layers defined in the base infrastructure.

## Local development

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

The server listens on `http://127.0.0.1:8000` by default (or `backend:8000` inside Docker). API docs are available at `/docs`.

## Celery worker

```bash
uv run celery -A app.workers.job_tasks worker --loglevel=info
```

A beat process is also defined for scheduled jobs:

```bash
uv run celery -A app.workers.job_tasks beat --loglevel=info
```

## Configuration

Settings are loaded from environment variables in `app/core/config.py`. Copy the root `.env.example` to `.env` to supply defaults. Notable options:

- `POSTGRES_*` for SQL persistence
- `MONGO_URI`, `MONGO_DB` for document store
- `REDIS_URL` for Celery broker/result backend
- `NATS_URL` for event streaming (optional)
- `MINIO_*` for object storage
- `WEAVIATE_URL` for vector search
- `OTEL_EXPORTER_OTLP_ENDPOINT` for tracing export

## Optional libraries

Modules under `app/core` lazily import optional clients (MinIO, NATS, Weaviate, OpenTelemetry, Prometheus). When running outside Docker, install them via:

```bash
uv add minio nats-py weaviate-client opentelemetry-sdk opentelemetry-exporter-otlp prometheus-client
```

## Testing

```bash
uv run pytest
```

Static analysis helpers:

```bash
uv run ruff check app
uv run mypy app
uv run black --check app
```
