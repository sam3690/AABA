"""Lightweight NATS JetStream utility used by orchestrator and workers."""
from __future__ import annotations

import asyncio
import importlib
from typing import Any, Optional

from app.core.config import settings

NatsClientType = Any

_spec = importlib.util.find_spec("nats")
if _spec is None:  # pragma: no cover - optional dependency
    _NATS_MODULE = None  # type: ignore[assignment]
    _IMPORT_ERROR = ModuleNotFoundError(
        "nats-py package is not installed. Add `nats-py` to pyproject and reinstall."
    )
else:  # pragma: no cover
    _NATS_MODULE = importlib.import_module("nats")
    _IMPORT_ERROR = None

_client: Optional[NatsClientType] = None
_lock = asyncio.Lock()


async def get_nats_client() -> NatsClientType:
    """Return a singleton async NATS client."""
    if _NATS_MODULE is None:
        raise RuntimeError(str(_IMPORT_ERROR)) from _IMPORT_ERROR

    global _client  # pylint: disable=global-statement
    if _client is None or _client.is_closed:
        async with _lock:
            if _client is None or _client.is_closed:
                _client = await _NATS_MODULE.connect(settings.NATS_URL)
    return _client
