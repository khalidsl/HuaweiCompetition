from flask import Blueprint, request, jsonify
from controllers.typing_controller import TypingController

typing_routes = Blueprint('typing_routes', __name__)

@typing_routes.route('/typing/analyze', methods=['POST'])
def analyze_typing():
    data = request.json
    result = TypingController.analyze_typing_behavior(data)
    return jsonify(result), 200

@typing_routes.route('/typing/log', methods=['POST'])
def log_typing():
    data = request.json
    result = TypingController.log_typing_data(data)
    return jsonify(result), 201

@typing_routes.route('/typing/history/<user_id>', methods=['GET'])
def get_typing_history(user_id):
    result = TypingController.get_typing_history(user_id)
    return jsonify(result), 200