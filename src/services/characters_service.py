from src.repositories.characters_repository import CharacterRepository
from src.models.characters_model import character_output, characters_output

class CharacterService:
    def __init__(self):
        self.repository = CharacterRepository()

    def get_all_characters(self):
        characters = self.repository.get_all()
        return characters_output.dump(characters)
    
    def get_character_by_id (self, char_id):
        character = self.repository.get_by_id(char_id)
        if character:
            return character_output.dump(character)
        return None
    