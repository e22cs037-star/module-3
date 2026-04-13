def detect_fraud(data):
    score = 0

    if data["copy_paste_count"] > 2:
        score += 20

    if data["window_switch_count"] > 2:
        score += 20

    if data["idle_time"] > 0.25:
        score += 15

    if data["sudden_typing_change"]:
        score += 25

    if data["typing_speed"] > 0.8:
        score += 20

    # ✅ Final decision
    status = "Fraud" if score >= 40 else "Normal"

    return status, score