from flask import Flask


app = Flask(__name__)
BACKEND_URL = "http://127.0.0.1:8134"
SECRET_KEY = "test"
app.config["SECRET_KEY"] = SECRET_KEY

from . import routes
