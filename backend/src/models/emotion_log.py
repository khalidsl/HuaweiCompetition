from datetime import datetime
from flask import current_app
from flask_pymongo import PyMongo

mongo = PyMongo()

class EmotionLog:
    def __init__(self, user_id, emotion, confidence):
        self.user_id = user_id
        self.emotion = emotion
        self.confidence = confidence
        self.timestamp = datetime.utcnow()

    def save_to_db(self):
        emotion_log_data = {
            "user_id": self.user_id,
            "emotion": self.emotion,
            "confidence": self.confidence,
            "timestamp": self.timestamp
        }
        mongo.db.emotion_logs.insert_one(emotion_log_data)

    @staticmethod
    def get_logs_by_user(user_id):
        return mongo.db.emotion_logs.find({"user_id": user_id})