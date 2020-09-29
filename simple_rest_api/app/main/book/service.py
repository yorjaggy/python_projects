import logging
from datetime import datetime
from app.main import db
from .model import Book

def create(data):
    try:
        if data.get('ISBN') == None:
            return False, 'please provide a valid ISBN'
        
        book = Book.query.filter_by(ISBN=data.get('ISBN')).first()

        if not book:
            new_element = Book(
                name  = data.get('name'),
                author = data.get('author'),
                ISBN = data.get('ISBN'),
                year = data.get('year'),
                published_date = data.get('published_date'),
                isactive = True,
                created_on = datetime.now(),
                updated_on = datetime.now()
            )
          
            db.session.add(new_element)
            db.session.commit()

            return True, new_element.to_json
        else:
            return False, 'The book is already created, please try to recover your password'
    except Exception as e:
        logging.error(str(e))
        return False, 'Exception in service book creation.'




def request_all(page=None, perpage=None):
    try: 
        page = 1 if page == None else int(page)
        perpage = 20 if perpage == None else int(perpage)

        _books =  Book.query.filter_by(isactive=True).order_by(Book.created_on.desc()).paginate(page, perpage).items
        _books = [x.to_json for x in _books]
        return True, _books
    except Exception as e:
        logging.error(str(e))
        return False, 'Exception requesting all books.'


def request_by_id(id=None, isbn=None):
    try:
        if not id == None:
            _ret = Book.query.filter_by(id=id, isactive = True).first()
            return True, _ret.to_json
        elif not isbn == None:
            _ret = Book.query.filter_by(ISBN=isbn, isactive = True).first()
            return True, _ret.to_json
    except Exception as e:
        logging.error(str(e))
        return False, 'Exception requesting book by id.'


def update(id, data):
    try:
        _book = Book.query.filter_by(id=id).first()

        if not _book:
            return False, 'book does not exists. Please create it previous to update it.'
        
        _book.name = data['name']
        _book.author = data['author']
        _book.ISBN = data['ISBN']
        _book.year = data['year']
        _book.published_date = data['published_date']
        _book.isactive = data['isactive']
        _book.updated_on = datetime.now()
        
        db.session.commit()

        return True, 'Successfully updated.'
    except Exception as e:
        logging.error(str(e))
        return False, 'Exception updating book.'



def patch(id, data):
    try:
        _book = Book.query.filter_by(id=id).first()

        if not _book:
            return False, 'book does not exists. Please create it previous to update it.'
        
        _book.name = _book.name if  data.get('name') == None else data.get('name')
        _book.author = _book.author if  data.get('author') == None else data.get('author')
        _book.ISBN = _book.ISBN if  data.get('ISBN') == None else data.get('ISBN')
        _book.year = _book.year if  data.get('year') == None else data.get('year')
        _book.published_date = _book.published_date if  data.get('published_date') == None else data.get('published_date')
        _book.isactive = _book.isactive if  data.get('isactive') == None else data.get('isactive')
        _book.updated_on = datetime.now()
        
        db.session.commit()

        return True, 'Successfully updated.'
    except Exception as e:
        logging.error(str(e))
        return False, 'Exception patching book.'


def delete(id):
    try:
        _book = Book.query.filter_by(id=id, isactive = True).first()
        if not _book:
            return False, 'book does not exist. Please create it previos to update it.'
        else:
            _book.isactive = False
            _book.updated_on = datetime.now()
            db.session.commit()
            return True, 'Successfully deleted.'
    except Exception as e:
        logging.error(str(e))
        return False, 'Exception deleting book.'