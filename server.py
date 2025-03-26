from flask import Flask, request, jsonify
from final_project.EmotionDetection import emotion_detector

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "Emotion Detection API is running! Use /emotionDetector endpoint to analyze text."

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze:
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "message": "Invalid text! Please try again!"
        }), 400

    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if response.get("dominant_emotion") is None:
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "message": "Invalid text! Please try again!"
        }), 400

    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)