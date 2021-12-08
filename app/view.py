from flask import Blueprint, request, redirect, jsonify, render_template
from app.forms import LoginForm

view = Blueprint("view", __name__)

@view.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@view.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign in", form=form)

