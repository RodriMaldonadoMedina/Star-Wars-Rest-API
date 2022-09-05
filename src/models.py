from flask_sqlalchemy import SQLAlchemy
from eralchemy import draw_er

db = SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(30), unique=False, nullable=False)
    suscription = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,
            "user_last_name": self.last_name,
            "email": self.email,
            "is_active": self.is_active,
            "suscription": self.suscription
            # do not serialize the password, its a security breach
        }
    

class Personaje(db.Model):
    __tablename__='personaje'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    birth_date = db.Column(db.String(15), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    height = db.Column(db.String(6), nullable=True)
    eye_color = db.Column(db.String(15), nullable=True)
    skin_color = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        return '<Personaje %r>' % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color
        }

class Planeta(db.Model):
    __tablename__='planeta'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    diametro = db.Column(db.String(15), nullable=True)
    clima = db.Column(db.String(10), nullable=True)
    gravedad = db.Column(db.String(6), nullable=True)
    habitantes = db.Column(db.String(15), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "diametro": self.diametro,
            "clima": self.clima,
            "gravedad": self.gravedad,
            "habitantes": self.habitantes
        }

class Nave(db.Model):
    __tablename__='nave'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    costo_creditos = db.Column(db.Integer, nullable=False)
    pasajeros = db.Column(db.Integer, nullable=True)
    capacidad_carga = db.Column(db.Integer, nullable=True)
    clase = db.Column(db.String(15), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "costo_creditos": self.costo_creditos,
            "pasajeros": self.pasajeros,
            "capacidad_carga": self.capacidad_carga,
            "clase": self.clase
        }

class Personaje_Favorito(db.Model):
    __tablename__='personaje_favorito'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    personaje_id = db.Column(db.Integer, db.ForeignKey(Personaje.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
        }

class Planeta_Favorito(db.Model):
    __tablename__='planeta_favorito'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    planeta_id = db.Column(db.Integer, db.ForeignKey(Planeta.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planeta_id": self.planeta_id,
        }

class Nave_Favorito(db.Model):
    __tablename__='nave_favorito'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    nave_id = db.Column(db.Integer, db.ForeignKey(Nave.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nave_id": self.nave_id,
        }

## Draw from SQLAlchemy base
draw_er(db.Model, 'diagram.png')