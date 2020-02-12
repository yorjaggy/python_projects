from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import create, request_all, request_by_id

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        try:
            isOk, response = create(data=request.json)
            if isOk:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully created.',
                    'data' : response.to_json
                }

                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': response,
                }
                return response_object, 400
        except Exception as e:
            response_object = {
                    'status': 'fail',
                    'message': str(e),
            }
            return response_object, 500


    @api.doc('list_of_registered_users')
    #@admin_token_required
    #@api.marshal_list_with(_user, envelope='data')
    def get(self):
        try:
            email = request.args.get('email')
            id_national = request.args.get('id_national')
            username = request.args.get('username')

            if email != None:
                data = request_all(email,'email')
                if data:
                    data = data.to_json 
                else:
                    return {'status': 'fail', 'message':  'email id not found', 'data': ''}, 400
            
            if id_national != None:
                data = request_all(id_national,'id_national')
                if data:
                    data = data.to_json 
                else:
                    return {'status': 'fail', 'message':  'national id not found', 'data': ''}, 400
                
            if username != None:
                data = request_all(username,'username')
                if data:
                    data = data.to_json 
                else:
                    return {'status': 'fail', 'message': 'username not found', 'data': ''}, 400

            if email == None and username == None and id_national == None:
                response = request_all('', None)
                if response:
                    data = [x.to_json for x in response]
                else:
                    return {'status': 'fail', 'message': 'users not found', 'data': ''}, 400
                
            response_object = {
                        'status': 'success',
                        'message': '',
                        'data' : data
                    }
            return response_object, 200
        except Exception as e:
            response_object = {
                        'status': 'fail',
                        'message': 'It was not possible to retrieve information. {}'.format(str(e))
                    }
            return response_object, 400



@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    #@token_required
    @api.doc('get a user')
    #@api.marshal_with(_user)
    def get(self, id):
        try:
            """ Get a user given its identifier """
            user = request_by_id(id)
            
            if not user:
                response_object = {
                        'status': 'fail',
                        'message': 'It was not possible to retrieve User with id {}'.format(str(id))
                    }
                return response_object, 400
            else:
                response_object = {
                        'status': 'success',
                        'message': '',
                        'data' : user.to_json
                }
                return response_object, 201

        except Exception as e:
            response_object = {
                    'status': 'fail',
                    'message': str(e),
            }
            return response_object, 500


    @api.response(201, 'User successfully updated.')
    @api.doc('update user by id')
    @api.expect(_user, validate=True)
    def put(self, id):
        """ Update user by id"""
        try:
            data = request.json
            isOk, message = update(id=id, data=data)
            if not isOk:
                response_object = {
                        'status': 'fail',
                        'message': message,
                }
                return response_object, 401
            else:
                response_object = {
                        'status': 'success',
                        'message': message,
                }
                return response_object, 200
        except Exception as e:
            response_object = {
                        'status': 'fail',
                        'message': str(e),
                }
            return response_object, 500


    @api.response(201, 'User successfully deleted.')
    @api.doc('deletes a specific user by id')
    def delete(self, id):
        """ Delete a User by specific id """
        try:
            isOk, message = delete(id=id)
            if not isOk:
                response_object = {
                    'status': 'fail',
                    'message': message,
                }
                return response_object, 400
            else:
                response_object = {
                    'status': 'success',
                    'message': message,
                }
                return response_object, 200
        except Exception as e:
            response_object = {
                        'status': 'fail',
                        'message': str(e),
                }
            return response_object, 500