from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detection App Running"

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("textToAnalyze")

    if not text or text.strip() == "":
        return "Invalid input! Please enter text."

    result = emotion_detector(text)

    return (
        f"Anger: {result['anger']}<br>"
        f"Disgust: {result['disgust']}<br>"
        f"Fear: {result['fear']}<br>"
        f"Joy: {result['joy']}<br>"
        f"Sadness: {result['sadness']}<br>"
        f"Dominant Emotion: {result['dominant_emotion']}"
    )

if __name__ == "__main__":
    app.run(debug=True)