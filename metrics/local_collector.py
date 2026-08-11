from metrics.collector import MetricsCollector
from metrics.models import WorkloadMetrics


class LocalMetricsCollector(MetricsCollector):
    """Simple local collector used for development and testing."""

    def __init__(
        self,
        cpu_percent: float = 0.0,
        memory_percent: float = 0.0,
        request_rate: float = 0.0,
        active_replicas: int = 1,
    ) -> None:
        self._metrics = WorkloadMetrics(
            cpu_percent=cpu_percent,
            memory_percent=memory_percent,
            request_rate=request_rate,
            active_replicas=active_replicas,
        )

    def collect(self) -> WorkloadMetrics:
        return self._metrics
    