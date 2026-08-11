from app.config import ScalingConfig
from controller.decision import ScalingAction


def apply_safety_guard(
    action: ScalingAction,
    current_replicas: int,
    config: ScalingConfig,
) -> int:
    """Return a safe target replica count within configured limits."""

    if current_replicas < config.min_replicas:
        current_replicas = config.min_replicas

    if current_replicas > config.max_replicas:
        current_replicas = config.max_replicas

    if action == ScalingAction.SCALE_UP:
        return min(
            current_replicas + config.scale_up_step,
            config.max_replicas,
        )

    if action == ScalingAction.SCALE_DOWN:
        return max(
            current_replicas - config.scale_down_step,
            config.min_replicas,
        )

    return current_replicas