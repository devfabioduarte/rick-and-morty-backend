from src.repositories.characters_repository import CharacterRepository
from src.models.characters_model import character_output, characters_output
from werkzeug.exceptions import NotFound

class CharacterService:
    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self, page, name):
        per_page = 20

        filters = {
            'name' : name
            }

        characters = self.character_repository.get_all_characters(
        page, 
        per_page, 
        filters
        )
        
        data = characters_output.dump(characters.items)

        return {
            "characters" : data,
            "total_pages" : characters.pages,
            "total_characters" : characters.total, 
            "current_page" : page,
            "per_page" : per_page,
        }

    def get_character_by_id (self, char_id):
        character = self.character_repository.get_by_id(char_id)
        if character:
            return character_output.dump(character)
        raise NotFound(f"Character with id {char_id} not found")
    