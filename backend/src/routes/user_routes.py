from flask import Blueprint, request, jsonify
from models.user import User
from services.notification_service import send_notification
from utils.validator import validate_user_data
from flask_jwt_extended import create_access_token

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not validate_user_data(data):
        return jsonify({"msg": "Invalid data"}), 400

    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],  # Ensure to hash this password in the User model
        role=data.get('role', 'user')
    )
    new_user.save()  # Assuming a save method exists in the User model
    send_notification(new_user.email, "Welcome!", "Thank you for registering!")

    return jsonify({"msg": "User registered successfully"}), 201

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.find_by_email(data['email'])  # Assuming a method to find user by email

    if user and user.verify_password(data['password']):  # Assuming a method to verify password
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401