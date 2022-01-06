from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def load_home_page():
    return render_template("login_reg.html")

@app.route("/register", methods=["POST"])
def register_user():

    # if info doesn't pass validations, redirect to login page
    if not User.validate_email_reg(request.form):
        return redirect("/")

    # hash entered password if password passes validations
    pw_hash = bcrypt.generate_password_hash(request.form["pass_ent"])

    # create user instance for database with form info
    data = {
        "fName" : request.form["fName"],
        "lName" : request.form["lName"],
        "email" : request.form["email"],
        "password" : pw_hash
    }

    id = User.register_user(data)
    # put user id in session after successful registration
    session["user_id"] = id
    # redirect to success page after successful registration
    return redirect("/reg_success")