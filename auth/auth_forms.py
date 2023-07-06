from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from models import User

class SignupForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(message="Field cannot be blank"), 
                                                   Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})
    email = StringField('Email', 
                        validators=[DataRequired(message="Field cannot be blank"), 
                                             Email(message="Must be a valid example@example.com")],
                        render_kw={"placeholder": "Email"})
    password = PasswordField('Password', 
                             validators=[DataRequired(message="Field cannot be blank"),
                                         Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(message="Field cannot be blank"),
                                                                     EqualTo('password', 
                                                                             message='Passwords must match')],
                                     render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign up')
    
    def validate_username(self, username):
        existing_username = User.query.filter_by(
            username=username.data).first()
        if existing_username:
            raise ValidationError("The username already exists.")
    
    def validate_email(self, email):
        existing_email = User.query.filter_by(
            email=email.data).first()
        if existing_email:
            raise ValidationError("This email is already exists.")
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Field cannot be blank"), Email(message="Must be a valid example@example.com")])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Field cannot be blank"), Email(message="Must be a valid example@example.com")])
    submit = SubmitField('Send link')

class PasswordResetForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired(message="Field cannot be blank")])
    confirm_password = PasswordField('Confirm new password',
                                     validators=[DataRequired(message="Field cannot be blank"), 
                                                 EqualTo(new_password,
                                                         message='Passwords must match')])
    submit = SubmitField('Change password')