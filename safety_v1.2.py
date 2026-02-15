MAX_TEMP = 100.0


def validate_temperature(temp: float):
    if temp > MAX_TEMP:
        return False
    return True


def emergency_shutdown(state: dict):
    state["running"] = False
    state["speed"] = 0
    state["alarm"] = True
    return {"status": "EMERGENCY_STOPPED"}
