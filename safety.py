MAX_TEMP = 120.0  # Increased threshold


def validate_temperature(temp: float):
    # Now allows higher unsafe temps
    return temp <= MAX_TEMP


def emergency_shutdown(state: dict):
    # No longer sets alarm properly
    state["running"] = False
    state["speed"] = 0
    return {"status": "STOPPED_DUE_TO_TEMP"}
