from application import db
from datetime import datetime

class Artists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(96), nullable=False)
    individuals_in_group = db.Column(db.String(250))
    year_founded = db.Column(db.Integer)
    #songs = db.relationship("Songs", backref="author", lazy=True)
    song = db.relationship("Songs")

    def __repr__(self): #pragma: no cover
        return f"Artist('{self.artist_name}'', '{self.year_founded}')"

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(200), nullable=False)
    album_name = db.Column(db.String(200), nullable=False)
    trivia = db.Column(db.String(200))
    #artists_id = db.Column(db.Integer, db.ForeignKey("Artists.id"), nullable=False)
    artists_id = db.Column(db.Integer, db.ForeignKey(Artists.id))
    def __repr__(self): #pragma: no cover
        return f"Song('{self.song_name}')"
