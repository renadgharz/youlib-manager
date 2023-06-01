from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(),
                                         EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send link')

class PasswordResetForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm new password',
                                     validators=[DataRequired(), 
                                                 EqualTo(new_password,
                                                         message='Passwords must match')])
    submit = SubmitField('Change password')