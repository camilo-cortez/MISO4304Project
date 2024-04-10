from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import uuid
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()

class BlacklistEntry(db.Model):
    __tablename__ = 'blacklistentry'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    routeId = db.Column(db.String(36))
    userId = db.Column(db.String(36))
    expireAt = db.Column(db.DateTime)
    createdAt = db.Column(db.DateTime, default=datetime.now())

    

class BlacklistSchema(SQLAlchemyAutoSchema): 
    class Meta:
        model = BlacklistEntry
        load_instance = True