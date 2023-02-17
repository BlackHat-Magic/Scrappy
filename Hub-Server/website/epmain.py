from flask import Blueprint, Flask, render_template, redirect, url_for, request, session, flash, jsonify
from .models import Image
from . import db
import json

epmain = Blueprint("epmain", __name__)

@epmain.route("/")
def home():
    return(render_template("index.html", title="Home"))

@epmain.route("/add-gelbooru-image", methods=["POST"])
def addImage():
    data = json.loads(request.data)
    siteid = data["siteid"]
    url = data["url"]
    tags = data["tags"]
    height = data["height"]
    width = data["width"]

    with open(f"images/{'{:07d}'.format(siteid)}.jpg", "wb") as handler:
        handler.write(img)

    new_image = Image(
        siteid = siteid,
        url = url,
        tags = tags,
        height = height,
        width = width
    )
    db.session.add(new_image)
    db.session.commit
    return("fuck")