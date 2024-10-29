from functools import wraps

from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    def login_decorator(*args, **kwargs):
        if "token" not in session:
            return redirect(url_for("login"))
        return func(*args, **kwargs)

    return login_decorator
