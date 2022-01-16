from flask_app import app

from flask_app.controllers import users
from flask_app.controllers import reviews
from flask_app.controllers import likes
from flask_app.controllers import dislikes

if __name__ == "__main__":
    app.run(debug = True)
