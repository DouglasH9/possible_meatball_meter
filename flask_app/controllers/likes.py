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

@app.route("/delete_like/<int:reviewID>", methods=["POST"])
def delete_like(reviewID):

    data = {
        "user_id" : request.form["user_id"],
        "review_id" : reviewID
    }

    Like.delete_like(data)

    return redirect(f"/show_review/{reviewID}")