from flask import Flask
from flask_app.config.mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "jinkies!"

def get_likes_count_for_review(data):

    
    query = "SELECT * FROM likes WHERE review_id = %(reviewID)s"
    result = connectToMySQL("meatball_meter").query_db(query, data)
    print(result)
    
    likes_count = 0

    return likes_count

app.jinja_env.globals.update(get_likes_count_for_review = get_likes_count_for_review)