import os
# 数据库的设置
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'api.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}' # f标签里{}不会被/转义

SQLALCHEMY_TRACK_MODIFICATIONS = False