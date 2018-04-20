from flask import Blueprint

tasks = Blueprint('tasks', __name__)

import api.tasks.views