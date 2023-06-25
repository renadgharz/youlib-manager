from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Field cannot be blank")])
    email = StringField('Email', validators=[DataRequired(message="Field cannot be blank"), Email(message="Must be a valid example@example.com")])
    password = PasswordField('Password', 
                             validators=[DataRequired(message="Field cannot be blank"),
                                         Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[`~!@#$%^&*()_+-=[]{}|\;:\'\",./<>?])[A-Za-z\d`~!@#$%^&*()_+-=[]{}|\;:\'\",./<>?]{8,}', 
                                                message="Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character"),
                                         Length(min=8, message="Password must be at least 8 characters long")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message="Field cannot be blank"),
                                                                     EqualTo('password', 
                                                                             message='Passwords must match')])
    submit = SubmitField('Sign up')
    
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