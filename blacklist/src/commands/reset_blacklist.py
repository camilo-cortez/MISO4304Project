from flask import jsonify
from .base_command  import  BaseCommand
from src.models.model import BlacklistSchema, BlacklistEntry, db

blacklist_schema = BlacklistSchema()

class ResetBlacklist(BaseCommand):

    def execute(self):
        db.session.query(BlacklistEntry).delete()
        db.session.commit()
        return {"msg": "Todos los datos fueron eliminados"}