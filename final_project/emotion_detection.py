import requests

def emotion_detector(text_to_analyze):
    """
    Diagnostic version of the emotion_detector function
    that prints the entire JSON to identify its structure.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            response_json = response.json()
            # Print the entire response JSON to see its structure
            print("DEBUG: Entire Watson Response:", response_json)
            return response_json
        except ValueError:
            return "Error parsing JSON response."
    else:
        return f"Error: {response.status_code}, {response.text}"