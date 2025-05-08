from flask import Blueprint
from src.controllers.characters_controller import CharacterController

character_bp = Blueprint("characters", __name__)
controller_characters = CharacterController()

# Rota para listar todos os personagens
@character_bp.route("/", methods=["GET"])
def get_all_characters():
    return controller_characters.get_all_characters()

# Rota para buscar um personagem pelo ID
@character_bp.route("/<int:char_id>", methods=["GET"])
def get_by_id(char_id):
    return controller_characters.get_character_by_id(char_id)

