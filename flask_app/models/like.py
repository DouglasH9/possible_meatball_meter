from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user
from flask_app.models import review

class Like:
    def __init__(self, data):
        self.id = data["id"],
        self.user_id = data["user_id"],
        self.review_id = data["review_id"],
        self.created_at = data["created_at"],
        self.updated_at = data["updated_at"],

        # empty object for user data for possible later features
        self.user = {}

        # empty object for review data
        self.review = {}

    @classmethod
    def add_like(cls, data):
        query = "INSERT INTO likes (user_id, review_id, created_at, updated_at) VALUES (%(user_id)s, %(review_id)s, NOW(), NOW());"
        print(query)
        return connectToMySQL("meatball_meter").query_db(query, data)

    @classmethod
    def delete_like(cls, data):
        query = "DELETE FROM likes WHERE id = %(id)s"
        result = connectToMySQL("meatball_meter").query_db(query, data)
        return result