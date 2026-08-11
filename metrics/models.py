from dataclasses import dataclass


@dataclass(frozen=True)
class WorkloadMetrics:
    cpu_percent: float
    memory_percent: float
    request_rate: float
    active_replicas: int

    def is_valid(self) -> bool:
        return (
            0 <= self.cpu_percent <= 100
            and 0 <= self.memory_percent <= 100
            and self.request_rate >= 0
            and self.active_replicas >= 0
        )