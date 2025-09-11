from app import db

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    movies = db.relationship("Movie", backref="director", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "name": self.name}
