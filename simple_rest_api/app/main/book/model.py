from .. import db

class Book(db.Model):
    """ book Model for storing book related details """
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    ISBN = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    published_date = db.Column(db.String(100),  nullable=False)
    isactive = db.Column(db.Boolean, nullable=False, default = True)
    created_on = db.Column(db.DateTime, nullable=True)
    updated_on = db.Column(db.DateTime, nullable=True) 


    @property
    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'author' : self.author,
            'ISBN' : self.ISBN,
            'year' : self.year,
            'published_date' : self.created_on.strftime("%d/%m/%Y, %H:%M:%S"),
            'isactive' : self.isactive,
            'created_on' : self.created_on.strftime("%d/%m/%Y, %H:%M:%S"),
            'updated_on' : self.updated_on.strftime("%d/%m/%Y, %H:%M:%S"),
        }