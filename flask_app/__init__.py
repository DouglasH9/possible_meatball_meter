from flask import Flask
from flask_app.config.mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "jinkies!"

def get_likes_count_for_review(reviewID: int) -> int:

    data ={
        "review_id" : reviewID
    }
    query = f"SELECT * FROM likes WHERE review_id = {reviewID}"
    result = connectToMySQL("meatball_meter").query_db(query, data)

    likes_count = 0

    for row in result:
        likes_count += 1

    return likes_count

app.jinja_env.globals.update(get_likes_count_for_review = get_likes_count_for_review)