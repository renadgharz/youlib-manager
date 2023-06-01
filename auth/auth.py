from flask import Blueprint, render_template, redirect, url_for
from auth.auth_forms import SignupForm, LoginForm, PasswordResetRequestForm, PasswordResetForm

auth_blueprint = Blueprint('auth_blueprint', __name__,
                           template_folder = "templates",
                           static_folder = "static")

@auth_blueprint.route("/auth/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    
    if form.validate_on_submit():
        # add code to send validated data to database
        return redirect(url_for('auth_blueprint.login'))
    
    return render_template("signup.html", signup_form=form)

@auth_blueprint.route("/auth/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        # grant access to user
        return redirect(url_for('')) # add route to home page of app blueprint once created
    
    return render_template("login.html", login_form=form)

@auth_blueprint.route("/auth/pwd-reset-request")
def pwd_reset_request():
    form = PasswordResetRequestForm()

    if form.validate_on_submit():
        # verify that email exists in db
        # send reset link to email upon validation
        pass
    
    return render_template("pwd_reset_request.html", pwd_reset_request_form=form)

@auth_blueprint.route("/auth/pwd-reset")
def pwd_reset():
    form  = PasswordResetForm()
    
    if form.validate_on_submit():
        # delete old password from db, add new password
        return redirect(url_for('auth_blueprint.login'))
    
    return render_template("pwd_reset.html", pwd_reset_form=form)

@auth_blueprint.route("/login")
def redir_login():
    return redirect(url_for("auth_blueprint.login"))

@auth_blueprint.route("/signup")
def redir_signup():
    return redirect(url_for("auth_blueprint.signup"))

@auth_blueprint.route("/pwd-reset-request")
def redir_pwd_reset_request():
    return redirect(url_for("auth_blueprint.pwd_reset_request"))

@auth_blueprint.route("/pwd-reset")
def redir_pwd_reset():
    return redirect(url_for("auth_blueprint.pwd_reset"))
