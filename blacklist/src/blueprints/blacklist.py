from flask import jsonify, request, Blueprint
from src.commands.create_blacklist_entry import CreateBlacklistEntry
#from src.commands.get_blacklist import GetBlacklist
from src.commands.reset_blacklist import ResetBlacklist
from src.commands.ping import Ping

blacklist_blueprint  = Blueprint('blacklist', __name__)

@blacklist_blueprint.route('/blacklist', methods = ['POST'])
def create_post():
    json = request.get_json()
    token = request.headers.get('Authorization', '').strip()
    result = CreateBlacklistEntry(json, token).execute()
    return jsonify(result), 201

@blacklist_blueprint.route('/blacklist/ping', methods=['GET'])
def ping():
    response = Ping().execute()
    return response, 200

@blacklist_blueprint.route('/blacklist', methods=['GET'])
def get_blacklist():
    offer_id = request.args.get("offerId", '')
    token = request.headers.get('Authorization', '').strip()
    response = ""#GetBlacklist(offer_id=offer_id, token=token).execute()
    return jsonify(response), 200

@blacklist_blueprint.route('/blacklist/reset', methods=['POST'])
def reset_blacklist():
    response = ResetBlacklist().execute()
    return jsonify(response), 200