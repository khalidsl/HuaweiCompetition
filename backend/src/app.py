from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config.db import init_db
from routes.user_routes import user_routes
from routes.emotion_routes import emotion_routes
from routes.voice_routes import voice_routes
from routes.typing_routes import typing_routes

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Initialize CORS
    CORS(app)

    # Initialize JWT
    jwt = JWTManager(app)

    # Initialize database
    init_db(app)

    # Register routes
    app.register_blueprint(user_routes)
    app.register_blueprint(emotion_routes)
    app.register_blueprint(voice_routes)
    app.register_blueprint(typing_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)