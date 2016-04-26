from flask import render_template, url_for, request, redirect, flash
from flask.ext.login import login_user
from . import auth
from ..models import User
from .forms import LoginForm


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remeber_me.data)
            return render_template(url_for('index'))
        flash("Invalid usrname or password")
    return render_template('auth/login.html', form=form)