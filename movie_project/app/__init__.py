from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

login = LoginManager()
login.init_app(app)
login.login_view = 'admin.login'

from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
