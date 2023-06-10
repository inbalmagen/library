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
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    loan_date = db.Column(db.String(200))
    return_date = db.Column(db.String(200))

    def __init__(self, customer_id, book_id, loan_date, return_date):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def to_dict_with_names(result):
        loan = result[0]
        book = result[1]
        customer = result[2]
        return {
            'id': loan.id,
            'customer_id': loan.customer_id,
            'customer_name': customer.name,
            'book_id': loan.book_id,
            'name': book.name,
            'loan_date': loan.loan_date,
            'return_date': loan.return_date
        }

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'book_id': self.book_id,
            'loan_date': self.loan_date,
            'return_date': self.return_date
        }