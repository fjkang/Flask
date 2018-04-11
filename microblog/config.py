import os
# 数据库的设置
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}' # f标签里{}不会被/转义
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 表单安全的一些措施
CSRF_ENABLE = True
SECRET_KEY = 'you-will-never-guess'
# OPENID供应商的链接
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# 模拟邮箱服务器设置
# 开启邮箱服务器命令:python -m smtpd -n -c DebuggingServer localhost:25
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
# 管理员列表
ADMINS = ['you@example.com']
# 分页参数
POSTS_PER_PAGE = 3

