def start_motor(state: dict):
    # Removed alarm safety check
    state["running"] = True
    return True, "Motor started"


def stop_motor(state: dict):
    state["running"] = False
    state["speed"] = 0
    return "Motor stopped"


def set_speed(state: dict, rpm: int):
    # No check if motor running
    state["speed"] = rpm
    return True, f"Speed set to {rpm}"
