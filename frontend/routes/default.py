from requests import get
from flask import render_template, session

from .. import app, BACKEND_URL
from ..utils import login_required


@app.get("/")
@login_required
def index():
    print(session)
    token = session.get("oauth2_token")
    headers = {"Authorization": f"Bearer {token}"}
    response = get(f"{BACKEND_URL}/users/me", headers=headers)
    user = response.json().get("current_user")
    return render_template("home.html", user=user)
