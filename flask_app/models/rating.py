from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user

class Rating:
    def __init__(self, data):
        self.id = data["id"]
        self.review = data["review"]
        self.is_blasted = data["is_blasted"]
        self.rating = data["rating"]
        self.user_id = data["user_id"]
        self.restaurant_name = data["restaurant_name"]
        self.is_affordable = data["is_affordable"]