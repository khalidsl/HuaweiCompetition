from flask import Blueprint, request, jsonify
from services.ai_service import analyze_emotion
from models.emotion_log import EmotionLog
from utils.logger import log_error

emotion_controller = Blueprint('emotion_controller', __name__)

@emotion_controller.route('/analyze/facial', methods=['POST'])
def analyze_facial_emotion():
    try:
        data = request.json
        image = data.get('image')
        if not image:
            return jsonify({'error': 'Image data is required'}), 400
        
        result = analyze_emotion(image, 'facial')
        emotion_log = EmotionLog(user_id=data.get('user_id'), emotion=result['emotion'], confidence=result['confidence'])
        emotion_log.save()
        
        return jsonify(result), 200
    except Exception as e:
        log_error(e)
        return jsonify({'error': 'An error occurred while analyzing facial emotion'}), 500

@emotion_controller.route('/analyze/voice', methods=['POST'])
def analyze_voice_emotion():
    try:
        data = request.json
        audio = data.get('audio')
        if not audio:
            return jsonify({'error': 'Audio data is required'}), 400
        
        result = analyze_emotion(audio, 'voice')
        emotion_log = EmotionLog(user_id=data.get('user_id'), emotion=result['emotion'], confidence=result['confidence'])
        emotion_log.save()
        
        return jsonify(result), 200
    except Exception as e:
        log_error(e)
        return jsonify({'error': 'An error occurred while analyzing voice emotion'}), 500