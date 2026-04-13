def preprocess_data(data):
    try:
        return {
            "typing_speed": data["typing_speed"] / 100,
            "key_hold_time": data["key_hold_time"] / 200,
            "mouse_speed": data["mouse_speed"] / 1000,
            "pause_time": data["pause_time"] / 10,
            "idle_time": data["idle_time"] / 60,
            "copy_paste_count": data["copy_paste_count"],
            "window_switch_count": data["window_switch_count"],
            "sudden_typing_change": data["sudden_typing_change"]
        }
    except Exception as e:
        raise ValueError(f"Preprocessing error: {e}")