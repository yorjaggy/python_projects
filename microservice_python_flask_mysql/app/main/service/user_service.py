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
    user = User.query.filter_by(id=id).first()

    if not user:
        return False, 'User does not exists. Please create it previos to update it.'
    else:
        user.id_national = data['id_national'],
        user.name = data['name'],
        user.username = data['username'],
        user.email = data['email'],
        user.career = data['career'],
        user.phonenumber = data['phonenumber'],
        user.birthdate = data['birthdate'],
        user.isactive = user.isactive if data.get('isactive') == None else data.get('isactive')
        user.updated_on = datetime.datetime.now()
        
        db.session.commit()

        return True, 'Successfully updated.'


def delete(id):
    user = User.query.filter_by(id=id, isactive = True).first()
    if not user:
        return False, 'User does not exist. Please create it previos to update it.'
    else:
        user.isactive = False
        user.updated_on = datetime.datetime.now()
        db.session.commit()
        return True, 'Successfully deleted.'

   