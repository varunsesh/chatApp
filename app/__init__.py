from flask import Flask
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "it's-restricted"
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    db.init_app(app) ##Initiliase sql database
    #Create login manager, lets code and flask login manager work together
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")

    
    return app



