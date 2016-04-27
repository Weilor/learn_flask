from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp
from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    remember_me = BooleanField('Remember me')


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0,
                                                          message="username must have only letters, "
                                                                  "numbers, dots or underscores")])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password2', message="Password must match")])
    password2 = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already in use.")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username is already in use.")