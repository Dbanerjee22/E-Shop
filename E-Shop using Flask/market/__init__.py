from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 1
app.config['SECRET_KEY'] ='d4c3e047bddd96d1493cddae'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page" #to route user if they need authoriztion to access @login_required
login_manager.login_message_category = "info"

from market import route