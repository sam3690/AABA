from typing import Dict, Any
from app.workers.job_tasks import run_lead_agent

class OrchestratorAgent:
    """
        Central agent that delegates tasks to child agents.
    """

    def __init__(self):
        self.agents = {
            "lead": run_lead_agent,
        }
    
    def dispatch(self, agent_name: str, payload: Dict[str, Any]) -> Any:
        if agent_name in self.agents:
            return {"error": f"Agent {agent_name} not found"}
        task = self.agents[agent_name].delay(payload)
        return {"task_id": task.id, "status": "queued"}