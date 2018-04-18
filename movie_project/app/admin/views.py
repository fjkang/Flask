from flask import render_template, redirect, url_for, flash, session, request
from flask_login import login_user, login_required, logout_user

from . import admin
from app.admin.forms import LoginForm, TagForm
from app.models import Admin, Tag
from app import db


@admin.route("/")
@login_required
def index():
    return render_template("admin/index.html")


#后台登陆
@admin.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(name=form.data["account"]).first()
        if admin and admin.check_pwd(form.data["pwd"]):
            login_user(admin)
            return redirect(url_for("admin.index"))
        flash("密码错误!")
        return redirect(url_for('admin.login'))
    return render_template("admin/login.html", form=form)


@admin.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin.login"))


@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")


# 添加标签
@admin.route("/tag_add/", methods=['GET', 'POST'])
@login_required
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        if Tag.query.filter_by(name=form.data['name']).count() == 1:
            flash("标签已存在!", "err")
            return redirect(url_for('admin.tag_add'))

        tag = Tag(name=form.data['name'])
        db.session.add(tag)
        db.session.commit()
        flash("添加标签成功!", "ok")
        redirect(url_for('admin.tag_add'))
    return render_template("admin/tag_add.html", form=form)


# 标签列表
@admin.route("/tag_list/<int:page>/", methods=["GET"])
def tag_list(page=None):
    if page == None:
        page = 1
    pagedata = Tag.query.order_by(Tag.addtime.desc()).paginate(
        page=page, per_page=10)
    return render_template("admin/tag_list.html", pagedata=pagedata)


# 删除标签
@admin.route("/tag_list/del/<int:id>", methods=["GET"])
def tag_del(id=None):
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    flash("删除标签成功!", "ok")
    return redirect(url_for('admin.tag_list', page=1))


# 编辑标签
@admin.route("/tag_list/edit/<int:id>", methods=["GET", "POST"])
def tag_edit(id):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        if tag.name != form.data["name"] and Tag.query.filter_by(
                name=form.data['name']).count() == 1:
            flash("标签已存在!", "err")
            return redirect(url_for('admin.tag_edit', id=id))

        tag.name = form.data["name"]
        db.session.add(tag)
        db.session.commit()
        flash("修改标签成功!", "ok")
        redirect(url_for('admin.tag_edit', id=id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)


@admin.route("/movie_add/")
def movie_add():
    return render_template("admin/movie_add.html")


@admin.route("/movie_list/")
def movie_list():
    return render_template("admin/movie_list.html")


@admin.route("/preview_add/")
def preview_add():
    return render_template("admin/preview_add.html")


@admin.route("/preview_list/")
def preview_list():
    return render_template("admin/preview_list.html")


@admin.route("/user_list/")
def user_list():
    return render_template("admin/user_list.html")


@admin.route("/comment_list/")
def comment_list():
    return render_template("admin/comment_list.html")


@admin.route("/moviecol_list/")
def moviecol_list():
    return render_template("admin/moviecol_list.html")


@admin.route("/oplog_list/")
def oplog_list():
    return render_template("admin/oplog_list.html")


@admin.route("/adminloginlog_list/")
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")


@admin.route("/userloginlog_list/")
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")


@admin.route("/auth_add/")
def auth_add():
    return render_template("admin/auth_add.html")


@admin.route("/auth_list/")
def auth_list():
    return render_template("admin/auth_list.html")


@admin.route("/role_add/")
def role_add():
    return render_template("admin/role_add.html")


@admin.route("/role_list/")
def role_list():
    return render_template("admin/role_list.html")


@admin.route("/admin_add/")
def admin_add():
    return render_template("admin/admin_add.html")


@admin.route("/admin_list/")
def admin_list():
    return render_template("admin/admin_list.html")
