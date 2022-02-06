from flask import Flask
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()

def create_app():
   
    app = Flask(__name__)
    app.config.from_object(Config)

    from .view import view

    app.register_blueprint(view, url_prefix="/")

    
    return app



