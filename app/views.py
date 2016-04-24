from app import app
from flask import render_template, flash, redirect
from forms import LoginForm


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash("OpenID=" + form.openid.data + "and remember me is" + str(form.remember_me.data))
        return redirect('/index')
    return render_template("forms.html", title="sign in", form=form)