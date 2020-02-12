import uuid
import datetime

from sqlalchemy import or_
from app.main import db
from app.main.model.user import User

def create(data):
    try:
        if  data.get('email') != None and data.get('id_national') != None and data.get('phonenumber') != None:
            user = User.query.filter(
                or_(
                    User.email==data.get('email'), 
                    User.id_national == data.get('id_national'), 
                    User.phonenumber == data.get('phonenumber'),
                )).first()

        if not user:
            new_user = User(
                id_national = data['id_national'],
                name = data['name'],
                username = data['username'],
                email = data['email'],
                career = data['career'],
                phonenumber = data['phonenumber'],
                birthdate = data['birthdate'],
                isactive = True,
                created_on = datetime.datetime.now(),
                updated_on = datetime.datetime.now()
            )
            
            db.session.add(new_user)
            db.session.commit()

            return True, new_user
        else:
            return False, 'The user is already created, please try to recover your password'
    except Exception as e:
        #return False, 'Error in service. {}'.format(str(e))
        return False, str(e)


def request_all(id, param):
    if param != None:
        switcher={
            'email': User.query.filter_by(email=id, isactive = True).first(),
            'id_national': User.query.filter_by(id_national=id, isactive = True).first(),
            'username' : User.query.filter_by(username=id, isactive = True).first()
            }
        return switcher.get(param)
    else:
        return User.query.filter_by(isactive=True).all()

def request_by_id(id):
    return User.query.filter_by(id=id, isactive = True).first()

def update(id, data):
    return False, "Pending implementation"


def delete(id):
    return False, "Pending implementation"
   