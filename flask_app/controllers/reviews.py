from types import MethodDescriptorType
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.review import Review
from flask_app.models import user

@app.route("/add_review")
def render_add_a_review():
    return render_template("/add_review.html")
