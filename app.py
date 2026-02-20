"""
Emotion Detection Flask App.

This module detects emotions from input text using the Watson NLP API.
It provides routes for UI, API info, and emotion detection.

The user is using cloud-ide-kubernetes tools to complete the Developing AI Applications with Python and Flask course.
"""

import os
import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/Analyze"
)
WATSON_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json",
}


def emotion_detector(text_to_analyse):
    """Call Watson API to detect emotions from text."""
    if not text_to_analyse:
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 0,
            "sadness": 0,
            "dominant_emotion": None,
        }

    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(
            WATSON_URL,
            headers=WATSON_HEADERS,
            json=payload,
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 0,
            "sadness": 0,
            "dominant_emotion": None,
        }

    emotions = data.get("document", {}).get("emotion", {})
    dominant_emotion = max(emotions, key=emotions.get) if emotions else None

    return {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "dominant_emotion": dominant_emotion,
    }

@app.route("/", methods=["GET"])
def home():
    """Render the emotion detection."""
    return render_template("emotion.html")


@app.route("/info", methods=["GET"])
def info():
    """Explain how to use the API."""
    return (
        "Emotion Detector is running. "
        "Send POST requests to /detect_emotion with JSON {'text': 'your text'}."
    )


@app.route("/detect_emotion", methods=["POST"])
def detect_emotion():
    """Detect emotions from posted text."""
    data = request.get_json(silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    text = str(data["text"]).strip()
    if not text:
        return jsonify({"error": "Text must not be empty"}), 400

    emotions = emotion_detector(text)
    return jsonify(emotions), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5050")), debug=False)
    
