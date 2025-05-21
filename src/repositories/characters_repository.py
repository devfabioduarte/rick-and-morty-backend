from src.models.characters_model import Character, db

class CharacterRepository:
    
    def get_all_characters(self, page, per_page, name=None):
        try:
            query = Character.query
            if name:
                 query = query.filter(Character.name.ilike(f'%{name}%'))
            
            total = query.count()
            pagination = query.offset((page - 1) * per_page).limit(per_page).all()
            return pagination, total
        
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
    