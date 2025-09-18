from app.agents.lead_agent import fetch_leads
from celery import Celery
from app.core.config import settings

Celery_app = Celery(
    "worker",
    broker = settings.REDIS_URL,
    backend = settings.REDIS_URL,
)

@Celery_app.task
def add(x, y):
    return x + y

@Celery_app.task
def run_lead_agent(payload):
    return fetch_leads(payload)