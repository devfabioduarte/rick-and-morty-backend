from src.repositories.characters_repository import CharacterRepository
from src.models.characters_model import character_output, characters_output
from flask import request

class CharacterService:
    def __init__(self):
        self.repository = CharacterRepository()

    def get_all_characters(self):
        page = request.args.get('page',1, type=int)
        per_page = 20

        filters = {
            'name' : request.args.get('name', '').strip()
            }

        filters = {k: v for k, v in filters.items() if v is not None}

        print("Filtros aplicados:", filters)

        query = CharacterRepository.get_all_characters(self, filters)
        paginated = query.paginate(page=page, per_page=per_page, error_out=False)
        

        data = characters_output.dump(paginated.items)
        return {
            "characters" : data,
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
    