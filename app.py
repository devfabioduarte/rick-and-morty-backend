from flask import Flask
from src.models import db, ma
from config.settings import DATABASE_URI
from src.routes.characters_route import character_bp
from flask_cors import CORS
from src.utils.constants import ENVIRONMENTS
import os
from dotenv import load_dotenv
load_dotenv

app = Flask(__name__)

#parte do cors

front_end_url = os.getenv("FRONT_END_URL")
environment = os.getenv("ENVIRONMENT")

origins_map = {
    ENVIRONMENTS.LOCAL.value: ["*"],
    ENVIRONMENTS.PRODUCTION.value: [front_end_url]
}

allowed_origins = origins_map.get(environment, origins_map[ENVIRONMENTS.PRODUCTION.value])

print(allowed_origins)

CORS(app, resources={r"/*": {"origins": allowed_origins}})

def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', front_end_url)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

app.register_blueprint(character_bp, url_prefix='/characters')

if __name__ == "__main__":
    app.run(debug=True)


