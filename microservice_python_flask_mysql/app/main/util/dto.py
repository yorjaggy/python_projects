from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id_national' : fields.Integer(required=True, description='id_national'),
        'name' : fields.String(required=True, description='name'),
        'username' : fields.String(required=True, description='username'),
        'email' : fields.String(required=True, description='email'),
        'career' : fields.String(required=True, description='career'),
        'birthdate' : fields.DateTime(dt_format='rfc822'),
        'phonenumber' : fields.String(required=True, description='phonenumber'),
        'isactive' : fields.Boolean(description='is active or no, changes when is deleted'),
        'created_on' : fields.DateTime(dt_format='rfc822'),
        'updated_on' : fields.DateTime(dt_format='rfc822'),
    })
