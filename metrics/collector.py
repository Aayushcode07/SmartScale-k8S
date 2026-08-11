from abc import ABC, abstractmethod

from metrics.models import WorkloadMetrics


class MetricsCollector(ABC):
    """Base interface for obtaining workload metrics."""

    @abstractmethod
    def collect(self) -> WorkloadMetrics:
        """Return the latest workload metrics."""
        raise NotImplementedError