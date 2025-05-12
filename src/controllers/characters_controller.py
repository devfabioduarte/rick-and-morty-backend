from flask import jsonify, request
from src.services.characters_service import CharacterService
from src.models.characters_model import characters_output


class CharacterController():
    
    def __init__(self):
        self.character_service = CharacterService()
        
    def get_all_characters(self):       
        try:
            page = request.args.get('page',1, type=int)
            per_page = 20

            filters = {
                'name' : request.args.get('name'.strip().lower())
            }

            filters = {k: v for k, v in filters.items() if v is not None}

            result = self.character_service.get_all_characters(page, per_page, filters)

            data = characters_output.dump(result['data'])

            return jsonify({
                "success" : True,
                "message" : "Characters retrieved successfully",
                "characters" : data,
                'pagination': {
                'total': result['total'],
                'pages': result['pages'],
                'current_page': result['current_page'],
                'per_page': per_page
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
            