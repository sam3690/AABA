from app.core.config import settings
from app.core.observability import setup_tracing
from celery import Celery

from app.agents.lead_agent import fetch_leads

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

setup_tracing("aaba-worker")

@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def run_lead_agent(payload):
    return fetch_leads(payload)
