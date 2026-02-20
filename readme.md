 Emotion Detection Flask App

A Flask web application that detects emotions from user text using the IBM Watson NLP Emotion API.

## Features
- Web UI at `/`
- Info endpoint at `/info`
- Emotion detection endpoint at `/detect_emotion` (POST)
- Handles blank input with `400` response
- Returns:
  - anger
  - disgust
  - fear
  - joy
  - sadness
  - dominant_emotion

## Project Structure
- `app.py` - Flask backend and routes
- `templates/emotion_detection.html` - UI template
- `static/css/emotion_detection.css` - stylesheet
- `__init__.py` - exposes `application` for deployment

## Requirements
- Python 3.10+
- Flask
- requests
- pylint (for static analysis)

## Installation
```bash
python -m pip install flask requests pylint
```

## Run the App
```bash
python app.py
```

Default URL:
- `http://127.0.0.1:5000/` (or port from `PORT` environment variable)

## API Usage

### POST `/detect_emotion`
Request:
```json
{
  "text": "I love this new technology."
}
```

Example (Windows):
```bash
curl -X POST "http://127.0.0.1:5000/detect_emotion" -H "Content-Type: application/json" -d "{\"text\":\"I love this new technology.\"}"
```

Response:
```json
{
  "anger": 0.01,
  "disgust": 0.00,
  "fear": 0.02,
  "joy": 0.90,
  "sadness": 0.01,
  "dominant_emotion": "joy"
}
```

## Static Code Analysis
```bash
python -m pylint app.py
```

## Notes
- Keep HTML files in `templates/`.
- Keep CSS files in `static/css/`.
- If deployment expects `application`, import from `__init__.py`.
