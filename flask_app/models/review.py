from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user

class Review:
    def __init__(self, data):
        self.id = data["id"]
        self.review = data["review"]
        self.is_blasted = data["is_blasted"]
        self.rating = data["rating"]
        self.user_id = data["user_id"]
        self.restaurant_name = data["restaurant_name"]
        self.is_affordable = data["is_affordable"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.user = {}

    @classmethod
    def add_review(cls, data):
        query = "INSERT INTO reviews (review, is_blasted, rating, user_id, restaurant_name, is_affordable, created_at, updated_at) VALUES (%(review)s, %(is_blasted)s, %(rating)s, %(user_id)s, %(restaurant_name)s, %(is_affordable)s, %(created_at)s, %(updated_at)s)"
        print (query)
        return connectToMySQL("meatball_meter").query_db(query, data)