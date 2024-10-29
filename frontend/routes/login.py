from requests import get, post
from flask import render_template, session, redirect, url_for

from .. import app, BACKEND_URL
from ..forms import LoginForm


@app.get("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.post("/login")
def login_post():
    form = LoginForm()
    if form.validate_on_submit():
        data = {"username": form.nickname.data, "password": form.password.data}
        response = post(f"{BACKEND_URL}/token", data=data)

        if response.status_code == 200:
            session["oauth2_token"] = response.json().get("access_token")
        else:
            return "Login Error!", 400
    return redirect(url_for("index"))
