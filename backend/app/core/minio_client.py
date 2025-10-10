"""MinIO helper for storing automation artefacts."""
from __future__ import annotations

import importlib
from typing import Any, Optional

from app.core.config import settings

MinioType = Any

_spec = importlib.util.find_spec("minio")
if _spec is None:  # pragma: no cover - optional dependency
    _Minio = None  # type: ignore[assignment]
    _IMPORT_ERROR = ModuleNotFoundError(
        "minio package is not installed. Add `minio` to pyproject and reinstall."
    )
else:  # pragma: no cover
    minio_module = importlib.import_module("minio")
    _Minio = getattr(minio_module, "Minio")  # type: ignore[assignment]
    _IMPORT_ERROR = None

_client: Optional[MinioType] = None


def get_minio_client() -> MinioType:
    """Return a singleton MinIO client configured from environment variables."""
    if _Minio is None:
        raise RuntimeError(str(_IMPORT_ERROR)) from _IMPORT_ERROR

    global _client  # pylint: disable=global-statement
    if _client is None:
        _client = _Minio(
            settings.MINIO_ENDPOINT.replace("http://", "").replace("https://", ""),
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_ENDPOINT.startswith("https"),
        )
    return _client
