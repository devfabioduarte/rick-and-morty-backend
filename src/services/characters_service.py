from src.repositories.characters_repository import CharacterRepository
from src.models.characters_model import character_output, characters_output
from werkzeug.exceptions import NotFound

class CharacterService:
    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self, page, name):
        per_page = 20
        pagination, total = self.character_repository.get_all_characters(page, per_page, name)
        data = characters_output.dump(pagination)
        total_pages = (total + per_page - 1) // per_page
        
        return {
            "characters" : data,
            "total_pages" : total_pages,
            "total_characters" : total, 
            "current_page" : page,
            "per_page" : per_page,
        }

    def get_character_by_id (self, char_id):
        character = self.character_repository.get_by_id(char_id)
        if not character:
            raise NotFound(f"Character with id {char_id} not found")
        return character_output.dump(character)