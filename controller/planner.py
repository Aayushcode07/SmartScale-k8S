from dataclasses import dataclass

from app.config import ScalingConfig
from controller.decision import ScalingAction, decide_scaling
from controller.safety import apply_safety_guard
from metrics.models import WorkloadMetrics


@dataclass(frozen=True)
class ScalingPlan:
    action: ScalingAction
    current_replicas: int
    target_replicas: int


def create_scaling_plan(
    metrics: WorkloadMetrics,
    config: ScalingConfig,
) -> ScalingPlan:
    """Create a scaling decision and apply safety limits."""

    action = decide_scaling(metrics, config)

    target_replicas = apply_safety_guard(
        action=action,
        current_replicas=metrics.active_replicas,
        config=config,
    )

    return ScalingPlan(
        action=action,
        current_replicas=metrics.active_replicas,
        target_replicas=target_replicas,
    )