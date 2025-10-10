from fastapi import FastAPI

from app.api import jobs, monitoring, agents
from app.core.metrics import instrument_app
from app.core.observability import setup_tracing

app = FastAPI(title="Autonomous AI Business Agent (AABA)")

setup_tracing("aaba-api")
instrument_app(app)

# Routers
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(monitoring.router, prefix="/monitoring", tags=["Monitoring"])
app.include_router(agents.router, prefix="/agents", tags=["Agents"])

@app.get("/")
def root():
    return {"message": "AABA backend is running 🚀"}
