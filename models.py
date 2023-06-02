from flask_sqlalchemy import SQLAlchemy
from database import db
# Books Model
class Books(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    author = db.Column(db.String(50))
    year_published = db.Column(db.String(200))
    type = db.Column(db.String(10))

    def __init__(self, name, author, year_published, type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.type = type

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'year_published': self.year_published,
            'type': self.type
        }
    

# Customers Model
class Customers(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    age = db.Column(db.String(200))

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'age': self.age,
        }
    

# Loans Model
class Loans(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    # customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    # book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    customer_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    loandate = db.Column(db.String(200))
    returndate = db.Column(db.String(10))

    def __init__(self, customer_id, book_id, loandate, returndate):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loandate = loandate
        self.returndate = returndate

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'book_id': self.book_id,
            'loan_date': self.loandate,
            'return_date': self.returndate
        }