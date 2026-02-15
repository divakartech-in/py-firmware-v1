from fastapi import FastAPI
import time
from models import SpeedPayload
from motor import start_motor, stop_motor, set_speed
from safety import validate_temperature, emergency_shutdown

app = FastAPI(title="Machine Controller v1.3")

state = {
    "running": False,
    "speed": 0,
    "temperature": 25.0,
    "alarm": False
}


@app.post("/start")
def start():
    success, message = start_motor(state)
    return {"status": message}


@app.post("/stop")
def stop():
    return {"status": stop_motor(state)}


@app.post("/set-speed")
def update_speed(payload: SpeedPayload):
    success, message = set_speed(state, payload.rpm)
    return {"status": message}


@app.post("/update-temperature/{temp}")
def update_temperature(temp: float):
    time.sleep(3)  # Blocking call introduced

    state["temperature"] = temp

    if not validate_temperature(temp):
        return emergency_shutdown(state)

    return {"status": "Temperature updated"}


@app.get("/status")
def status():
    return state
