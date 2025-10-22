from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import datetime

class User:
    def __init__(self, name, email, password, role='user'):
        self.name = name
        self.email = email
        self.password = self.hash_password(password)
        self.role = role

    def hash_password(self, password):
        return Bcrypt().generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'created_at': datetime.utcnow()
        }