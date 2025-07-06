from flask import Flask
from src.models import db, ma
from config.settings import DATABASE_URI
from src.routes.characters_route import character_bp
from flask_cors import CORS

app = Flask(__name__)
# Configuração mais permissiva do CORS para desenvolvimento

CORS(app, 
     resources={r"/*": {
         "origins": ["http://localhost:5173"],
         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         "allow_headers": ["Content-Type", "Authorization"]
     }},
     supports_credentials=True)

# Additional CORS headers for all responses
@app.after_request
def after_request(response):
    # Allow specific origins instead of *
    response.headers.add('Access-Control-Allow-Credentials', 'true')
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


