def start_motor(state: dict):
    if state["alarm"]:
        return False, "Machine in alarm state"
    state["running"] = True
    return True, "Motor started"


def stop_motor(state: dict):
    state["running"] = False
    state["speed"] = 0
    return "Motor stopped"


def set_speed(state: dict, speed: int):
    if not state["running"]:
        return False, "Motor not running"

    state["speed"] = speed
    return True, f"Speed set to {speed}"
