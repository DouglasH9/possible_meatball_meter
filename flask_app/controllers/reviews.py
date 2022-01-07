from types import MethodDescriptorType
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.review import Review
from flask_app.models import user

@app.route("/add_review")
def render_add_a_review():
    return render_template("/add_review.html")

@app.route("push_review", methods=["POST"])
def push_review_to_db():
    if "user_id" not in session:
        return redirect("/logout")

    data = {
        "restaurant_name" : request.form["restaurant_name"],
        "review" : request.form["review"],
        "rating" : request.form["rating"], 
        "is_affordable" : request.form["is_affordable"],
        "user_id" : session["user_id"]
    }
    if not Review.validate_review(data):
        return redirect("/dashboard")

    Review.add_review(data)
    return redirect("/dashboard")
