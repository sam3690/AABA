from fastapi import FastAPI
from app.api import jobs, monitoring

app = FastAPI(title="Autonomous AI Business Agent (AABA)")

# Routers
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(monitoring.router, prefix="/monitoring", tags=["Monitoring"])

@app.get("/")
def root():
    return {"message": "AABA backend is running 🚀"}
