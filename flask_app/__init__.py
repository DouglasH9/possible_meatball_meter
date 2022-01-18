from flask import Flask
from flask_app.config.mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "jinkies!"

def get_likes_count_for_review(reviewID: int) -> int:

    data ={
        "review_id" : reviewID
    }
    query = "SELECT * FROM likes WHERE review_id = %(review_id)s"
    result = connectToMySQL("meatball_meter").query_db(query, data)

    likes_count = 0

    for row in result:
        likes_count += 1

    return likes_count

def get_dislikes_count_for_review(reviewID: int) -> int:

    data ={
        "review_id" : reviewID
    }
    query = "SELECT * FROM dislikes WHERE review_id = %(review_id)s"
    result = connectToMySQL("meatball_meter").query_db(query, data)

    dislikes_count = 0

    for row in result:
        dislikes_count += 1

    return dislikes_count

def check_to_see_if_user_liked_review(userID, reviewID):

    data = {
        "user_id" : userID,
        "review_id" : reviewID
    }

    user_has_liked_post = True

    query = "SELECT * FROM likes LEFT JOIN users ON users.id = likes.user_id LEFT JOIN reviews ON reviews.id = likes.review_id WHERE users.id = %(user_id)s AND likes.review_id = %(review_id)s;"
    result = connectToMySQL("meatball_meter").query_db(query, data)

    if (result == () ):
        user_has_liked_post = False

    return user_has_liked_post

def check_to_see_if_user_disliked_review(userID, reviewID):

    data = {
        "user_id" : userID,
        "review_id" : reviewID
    }

    user_has_disliked_post = True

    query = "SELECT * FROM dislikes LEFT JOIN users ON users.id = dislikes.user_id LEFT JOIN reviews ON reviews.id = dislikes.review_id WHERE users.id = %(user_id)s AND dislikes.review_id = %(review_id)s;"
    result = connectToMySQL("meatball_meter").query_db(query, data)

    if (result == () ):
        user_has_disliked_post = False

    return user_has_disliked_post


app.jinja_env.globals.update(get_likes_count_for_review = get_likes_count_for_review, get_dislikes_count_for_review = get_dislikes_count_for_review, check_to_see_if_user_liked_review = check_to_see_if_user_liked_review, check_to_see_if_user_disliked_review = check_to_see_if_user_disliked_review)