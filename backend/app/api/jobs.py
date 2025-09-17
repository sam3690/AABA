from fastapi import APIRouter
from app.workers.job_tasks import add

router = APIRouter()

@router.get("/")
async def list_jobs():
    # Later: fetch from Postgres
    return {"jobs": ["example-job-1", "example-job-2"]}

@router.post("/test-task")
async def test_task(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id}
