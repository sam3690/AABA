# Autonomous Autonomous Business Administration (AABA)

An open-source infrastructure scaffold for building autonomous business administration agents. This repository delivers the base services, development tooling, and observability plumbing outlined in the reference architecture.

## Why this repo exists

- ✨ **Composable services** – FastAPI gateway, Celery workers, Redis broker, Postgres, MongoDB, MinIO, Weaviate, NATS, and more.
- 🔭 **Full observability stack** – OpenTelemetry Collector, Prometheus, Grafana, Loki, Jaeger, exporters, and Flower.
- 🧱 **Ready-to-extend** – Keep the existing code structure/logic while enabling rapid iteration on agent behavior and integrations.
- 👐 **Open source friendly** – Contribution guidelines, licensing, docs, and env templates bundled in.

See `docs/infrastructure-overview.md` for a service-by-service walkthrough that mirrors the attached architecture diagram.

## Quick start

1. **Clone**
	```bash
	git clone https://github.com/sam3690/AABA.git
	cd AABA
	```
2. **Bootstrap environment**
	```bash
	cp .env.example .env
	```
	Adjust secrets as needed (MinIO, Grafana, Postgres, integrations, etc.).
3. **Launch the stack**
	```bash
	cd infra
	docker compose up --build
	```
4. **Access key endpoints**
	- FastAPI: http://localhost:8000/docs
	- Frontend Dev Server: http://localhost:3000
	- Flower (Celery UI): http://localhost:5555
	- Grafana: http://localhost:3001 (default `admin/changeme`)
	- Prometheus: http://localhost:9090
	- Alertmanager: http://localhost:9093
	- Jaeger UI: http://localhost:16686
	- MinIO Console: http://localhost:9001
	- pgAdmin: http://localhost:5050
	- Mongo Express: http://localhost:8081

## Stack overview

| Capability | Service(s) |
| --- | --- |
| API Gateway | FastAPI (`backend` service) |
| Background jobs | Celery worker & beat (`celery-worker`, `celery-beat`) |
| Data stores | Postgres, MongoDB, MinIO, Weaviate |
| Messaging/eventing | Redis, NATS |
| Monitoring | OpenTelemetry Collector, Prometheus, Grafana, Alertmanager, Loki, Promtail, Jaeger |
| Admin UIs | Flower, pgAdmin, Mongo Express |

## Environment variables

All runtime configuration flows through `.env`. The tracked `.env.example` highlights the complete list with safe defaults for local development. Copy and edit as necessary before running the stack.

Key groups include:

- Database credentials (`POSTGRES_*`, `MONGO_*`)
- Broker & messaging (`REDIS_URL`, `NATS_URL`)
- Object storage (`MINIO_*`)
- Vector store (`WEAVIATE_URL`)
- Observability endpoints (`OTEL_EXPORTER_OTLP_ENDPOINT`, Grafana/Prometheus URLs)
- Admin dashboards and default credentials
- Placeholder SaaS integration secrets (Stripe, Slack, Gmail, QuickBooks, etc.)

## Development workflow

- **Backend** – Uses `uv` for dependency management (`cd backend && uv sync`). Launch locally with `uv run uvicorn app.main:app --reload`.
- **Celery** – Modules live under `backend/app/workers`. Workers are wired to Redis and instrumented with OpenTelemetry helpers.
- **Frontend** – Vite + React (`cd frontend && npm install && npm run dev`). The production build is not covered in this base setup.
- **Testing** – `uv run pytest` inside `backend`. Additional lint/format hooks provided via `ruff`, `black`, and `mypy` (see `pyproject.toml`).

## Optional dependencies

Some helper modules (MinIO, NATS, Weaviate, OpenTelemetry, Prometheus metrics) lazily import their respective packages. If you plan to use these features outside of Docker, install the extras locally:

```bash
uv add minio nats-py weaviate-client opentelemetry-sdk opentelemetry-exporter-otlp prometheus-client
```

## Contributing

We welcome pull requests! Please read `CONTRIBUTING.md` for coding standards, branching strategy, and how to run the validation checks.

## License

This project is released under the MIT License. See `LICENSE` for details.