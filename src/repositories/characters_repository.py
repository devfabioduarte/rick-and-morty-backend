from src.models.characters_model import Character

class CharacterRepository:
    def get_all(self):
        return Character.query.all()
    
    def get_by_id(self, char_id):
        return Character.query.get(char_id)
    