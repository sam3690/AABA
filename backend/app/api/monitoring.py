from fastapi import APIRouter
from app.core.redis import redis_client

router = APIRouter()

@router.get("/health")
async def health_check():
    try:
        redis_client.ping()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
