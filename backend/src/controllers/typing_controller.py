from flask import request, jsonify
from ..models.typing_behavior import TypingBehavior  # Assuming you have a TypingBehavior model
from ..services.ai_service import analyze_typing_behavior

class TypingController:
    @staticmethod
    def analyze_typing():
        data = request.get_json()
        if not data or 'user_id' not in data or 'typing_data' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        user_id = data['user_id']
        typing_data = data['typing_data']
        
        # Analyze typing behavior using the AI service
        analysis_result = analyze_typing_behavior(user_id, typing_data)
        
        # Save the analysis result to the database
        typing_behavior = TypingBehavior(user_id=user_id, analysis_result=analysis_result)
        typing_behavior.save()  # Assuming you have a save method in your model
        
        return jsonify({'result': analysis_result}), 200

    @staticmethod
    def get_typing_logs(user_id):
        logs = TypingBehavior.query.filter_by(user_id=user_id).all()  # Assuming you have a query method
        return jsonify([log.to_dict() for log in logs]), 200  # Assuming you have a to_dict method in your model