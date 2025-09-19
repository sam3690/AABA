from fastapi import APIRouter
from app.agents.orchestrator import OrchestratorAgent
from app.workers.job_tasks import celery_app

router = APIRouter()
orchestrator = OrchestratorAgent()

@router.post("/run-lead")
async def run_lead_agent(payload: dict):
    """
    Dispatch task to lead Agent via Orchestrator
    """
    return orchestrator.dispatch("lead", payload)


@router.get("/status/{task_id}")
async def get_task_status(task_id: str):
    """
    Retrieve the status and result of a celery task.
    """
    result = celery_app.AsyncResult(task_id)
    return{
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None
    }