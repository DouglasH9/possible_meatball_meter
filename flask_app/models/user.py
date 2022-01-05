from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.fName = data["fName"]
        self.lName = data["lName"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (fName, lName, email, password, created_at, updated_at) VALUES ( %(fName)s, %(lName)s, %(email)s, %(password)s, NOW(), NOW() )"
        return connectToMySQL("meatball_meter").query_db(query, data)

    #email registration validation
    @staticmethod
    def validate_email_reg(data):
        # set to true, if anything fails tests, is valid will flip to False
        is_valid = True
        # query to see if user already exists in database
        query = "SELECT * FROM users WHERE email = %(email)s"
        # db connection
        results = connectToMySQL("meatball_meter").query_db(query, data)
        # checks for password length
        if (len(data["pass_ent"]) < 8):
            flash("Password is not long enough!")
            is_valid = False
        # checks to see if entered password matches password confirmation
        if (data["pass_ent"] != data["pass_con "]):
            flash("Passwords do not match")
            is_valid = False
        # checks to see if email is already in database
        if len(results > 0):
            flash("Email is already taken, Bozo!")
            is_valid = False
        # checks for email length
        if len(data["email"] < 4):
            flash("Email must be longer than 3 characters")
            return False
        # checks to see if email matches email regex format
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    # method to get user from database using their email
    def get_by_email(cls, data):
        # sql query checking for user by email
        query = "SELECT * FROM users WHERE email = %(email)s"
        # defines result from query
        result = connectToMySQL("meatball_meter").query_db(query, data)
        # logic for what to do after checking for user
        if len(result) < 1:
            return False
        # return user data if user in database
        return cls(result[0])

    @classmethod
    # method to get user from database using their id
    def get_by_id(cls, data):
        # sql query
        query = "SELECT * FROM users WHERE id = %(id)s"
        # define results
        results = connectToMySQL("meatball_meter").query_db(query, data)
        return cls(results[0])

