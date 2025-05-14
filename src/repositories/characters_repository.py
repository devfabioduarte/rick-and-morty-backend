from src.models.characters_model import Character, db
from src.models.locations_model import Location
from src.models.episodes_model import Episode
from src.models.characters_episodes import CharacterEpisodes

class CharacterRepository:
    
    def get_all_characters(self,filters=None):
        try:
            query = Character.query
        
            if filters:
                if 'name' in filters and filters['name']:
                    name_filter = f'%{filters["name"]}%'
                    query = query.filter(Character.name.ilike(name_filter))
            
            return query
        
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
    