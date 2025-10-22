from flask import Blueprint, request, jsonify
from controllers.emotion_controller import EmotionController

emotion_routes = Blueprint('emotion_routes', __name__)

@emotion_routes.route('/analyze/facial', methods=['POST'])
def analyze_facial_emotion():
    data = request.json
    result = EmotionController.analyze_facial(data)
    return jsonify(result), 200

@emotion_routes.route('/analyze/voice', methods=['POST'])
def analyze_voice_emotion():
    data = request.json
    result = EmotionController.analyze_voice(data)
    return jsonify(result), 200

@emotion_routes.route('/logs', methods=['GET'])
def get_emotion_logs():
    logs = EmotionController.get_logs()
    return jsonify(logs), 200

@emotion_routes.route('/logs/<user_id>', methods=['GET'])
def get_user_emotion_logs(user_id):
    logs = EmotionController.get_user_logs(user_id)
    return jsonify(logs), 200