from enum import Enum

from app.config import ScalingConfig
from metrics.models import WorkloadMetrics


class ScalingAction(str, Enum):
    SCALE_UP = "scale_up"
    SCALE_DOWN = "scale_down"
    HOLD = "hold"


def decide_scaling(
    metrics: WorkloadMetrics,
    config: ScalingConfig,
) -> ScalingAction:
    """Choose a conservative scaling action from current workload metrics."""

    if not metrics.is_valid():
        return ScalingAction.HOLD

    if metrics.cpu_percent >= config.cpu_target_percent:
        if metrics.active_replicas < config.max_replicas:
            return ScalingAction.SCALE_UP

    if metrics.memory_percent >= config.memory_target_percent:
        if metrics.active_replicas < config.max_replicas:
            return ScalingAction.SCALE_UP

    if (
        metrics.cpu_percent < config.cpu_target_percent * 0.5
        and metrics.memory_percent < config.memory_target_percent * 0.5
    ):
        if metrics.active_replicas > config.min_replicas:
            return ScalingAction.SCALE_DOWN

    return ScalingAction.HOLD