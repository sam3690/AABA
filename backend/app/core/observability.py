"""OpenTelemetry bootstrap helpers for API and workers."""
from __future__ import annotations

import importlib

from app.core.config import settings

_trace_spec = importlib.util.find_spec("opentelemetry")
if _trace_spec is None:  # pragma: no cover - optional dependency
    trace = None  # type: ignore[assignment]
    OTLPSpanExporter = None  # type: ignore[assignment]
    Resource = None  # type: ignore[assignment]
    TracerProvider = None  # type: ignore[assignment]
    BatchSpanProcessor = None  # type: ignore[assignment]
else:  # pragma: no cover
    trace = importlib.import_module("opentelemetry").trace  # type: ignore[assignment]
    exporter_module = importlib.import_module(
        "opentelemetry.exporter.otlp.proto.grpc.trace_exporter"
    )
    sdk_resources = importlib.import_module("opentelemetry.sdk.resources")
    sdk_trace = importlib.import_module("opentelemetry.sdk.trace")
    sdk_export = importlib.import_module("opentelemetry.sdk.trace.export")
    OTLPSpanExporter = exporter_module.OTLPSpanExporter  # type: ignore[assignment]
    Resource = sdk_resources.Resource  # type: ignore[assignment]
    TracerProvider = sdk_trace.TracerProvider  # type: ignore[assignment]
    BatchSpanProcessor = sdk_export.BatchSpanProcessor  # type: ignore[assignment]


def setup_tracing(service_name: str) -> None:
    """Initialise a basic OTLP exporter if OpenTelemetry packages are available."""
    if trace is None:
        return

    resource = Resource(attributes={"service.name": service_name})
    provider = TracerProvider(resource=resource)
    span_processor = BatchSpanProcessor(
        OTLPSpanExporter(endpoint=settings.OTEL_EXPORTER_OTLP_ENDPOINT)
    )
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)
