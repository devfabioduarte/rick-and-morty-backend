from src.repositories.characters_repository import CharacterRepository
from src.models.characters_model import character_output, characters_output
from flask import request

class CharacterService:
    def __init__(self):
        self.repository = CharacterRepository()

    def get_all_characters(self, page, per_page):
        per_page = 20

        filters = {
            'name' : request.args.get('name', '').strip()
            }

        print("Filtros aplicados:", filters)

        characters = CharacterRepository.get_all_characters(self,
        page, 
        per_page, 
        filters
        )
        
        data = characters_output.dump(characters.items)
        return {
            "characters" : data,
            "data": characters.items,
            "total": characters.total,
            "pages": characters.pages,
            "current_page": characters.page
        }

    def get_character_by_id (self, char_id):
        character = self.repository.get_by_id(char_id)
        if character:
            return character_output.dump(character)
        return None
    