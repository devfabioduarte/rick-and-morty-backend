from flask import Blueprint
from src.controllers.characters_controller import CharacterController
from flask import request

character_bp = Blueprint("characters", __name__)
controller_characters = CharacterController()

@character_bp.route("/", methods=["GET"])
def get_all_characters():
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    name = request.args.get('name', '', type=str).strip()
    
    return controller_characters.get_all_characters(page, per_page, name)

@character_bp.route("/<int:char_id>", methods=["GET"])
def get_by_id(char_id):
    return controller_characters.get_character_by_id(char_id)