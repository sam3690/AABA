"""Prometheus metrics wiring for FastAPI with graceful degradation."""
from __future__ import annotations

import importlib
from typing import Any

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

_spec = importlib.util.find_spec("prometheus_client")
if _spec:
    prometheus_client = importlib.import_module("prometheus_client")
else:  # pragma: no cover - optional dependency
    prometheus_client = None


def instrument_app(app: FastAPI) -> None:
    """Attach /metrics endpoint when prometheus_client is available."""
    if prometheus_client is None:
        @app.get("/metrics", include_in_schema=False)
        async def metrics_unavailable() -> PlainTextResponse:  # type: ignore[return-value]
            return PlainTextResponse("prometheus_client missing", status_code=503)

        return

    registry: Any = prometheus_client.REGISTRY

    @app.get("/metrics", include_in_schema=False)
    async def metrics() -> PlainTextResponse:  # type: ignore[return-value]
        return PlainTextResponse(prometheus_client.generate_latest(registry))
