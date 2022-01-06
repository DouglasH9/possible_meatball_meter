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

        # define self.user for Review as empty object to be filled when review's user info is pulled from database
        self.user = {}

    @classmethod
    def add_review(cls, data):
        # insert query to add reviews to databased
        query = "INSERT INTO reviews (review, is_blasted, rating, user_id, restaurant_name, is_affordable, created_at, updated_at) VALUES (%(review)s, %(is_blasted)s, %(rating)s, %(user_id)s, %(restaurant_name)s, %(is_affordable)s, NOW(), NOW())"
        print (query)
        return connectToMySQL("meatball_meter").query_db(query, data)

    @staticmethod
    def validate_review(data):
        is_valid = True
        if (len(data["review"]) < 10):
            flash("Review must be at least 10 characters, you absolute fool!")
            is_valid = False
        if (len(data["restaurant_name"]) < 2):
            flash("Restaurant name must be more than 2 characters, dingus!")
            is_valid = False
        if (float(data["rating"]) < 0):
            flash("Rating must be greater than or equal to zero, genius!")
            is_valid = False
        elif (float(data["rating"]) > 8.3):
            flash("Rating must be less than 8.3, ya goofball!")
            is_valid = False
        
        return is_valid 
        