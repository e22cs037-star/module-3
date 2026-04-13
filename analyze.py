from flask import Blueprint, request, jsonify
from services.preprocessing import preprocess_data
from services.feature_engineering import extract_features
from services.fraud_rules import detect_fraud

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    processed = preprocess_data(data)
    features = extract_features(processed)
    result = detect_fraud(features)

    return jsonify({
        "features": features,
        "result": result
    })