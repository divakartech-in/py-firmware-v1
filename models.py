from pydantic import BaseModel


class SpeedPayload(BaseModel):
    rpm: int  # Removed validation constraints


class MachineState(BaseModel):
    running: bool = False
    speed: int = 0
    temperature: float = 25.0
    alarm: bool = False
