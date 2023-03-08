from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from chatAI import chatAI
import os
import json

app = Flask(__name__)
app.secret_key = "1a42de19d467142abed0171c9cf4e87a"
file = open("users.json","r")
users = json.loads(file.read())['users']
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ORG = "org-2t6czCfX79NXhNdPvPzLZauZ"
chatGPT = chatAI(OPENAI_API_KEY, OPENAI_ORG)

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for("login"))
        return func(*args, **kwargs)

    return decorated_view


def is_auth():
    return bool(session.get("username"))


@app.route("/", methods=["GET", "POST"])
def login():
    if is_auth():
        return redirect(url_for("home"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for user in users:
            if user["username"] == username:
                if check_password_hash(user["password"], password):
                    session["username"] = username
                    return redirect(url_for("home"))
        flash("Invalid username or password.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/home")
@login_required
def home():
    return render_template("home.html")


@app.route("/api/messages/", methods=["POST"])
@login_required
def messages():
    message = request.form["message"]
    response = chatGPT.sendMessage(message)
    return response


if __name__ == "__main__":
    app.run(debug=True)
