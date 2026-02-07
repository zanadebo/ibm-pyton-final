from flask import Flask, request, jsonify, send_from_directory
import requests
import os
from emotion_detector import analyze_emotion

API_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {
	'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
	'Content-Type': 'application/json'
}

app = Flask(__name__, static_folder='')


@app.route('/')
def index():
	return send_from_directory('.', 'emotion.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json(silent=True)
    text = (data or {}).get('text', '')
    result = analyze_emotion(text)
    status = 200 if result and result.get('anger') is not None or result.get('dominant_emotion') is not None else 200
    return jsonify(result), status


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)