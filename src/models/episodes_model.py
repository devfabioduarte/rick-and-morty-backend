from src.models import db, ma

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(50), nullable=False)
    episode = db.Column(db.String(50), nullable=False)

    characters = db.relationship('Character',secondary='character_episode', back_populates='episodes', uselist=True, lazy=True)

    def __repr__(self):
        return f"<Episodes {self.name}>"


class EpisodesOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()