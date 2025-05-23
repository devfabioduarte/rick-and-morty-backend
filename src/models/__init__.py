from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from src.models.locations_model import Location
from src.models.episodes_model import Episode
from src.models.characters_episodes import CharacterEpisodes
from src.models.characters_model import Character