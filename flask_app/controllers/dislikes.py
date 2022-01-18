from types import MethodDescriptorType
from flask_app import app
from flask import request, redirect
from flask_app.models.user import User
from flask_app.models.review import Review
from flask_app.models.like import Like
from flask_app.models.dislike import Dislike

@app.route("/add_dislike/<int:reviewID>", methods=["POST"])
def add_dislike(reviewID):

    data = {
        "user_id" : request.form["user_id"],
        "review_id" : reviewID
    }

    if Dislike.check_for_dislike_in_db(data):
        Dislike.push_dislike_to_db(data)

    return redirect(f"/show_review/{reviewID}")

@app.route("/delete_dislike/<int:reviewID>", methods=["POST"])
def delete_dislike(reviewID):

    data = {
        "user_id" : request.form["user_id"],
        "review_id" : reviewID
    }

    Dislike.delete_dislike(data)

    return redirect(f"/show_review/{reviewID}")