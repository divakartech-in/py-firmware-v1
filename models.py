from pydantic import BaseModel, Field


class SpeedRequest(BaseModel):
    speed: int = Field(..., ge=0, le=5000)


class MachineState(BaseModel):
    running: bool = False
    speed: int = 0
    temperature: float = 25.0
    alarm: bool = False
