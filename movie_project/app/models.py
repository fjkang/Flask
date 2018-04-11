from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  #编号
    name = db.Column(db.String(100), unique=True)  #昵称
    pwd = db.Column(db.String(100))  #密码
    email = db.Column(db.String(100), unique=True)  #邮箱
    phone = db.Column(db.String(11), unique=True)  #电话
    info = db.Column(db.Text)  #简介
    face = db.Column(db.String(255), unique=True)  #头像
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #创建时间
    uuid = db.Column(db.String(255), unique=True)  #标识号
    userlogs = db.relationship('Userlog', backref='user')  #用户日志外键关系
    comments = db.relationship('Comment', backref='user')  #评论外键关系
    moviecols = db.relationship('Moviecol', backref='user')  #收藏外键关系

    def __repr__(self):
        return f"<User {self.name}>"


# 用户登陆日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  #编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #所属用户
    ip = db.Column(db.String(100))  #登陆ip
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #登陆时间

    def __repr__(self):
        return f"<Userlog {self.id}>"


#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  #编号
    name = db.Column(db.String(100), unique=True)  #名称
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #创建时间
    movies = db.relationship('Movie', backref='tag')  #电影外键关系

    def __repr__(self):
        return f"<Tag {self.name}>"


#电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  #编号
    title = db.Column(db.String(255), unique=True)  #标题
    url = db.Column(db.String(255), unique=True)  #地址
    info = db.Column(db.Text)  #简介
    logo = db.Column(db.String(255), unique=True)  #封面
    star = db.Column(db.SmallInteger)  #星级
    playnum = db.Column(db.BigInteger)  #播放数
    commentnum = db.Column(db.BigInteger)  #评论数
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  #所属标签
    area = db.Column(db.String(255))  #上映地区
    release_time = db.Column(db.DateTime)  #上映时间
    length = db.Column(db.String(100))  #时长
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #创建时间
    comments = db.relationship('Comment', backref='movie')  #评论外键关系
    moviecols = db.relationship('Moviecol', backref='movie')  #收藏外键关系

    def __repr__(self):
        return f"<Movie {self.title}>"


# 上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  #编号
    title = db.Column(db.String(255), unique=True)  #标题
    logo = db.Column(db.String(255), unique=True)  #封面
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #创建时间

    def __repr__(self):
        return f"<Preview {self.title}>"


#评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  #编号
    content = db.Column(db.Text)  #内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  #所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #所属用户
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #最后登陆时间

    def __repr__(self):
        return f"<Comment {self.id}>"


#收藏电影
class Moviecol(db.Model):
    __tablename__ = "moviecol"    
    id = db.Column(db.Integer, primary_key=True)  #编号
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  #所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #所属用户
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #最后登陆时间

    def __repr__(self):
        return f"<Moviecol {self.id}>"

# 权限
class Auth(db.Model):
    __tablename__ = "auth"    
    id = db.Column(db.Integer, primary_key=True)  #编号
    name = db.Column(db.String(100), unique=True)  #名称
    url = db.Column(db.String(255), unique=True)  #地址
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #最后登陆时间

    def __repr__(self):
        return f"<Auth {self.name}>"


# 角色
class Role(db.Model):
    __tablename__ = "role"    
    id = db.Column(db.Integer, primary_key=True)  #编号
    name = db.Column(db.String(100), unique=True)  #名称
    auths = db.Column(db.String(600))  #权限
    addtime = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)  #最后登陆时间

    def __repr__(self):
        return f"<Role {self.name}>"

