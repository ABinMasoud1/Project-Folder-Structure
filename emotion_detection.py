import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    body = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, json=body, headers=headers, timeout=5)

        if response.status_code != 200:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        data = response.json()["emotionPredictions"][0]["emotion"]

        result = {
            "anger": data["anger"],
            "disgust": data["disgust"],
            "fear": data["fear"],
            "joy": data["joy"],
            "sadness": data["sadness"],
        }

        result["dominant_emotion"] = max(result, key=result.get)

        return result

    except Exception:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }