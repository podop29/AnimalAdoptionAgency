from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

default_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png'

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50),
                     nullable = False)

    species = db.Column(db.String(30), nullable = False)

    photo_url = db.Column(db.String(), default = default_url)

    age = db.Column(db.Integer)

    notes = db.Column(db.String())

    avalible = db.Column(db.Boolean(),default = True)