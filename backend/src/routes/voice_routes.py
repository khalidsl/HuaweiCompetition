from flask import Blueprint, request, jsonify
from controllers.voice_controller import VoiceController

voice_routes = Blueprint('voice_routes', __name__)

@voice_routes.route('/api/voice/analyze', methods=['POST'])
def analyze_voice():
    audio_file = request.files.get('audio')
    if not audio_file:
        return jsonify({'error': 'No audio file provided'}), 400
    
    result = VoiceController.analyze_audio(audio_file)
    return jsonify(result), 200

@voice_routes.route('/api/voice/emotions', methods=['GET'])
def get_voice_emotions():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    emotions = VoiceController.get_user_voice_emotions(user_id)
    return jsonify(emotions), 200