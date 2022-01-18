from types import MethodDescriptorType
from flask_app import app
from flask import request, redirect
from flask_app.models.user import User
from flask_app.models.review import Review
from flask_app.models.like import Like

@app.route("/add_like/<int:reviewID>", methods=["POST"])
def add_like(reviewID):

    data = {
        "user_id" : request.form["user_id"],
        "review_id" : reviewID
    }

    if Like.check_for_like_in_db(data):
        Like.push_like_to_db(data)

    return redirect(f"/show_review/{reviewID}")

"""SQL query to see if user has liked specific post...

SELECT * FROM likes LEFT JOIN users ON users.id = likes.user_id LEFT JOIN reviews ON reviews.id = likes.review_id WHERE users.id = 1 AND likes.review_id = 10;
"""