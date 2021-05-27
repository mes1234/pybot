from dataclasses import dataclass


@dataclass
class MotorAction:
    ramp_up: bool
    ramp_down: bool
    power: int
    time_ms: int
