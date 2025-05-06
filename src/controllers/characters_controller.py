from flask import jsonify, request
from src.services.characters_service import CharacterService

character_service = CharacterService()

class CharacterController():
    @staticmethod
    def get_all_characters():
        characters = character_service.get_all_characters()
        return jsonify(characters), 200

    @staticmethod
    def get_character_by_id(char_id):
        character = character_service.get_character_by_id(char_id)
        if character:
            return jsonify(character), 200
        return jsonify({'message' : 'Character not found'}), 404
