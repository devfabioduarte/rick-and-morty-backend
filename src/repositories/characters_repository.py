from src.models.characters_model import Character, db

class CharacterRepository:
    
    def get_all_characters(self,filter_params=None):
        try:
            characters = Character.query
            
            if filter_params:
                for key, value in filter_params.items():
                    if hasattr(Character, key):
                        if key == 'name':
                            characters = characters.filter(getattr(Character, key). ilike(f'%{value}%'))
                        else:
                            characters = characters.filter(getattr(Character, key) == value)
            return characters
        
        except Exception:
            db.session.rollback()
            raise
    
    def get_by_id(self, char_id):
        try: 
            character = db.session.get(Character, char_id)
            return character
        except Exception:
            db.session.rollback()
            raise
    