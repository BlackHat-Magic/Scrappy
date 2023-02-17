from . import db
from sqlalchemy.sql import func
import uuid

class Image(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    siteid = db.Column(db.String(255))
    url = db.Column(db.String(16383))
    tags = db.Column(db.PickleType)
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)