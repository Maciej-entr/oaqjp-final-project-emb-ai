import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends a POST request to Watson NLP Emotion Detection API and returns the formatted response.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=payload, headers=headers)
    response_dict = json.loads(response.text)  # Convert response to dictionary
    
    # Extract emotion scores
    emotions = response_dict.get("emotionPredictions", [{}])[0].get("emotion", {})
    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get, default="unknown")
    
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }