from src.models import db

class CharacterEpisodes(db.Model):
    __tablename__ = 'character_episode'
    
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True) 
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)

    def __repr__(self):
        return f"<CharacterEpisodes {self.name}>"
    
    
