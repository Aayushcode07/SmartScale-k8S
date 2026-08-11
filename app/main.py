from datetime import datetime, timezone

from fastapi import FastAPI

from metrics.local_collector import LocalMetricsCollector


app = FastAPI(
    title="SmartScale-K8S",
    description="Intelligent Kubernetes autoscaling control service",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "project": "SmartScale-K8S",
        "status": "running",
        "message": "Intelligent Kubernetes autoscaling service",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/metrics/current")
def current_metrics():
    collector = LocalMetricsCollector(
        cpu_percent=82,
        memory_percent=68,
        request_rate=145,
        active_replicas=3,
    )

    metrics = collector.collect()

    return {
        "cpu_percent": metrics.cpu_percent,
        "memory_percent": metrics.memory_percent,
        "request_rate": metrics.request_rate,
        "active_replicas": metrics.active_replicas,
        "valid": metrics.is_valid(),
    }