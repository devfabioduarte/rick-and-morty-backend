from src.repositories.characters_repository import CharacterRepository
from src.models.characters_model import character_output, characters_output
from flask import request

class CharacterService:
    def __init__(self):
        self.repository = CharacterRepository()

    def get_all_characters(self, page=1, per_page=20, filters=None):
        
        query = CharacterRepository.get_all_characters(filters)
        paginated = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            "data": paginated.items,
            "total": paginated.total,
            "pages": paginated.pages,
            "current_page": paginated.page
        }

        
    
    def get_character_by_id (self, char_id):
        character = self.repository.get_by_id(char_id)
        if character:
            return character_output.dump(character)
        return None
    