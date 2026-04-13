from flask import Flask, request, jsonify
from services.preprocessing import preprocess_data
from services.fraud_rules import detect_fraud

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Backend Running Successfully"

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        # ✅ Validate input
        required_fields = [
            "typing_speed", "key_hold_time", "mouse_speed",
            "pause_time", "copy_paste_count",
            "window_switch_count", "idle_time",
            "sudden_typing_change"
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # ✅ Preprocess
        processed = preprocess_data(data)

        # ✅ Fraud detection
        result, score = detect_fraud(processed)

        return jsonify({
            "status": result,
            "fraud_score": score,
            "processed_data": processed
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)