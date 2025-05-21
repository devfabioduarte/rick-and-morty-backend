from src.services.characters_service import CharacterService
from src.utils.api_response import ApiResponse

class CharacterController():
    
    def __init__(self):
        self.character_service = CharacterService()
        self.api_response = ApiResponse()
    
    def get_all_characters(self, page, per_page, name):       
        try:
            result = self.character_service.get_all_characters(page, per_page, name)

            return self.api_response.api_reponse(True,
                                    result,
                                    "Characters retrieved successfully",
                                    )
        except Exception as e:
            return self.api_response.api_reponse(False,
                                    result,
                                    "Error retrieving characters",
                                    )

    def get_character_by_id(self, char_id):
        try:
            character = self.character_service.get_character_by_id(char_id)
            
            return self.api_response.api_reponse( True,
                                    character,
                                    "Characters retrieved successfully",
                                    )
        except Exception as e:
            return self.api_response.api_reponse(errors=str(e))
            