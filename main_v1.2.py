from fastapi import FastAPI, HTTPException
from models import SpeedRequest
from motor import start_motor, stop_motor, set_speed
from safety import validate_temperature, emergency_shutdown

app = FastAPI(title="Machine Controller v1.2")

state = {
    "running": False,
    "speed": 0,
    "temperature": 25.0,
    "alarm": False
}


@app.post("/start")
def start():
    success, message = start_motor(state)
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {"status": message}


@app.post("/stop")
def stop():
    return {"status": stop_motor(state)}


@app.post("/set-speed")
def update_speed(req: SpeedRequest):
    success, message = set_speed(state, req.speed)
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {"status": message}


@app.post("/update-temperature/{temp}")
def update_temperature(temp: float):
    state["temperature"] = temp

    if not validate_temperature(temp):
        return emergency_shutdown(state)

    return {"status": "Temperature updated safely"}


@app.get("/status")
def status():
    return state
