# Flask
## flask_app
#### 项目来源:https://overiq.com/flask/0.12/intro-to-flask/
#### 这个项目主要包含了Flask框架一些基础的知识,搭建了一个网站其中包括几个模块
##### 1.admin 用户的登陆认证的网页
##### 2.article 选择文字的样式,更改显示样式的网页
##### 3.contact 一个通过邮件模块,发送留言给网站作者的网页
##### 4.index 主页
##### 5.login 登陆的网页,登陆后显示用户信息,包含一个logout的links
# ------------------------------
#### 用到的第三方扩展有:
##### Flask-Login:控制登陆的拓展
##### Flask-Mail:邮件发送的拓展
##### Flask-Migrate:数据库管理的拓展
##### Flask-Script:定义命令行参数的拓展
##### Flask-SQLAlchemy:sql链接库,本项目用的是mysql
##### Flask-WTF:表单管理的拓展
# ------------------------------
#### 还有最后利用blueprint,把整个项目从原来的main2.py文件里的所有代码,重构成规范的flask项目

requirements.txt可以通过pip命令自动生成和安装  
生成requirements.txt文件  
pip freeze > requirements.txt  
安装requirements.txt依赖  
pip install -r requirements.txt  
