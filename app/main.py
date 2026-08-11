from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="SmartScale-K8s",
    description="Intelligent Kubernetes autoscaling control service",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "project": "SmartScale-K8s",
        "status": "running",
        "message": "Intelligent Kubernetes autoscaling service",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }