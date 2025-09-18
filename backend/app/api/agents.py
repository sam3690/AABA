from fastapi import APIRouter
from app.agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()

@router.post("/run-lead")
async def run_lead_agent(payload: dict):
    """
    Dispatch task to lead Agent via Orchestrator
    """