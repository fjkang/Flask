from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)
db = SQLAlchemy(app)

from api.tasks import tasks as tasks_blueprint
from api.users import users as users_blueprint


app.register_blueprint(tasks_blueprint)
app.register_blueprint(users_blueprint)



