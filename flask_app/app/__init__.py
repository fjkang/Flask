from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
from flask_login import LoginManager
import os, config

from mail import mail_setting

# 创建Flask应用实例
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')

# 初始化flask的第三方拓展
db = SQLAlchemy(app)
for key, value in mail_setting.items():
    app.config[key] = value
mail = Mail(app)    # 这句代码要放在config赋值之后
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# 导入视图模块
from . import views