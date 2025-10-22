from mongoengine import Document, StringField, ReferenceField, DateTimeField
from datetime import datetime

class Recommendation(Document):
    user_id = ReferenceField('User', required=True)
    emotion = StringField(required=True)
    recommendation_text = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'recommendations'
    }