from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def load_home_page():
    # loads login and registration page
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

@app.route("/reg_success")
def reg_success():
    # redirects to login page if user id isn't in session, blocking people from accessing the site without logging in
    if "user_id" not in session:
        return redirect("logout")
    data = {
        "id" : session["user_id"]
    }
    # renders success page with user object as a variable "user"
    return render_template("reg_success.html", user = User.get_by_id(data))

@app.route("/login", methods=["POST"])
def login():
    # set data to email from form
    data = {"email" : request.form["email_log"]}
    # pass email through getbyemail function and retrieve user info
    user_in_db = User.get_by_email(data)
    print(user_in_db)

    if not user_in_db:
        # flash message if user doesn't exist
        flash("Invalid email dumbo!")
        return redirect("/")

    # check to see if hashed password matches using check password has method from bcrypt
    elif not bcrypt.check_password_hash(user_in_db.password, request.form["pass_log"]):
        # flash message if hashed password doesn't match stored hashed password
        flash("Wrong password ya dringus!!!")
        return redirect("/")

    # if user email in database and password matches put user id and user name in session
    session["user_id"] = user_in_db.id
    session["user_name"] = user_in_db.fName
    return redirect("/dashboard")

@app.route("/dashboard")
def render_dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : session["user_id"]
    }

    return render_template("dashboard.html", user = User.get_by_id(data))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")