"""Weaviate helper for semantic memory access."""
from __future__ import annotations

import importlib
from typing import Any

from app.core.config import settings

WeaviateClientType = Any

_spec = importlib.util.find_spec("weaviate")
if _spec is None:  # pragma: no cover - optional dependency
    _WEAVIATE_MODULE = None  # type: ignore[assignment]
    _IMPORT_ERROR = ModuleNotFoundError(
        "weaviate-client package is not installed. Add it to pyproject and reinstall."
    )
else:  # pragma: no cover
    _WEAVIATE_MODULE = importlib.import_module("weaviate")
    _IMPORT_ERROR = None


def get_vector_client() -> WeaviateClientType:
    if _WEAVIATE_MODULE is None:
        raise RuntimeError(str(_IMPORT_ERROR)) from _IMPORT_ERROR

    return _WEAVIATE_MODULE.Client(
        url=settings.WEAVIATE_URL,
        additional_headers={"X-Aba-Origin": "backend"},
    )
