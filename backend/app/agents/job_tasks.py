from app.agents.lead_agent import fetch_leads
from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "worker",
    broker = settings.REDIS_URL,
    backend = settings.REDIS_URL,
)

@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def run_lead_agent(payload):
    query = payload.get("query", "default search")
    return fetch_leads(query)