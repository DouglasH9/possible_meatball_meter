from types import MethodDescriptorType
from flask_app import app
from flask import redirect, session
from flask_app.models.user import User
from flask_app.models.review import Review
from flask_app.models.like import Like

@app.route("/add_like/<int:reviewID>", methods=["POST"])
def add_like(reviewID):

    data = {
        "user_id" : session["user_id"],
        "review_id" : reviewID,
    }
    
    if Like.check_for_like_in_db(data):
        Like.add_like(data)
