from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
# import json

db = SQLAlchemy()
DB_NAME = "images.db"

def start():
    app = Flask(__name__)
    keyfile = open("session.key")
    key = keyfile.read()
    keyfile.close()
    app.config["SECRET_KEY"] = key
    app.config["SQLALCHEMY_DATABASE_URI"] =  f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .epmain import epmain

    app.register_blueprint(epmain, url_prefix="/")

    from .models import Image

    create_database(app)
    
    return app

def create_database(app):
    if(not path.exists("website/" + DB_NAME)):
        db.create_all(app=app)
        print("Created Database")
