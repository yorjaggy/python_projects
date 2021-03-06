import datetime
from .. config import key
from .. import db, flask_bcrypt

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_national = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100),unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    career = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    phonenumber = db.Column(db.String(20),unique=True)
    created_on = db.Column(db.DateTime, nullable=True)
    updated_on = db.Column(db.DateTime, nullable=True)
    isactive = db.Column(db.Boolean, nullable=False, default = True)

    @property
    def to_json(self):
        return {
            "id" : self.id,
            "id_national" : self.id_national,
            "username" : self.username,
            "name" : self.name,
            "email" : self.email,
            "career" : self.career,
            "birthdate" : self.birthdate,
            "phonenumber" : self.phonenumber,
            "created_on" : self.created_on.strftime("%d/%m/%Y, %H:%M:%S"),
            "updated_on" : self.updated_on.strftime("%d/%m/%Y, %H:%M:%S"),
            "isactive" : self.isactive
        }