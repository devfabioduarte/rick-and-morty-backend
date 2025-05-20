from flask import jsonify
from src.services.characters_service import CharacterService
from src.models.characters_model import characters_output


class CharacterController():
    
    def __init__(self):
        self.character_service = CharacterService()
    
    def get_all_characters(self, page, per_page):       
        try:
            result = self.character_service.get_all_characters(page, per_page)
            
            return jsonify({
                "success" : True,
                "message" : "Characters retrieved successfully",
                "characters" : result["characters"],
                'pagination': {
                'total': result["total"],
                'pages': result["pages"],
                'current_page': result["current_page"],
                'per_page': result.get("per_page", 20)
                            }           
                }), 200
        except Exception as e:
            return jsonify({
                "success" : False,
                "message" : "Failed to retrieve characters",
                "error" : str(e),
                "data" : None
            }), 500

    def get_character_by_id(self, char_id):
        try:
            character = self.character_service.get_character_by_id(char_id)
            if character:
                return jsonify({
                    "success" : True,
                    "message" : "Character retrieved successfully",
                    "data" : character
                }), 200
            else:
                return jsonify({
                    "success" : False,
                    "message" : "Character not found",
                    "data" : None
                }), 404
        except Exception as e:
            return jsonify({
                "success" : False,
                "message" : "Error retrieving character",
                "error" : str(e),
                "data" : None
            }), 500
            