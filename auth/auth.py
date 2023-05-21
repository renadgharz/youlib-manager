from flask import Blueprint, render_template, redirect, url_for

auth_blueprint =Blueprint('auth_blueprint', __name__,
                          template_folder = "templates",
                          static_folder = "static")

@auth_blueprint.route("/auth/login")
def login():
    return render_template("login.html")

@auth_blueprint.route("/auth/signup")
def signup():
    return render_template("signup.html")

@auth_blueprint.route("/auth/forgot-password")
def forgot_pwd():
    return render_template("forgot_pwd.html")

@auth_blueprint.route("/login")
def redir_login():
    return redirect(url_for("auth_blueprint.login"))

@auth_blueprint.route("/signup")
def redir_signup():
    return redirect(url_for("auth_blueprint.signup"))

@auth_blueprint.route("/forgot-password")
def redir_forgot_pwd():
    return redirect(url_for("auth_blueprint.forgot_pwd"))
