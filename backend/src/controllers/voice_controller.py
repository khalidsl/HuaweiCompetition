from flask import request, jsonify
from services.ai_service import analyze_voice_sentiment

class VoiceController:
    @staticmethod
    def analyze():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        try:
            result = analyze_voice_sentiment(file)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500