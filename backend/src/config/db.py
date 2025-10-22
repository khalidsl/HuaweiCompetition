from pymongo import MongoClient
import os

def get_db_connection():
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client.get_default_database()  # Replace with your database name if needed
    return db