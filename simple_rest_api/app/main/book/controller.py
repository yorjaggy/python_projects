import logging, os
from flask import request
from flask_restplus import Resource

from ..util.dto import BookDto
from .service import create, request_all, request_by_id, update, patch, delete

api = BookDto.api
_Book = BookDto.book

@api.route('/')
class Book(Resource):
    @api.response(201, 'Book successfully created.')
    @api.doc('create a new Book')
    @api.expect(_Book, validate=True)
    def post(self):
        """Creates a new Book """
        try:
            isOk, response = create(data=request.json)
            
            response_object = {
                    'status'    : 'fail'    if not isOk else 'success',
                    'message'   : response  if not isOk else '',
                    'data'      : ''        if not isOk else response
            }
            return response_object, 201 if isOk else 400

        except Exception as e:
            response_object = {
                    'status'    : 'fail',
                    'message'   : 'Exception in book creation',
                    'data'      : ''
            }
            return response_object, 500


    @api.doc('Request book list paginated')
    def get(self):
        try:
            page = request.args.get('page')
            perpage = request.args.get('perpage')
            isbn = request.args.get('isbn')

            if not isbn == None:
                isOk, response = request_by_id(isbn=isbn)
            else:
                isOk, response = request_all(page, perpage)
            
            response_object = {
                    'status'    : 'fail'    if not isOk else 'success',
                    'message'   : response  if not isOk else '',
                    'data'      : ''        if not isOk else response
            }
            return response_object, 200 if isOk else 400
        except Exception as e:
            logging.error(str(e))
            response_object = {
                        'status': 'fail',
                        'message': 'It was not possible to retrieve information.'
                    }
            return response_object, 400



@api.route('/<id>')
@api.param('id', 'The Book identifier')
@api.response(404, 'Book not found.')
class BookById(Resource):
    @api.doc('get a Book')
    #@api.marshal_with(_Book)
    def get(self, id=None):
        try:
            """ Get a Book given its identifier or ISBN"""
            isbn = request.args.get('isbn')
            isOk, response = request_by_id(id=id, isbn=isbn)
            
            response_object = {
                    'status'    : 'fail'    if not isOk else 'success',
                    'message'   : response  if not isOk else '',
                    'data'      : ''        if not isOk else response
            }

            return response_object, 200 if isOk else 400
        except Exception as e:
            logging.error(str(e))
            response_object = {
                        'status': 'fail',
                        'message': 'It was not possible to retrieve information.'
                    }
            return response_object, 400



    @api.response(201, 'Book successfully updated.')
    @api.doc('update Book by id')
    @api.expect(_Book, validate=True)
    def put(self, id=None):
        """ Update Book by id"""
        try:
            data = request.json
            isOk, response = update(id=id, data=data)
            
            response_object = {
                    'status'    : 'fail'    if not isOk else 'success',
                    'message'   : response  if not isOk else '',
                    'data'      : ''        if not isOk else response
            }

            return response_object, 200 if isOk else 400
        except Exception as e:
            logging.error(str(e))
            response_object = {
                        'status': 'fail',
                        'message': 'It was not possible to retrieve information.'
                    }
            return response_object, 500



    @api.response(201, 'Book successfully patched.')
    @api.doc('update Book by id')
    def patch(self, id):
        """ Update Book by id"""
        try:
            data = request.json
            isOk, response = patch(id=id, data=data)
            
            response_object = {
                    'status'    : 'fail'    if not isOk else 'success',
                    'message'   : response  if not isOk else '',
                    'data'      : ''        if not isOk else response
            }

            return response_object, 200 if isOk else 400
        except Exception as e:
            logging.error(str(e))
            response_object = {
                        'status': 'fail',
                        'message': 'It was not possible to retrieve information.'
                    }
            return response_object, 500



    @api.response(201, 'Book successfully deleted.')
    @api.doc('deletes a specific Book by id')
    def delete(self, id):
        """ Delete a Book by specific id """
        try:
            isOk, response = delete(id=id)
            response_object = {
                    'status'    : 'fail'    if not isOk else 'success',
                    'message'   : response  if not isOk else '',
                    'data'      : ''        if not isOk else response
            }

            return response_object, 200 if isOk else 400
        except Exception as e:
            logging.error(str(e))
            response_object = {
                        'status': 'fail',
                        'message': 'It was not possible to retrieve information.'
                    }
            return response_object, 500
