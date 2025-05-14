from src.models import db, ma

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    dimension = db.Column(db.String(50), nullable=False)

    native = db.relationship('Character',foreign_keys="Character.origin_id", back_populates='origin', uselist=True, lazy=True)
    residents = db.relationship('Character',foreign_keys="Character.location_id", back_populates='location', uselist=True, lazy=True)

    def __repr__(self):
        return f"<Locations {self.name}>"


class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()