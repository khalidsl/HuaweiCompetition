from flask import request
from werkzeug.exceptions import BadRequest

def validate_user_registration(data):
    if not data.get('name'):
        raise BadRequest("Name is required.")
    if not data.get('email'):
        raise BadRequest("Email is required.")
    if not data.get('password'):
        raise BadRequest("Password is required.")
    if len(data['password']) < 6:
        raise BadRequest("Password must be at least 6 characters long.")

def validate_emotion_analysis(data):
    if not data.get('user_id'):
        raise BadRequest("User ID is required.")
    if not data.get('emotion_data'):
        raise BadRequest("Emotion data is required.")

def validate_voice_analysis(data):
    if not data.get('audio_file'):
        raise BadRequest("Audio file is required.")