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

    @classmethod
    def get_all_reviews(cls):

        # left join query grabs all reviews with users.id left joined to user_id
        query = "SELECT * FROM reviews LEFT JOIN users ON users.id = user_id;"
        result = connectToMySQL("meatball_meter").query_db(query)

        # declares an all_reviews List variable to store the queried reviews
        all_reviews = []

        # creates and instance of a review from each row of results
        for row in result:
            review = cls(row)

            # creates instance of user who left review and stores in dictionary
            user_data = {
                # specify users.id because both users and reviews will have a unique id
                "id" : row["users.id"],
                "fName" : row["fName"],
                "lName" : row["lName"],
                "email" : row["email"],
                "password" : row["password"],
                # specify users created at and update at, because reviews will also have created and updated columns
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            # setting user_data to the user attribute of the review
            review.user = user.User(user_data)
            # append all the reviews to the all_reviews list
            all_reviews.append(review)

        return all_reviews
            
    @classmethod
    def get_one_review(cls, data):
        
        query = "SELECT * FROM reviews LEFT JOIN users ON users.id = user_id WHERE reviews.id = %(id)s;"
        result = connectToMySQL("meatball_meter").query_db(query, data)

        # create instance of review in var called "review" taking the the first dictionary returned in result List
        review = cls(result[0])

        # create user instance from the LEFT JOINED table results from query
        user_data ={
            "id" : result[0]["users.id"],
            "fName" : result[0]["fName"],
            "lName" : result[0]["lName"],
            "email" : result[0]["email"],
            "password" : result[0]["password"],
            "created_at" : result[0]["created_at"],
            "updated_at" : result[0]["updated_at"]
        }
        review.user = user.User(user_data)
        return review

    @classmethod
    def get_users_reviews(cls, data):
        query = "SELECT * FROM reviews LEFT JOIN users on users.id = reviews.user_id WHERE users.id = %(id)s"
        result = connectToMySQL("meatball_meter").query_db(query, data)

        all_user_reviews = []

        for row in result:
            review = cls(row)

            user_data = {
                "id" : row["id"],
                "fName" : row["fName"],
                "lName" : row["lName"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            
            review.user = user.User(user_data)
            print(row)
            all_user_reviews.append(review)
        print(all_user_reviews[0].user)
        return all_user_reviews

    @classmethod
    def send_edit_to_db(cls, data):
        query = "UPDATE reviews SET review = %(review)s, is_blasted = %(is_blasted)s, rating = %(rating)s, restaurant_name = %(restaurant_name)s, is_affordable = %(is_affordable)s, updated_at = NOW() WHERE id = %(id)s"
        result = connectToMySQL("meatball_meter").query_db(query, data)
        return result

    @classmethod
    def delete_review(cls, data):
        query = "DELETE FROM reviews WHERE id = %(id)s"
        result = connectToMySQL("meatball_meter").query_db(query, data)
        return result
