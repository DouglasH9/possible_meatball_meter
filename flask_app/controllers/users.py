from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def load_home_page():
    return render_template("login_reg.html")