from dataclasses import dataclass


@dataclass(frozen=True)
class ScalingConfig:
    min_replicas: int = 1
    max_replicas: int = 10
    cpu_target_percent: int = 70
    memory_target_percent: int = 75
    scale_up_step: int = 1
    scale_down_step: int = 1


DEFAULT_SCALING_CONFIG = ScalingConfig()