from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
from flask_login import LoginManager
import os, config

from mail import mail_setting

# 创建Flask应用实例
# app = Flask(__name__)
# app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')

# 初始化flask的第三方拓展

# for key, value in mail_setting.items():
#     app.config[key] = value
# 要config赋值之后再创建Mail()实例

# 以下改为blueprints控制
###################################
db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


# 定义app工厂
def create_app(config):
    # 创建app实例
    app = Flask(__name__)
    app.config.from_object(config)
    for key, value in mail_setting.items():
        app.config[key] = value
    # 要config赋值之后再创建Mail()实例

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 注册blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # print(app.config)

    return app