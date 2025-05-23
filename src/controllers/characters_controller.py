from src.services.characters_service import CharacterService
from src.utils.api_response import ApiResponse
from werkzeug.exceptions import NotFound

class CharacterController():
    
    def __init__(self):
        self.character_service = CharacterService()
        self.api_response = ApiResponse()
    
    def get_all_characters(self, page, name):       
        try:
            result = self.character_service.get_all_characters(page, name)

            return self.api_response.api_reponse(True,
                                    result,
                                    "Characters retrieved successfully",
                                    status_code=200)
        except Exception as e:
            return self.api_response.api_reponse(False,
                                    result,
                                    "Error retrieving characters",
                                    status_code=500)

    def get_character_by_id(self, char_id):
        try:
            character = self.character_service.get_character_by_id(char_id)
            
            return self.api_response.api_reponse( True,
                                    character,
                                    "Characters retrieved successfully",
                                    status_code=200)
        except NotFound as e:
            return self.api_response.api_reponse(False, None, str(e), status_code=404)
        
        except Exception as e:
            return self.api_response.api_reponse(False,
                                    None,
                                    f"Error retrieving character with id {char_id}",
                                    status_code=500)
            