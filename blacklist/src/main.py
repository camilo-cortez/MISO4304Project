from dotenv import load_dotenv
loaded = load_dotenv('.env.development')
import time
import os

from flask import Flask, jsonify
from src.blueprints.blacklist import blacklist_blueprint
from src.errors.errors import ApiError
from src.models.model import db

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

load_dotenv('.env.development')
load_dotenv('.env.test')

# Valida si esta presente para determinar si es productivo o test
if os.environ.get('MODE_TEST'):
    db_connection = 'sqlite:///blacklist.db'
    print("DB ENABLE FOR TEST")
else:
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')

    db_connection = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    #db_connection = 'postgresql://postgres:postgres@flask_db:5432/postgres'
    print("DB ENABLE FOR PRODUCTION")

app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
time.sleep(5)
db.create_all()

app.register_blueprint(blacklist_blueprint)

@app.errorhandler(ApiError)
def handle_exception(err):
    return jsonify({"msg": err.description}), err.code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3004)