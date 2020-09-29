from flask_restplus import Namespace, fields

class BookDto:
    api = Namespace('book', description='book related operations')
    book = api.model('book', {
        'id': fields.Integer(description='book Identifier'),
        'name' : fields.String(required=True, description='name'),
        'author' : fields.String(required=True, description='name'),
        'ISBN' : fields.String(required=True, description='name'),
        'year' : fields.Integer(description='year loaned'),
        'published_date' : fields.DateTime(dt_format='rfc822'),
        'isactive' : fields.Boolean(description='is active or no, changes when is deleted'),
        'created_on' : fields.DateTime(dt_format='rfc822'),
        'updated_on' : fields.DateTime(dt_format='rfc822')
    })