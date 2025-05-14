from src.models import db, ma

class CharacterEpisodes(db.Model):
    __tablename__ = 'character_episode'
    
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True) #importa a chave estrangeira
    episode = db.relationship("Episode", back_populates='episodes', uselist=True, lazy=True) #cria a relação

    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    character = db.relationship("Character", back_populates='episodes', uselist=True, lazy=True)

    def __repr__(self):
        return f"<CharacterEpisodes {self.name}>"
    
class CharacterEpisodesOutput(ma.Schema):
    episode_id = ma.Integer()
    character_id = ma.Integer()
    
    
