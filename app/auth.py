from flask import Blueprint, request, redirect, jsonify, render_template

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")




