from src.models.characters_model import Character, db
from flask import jsonify

class CharacterRepository:
    
    def get_all(self):
        return db.session.query(Character)
    
    def get_by_id(self, char_id):
        return db.session.get(Character, char_id)
    