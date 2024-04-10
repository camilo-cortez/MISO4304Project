from .base_command  import  BaseCommand
from src.commands.validation import datetime_valid, is_valid_uuid
from src.errors import errors
#from src.clients.user_client import UserClient
from src.models.model import BlacklistSchema, BlacklistEntry, db

blacklist_schema = BlacklistSchema()

class CreateBlacklistEntry(BaseCommand):

    def __init__(self, json, token):
        self.routeId = json.get("routeId", "").strip()
        self.expireAt = json.get("expireAt", "").strip()
        self.token = token

    def execute(self):
        #user_id = UserClient(self.token).validate_user()
        if not is_valid_uuid(self.routeId):
            raise errors.BadRequest
        if (self.routeId is None or self.expireAt is None):
            raise errors.BadRequest()
        parsed_date = datetime_valid(self.expireAt)
        if parsed_date is None:
            raise errors.InvalidExpireDate("msg")
        
        blacklist_entry = BlacklistEntry(routeId=self.routeId, userId=user_id, expireAt=parsed_date)

        db.session.add(blacklist_entry)
        db.session.commit()
        return {'id': blacklist_entry.id, 'routeId': blacklist_entry.routeId, 'userId': blacklist_entry.userId, 'expireAt': blacklist_entry.expireAt, 'createdAt': blacklist_entry.createdAt}