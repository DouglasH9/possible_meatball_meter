from types import MethodDescriptorType
from flask_app import app
from flask import redirect, session
from flask_app.models.user import User
from flask_app.models.review import Review

@app.route("/add_like/<int:reviewID>")
def add_like(reviewID):

    data = {
        "user_id" : session["user_id"],
        "review_id" : reviewID,
    }
