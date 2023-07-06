from flask import Blueprint, render_template, redirect, url_for, request
from auth.auth_forms import SignupForm, LoginForm, PasswordResetRequestForm, PasswordResetForm
from extensions import db
from models import UserCredentials


auth_blueprint = Blueprint('auth_blueprint', __name__,
                           template_folder = "templates",
                           static_folder = "static",
                           static_url_path = "/auth/static/")


@auth_blueprint.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    
    if form.validate_on_submit():
        form_data = request.form.to_dict()
        new_user = UserCredentials(**form_data)
        db.session.add(new_user)    
        db.session.commit()
        
        return redirect(url_for('auth_blueprint.login'))
    
    return render_template("signup.html", signup_form=form)

@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        # grant access to user
        return redirect(url_for('')) # add route to home page of app blueprint once created
    
    return render_template("login.html", login_form=form)

@auth_blueprint.route("/pwd-reset-request")
def pwd_reset_request():
    form = PasswordResetRequestForm()

    if form.validate_on_submit():
        # verify that email exists in db
        # send reset link to email upon validation
        pass
    
    return render_template("pwd_reset_request.html", pwd_reset_request_form=form)

@auth_blueprint.route("/pwd-reset")
def pwd_reset():
    form  = PasswordResetForm()
    
    if form.validate_on_submit():
        # delete old password from db, add new password
        return redirect(url_for('auth_blueprint.login'))
    
    return render_template("pwd_reset.html", pwd_reset_form=form)

