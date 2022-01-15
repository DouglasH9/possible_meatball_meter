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
    def push_like_to_db(cls, data):

        query = "INSERT INTO likes (user_id, review_id, created_at, updated_at) VALUES (%(user_id)s, %(review_id)s, NOW(), NOW());"
        print(query)
        result = connectToMySQL("meatball_meter").query_db(query, data)
        return result

    @staticmethod
    def check_for_like_in_db(data):

        # set variable for whether existence of like is True or False
        does_not_exist_in_db = True

        # query for like matching user_id AND review_id
        query = "SELECT * FROM likes WHERE user_id = %(user_id)s AND review_id = %(review_id)s"
        # store result of query in variable named "result"
        result = connectToMySQL("meatball_meter").query_db(query,data)

        print(result)

        # if result is greater than zero, like exists, set var to False
        if ( result != () ):
            does_not_exist_in_db = False
        # return boolean for existence of like
        print(does_not_exist_in_db)
        return does_not_exist_in_db

    @classmethod
    def delete_like(cls, data):
        query = "DELETE FROM likes WHERE id = %(id)s"
        result = connectToMySQL("meatball_meter").query_db(query, data)
        return result