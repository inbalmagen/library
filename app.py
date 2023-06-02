import json
from flask import Flask, request
from flask_cors import CORS
from database import db
from models import Customers, Books, Loans
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SECRET_KEY'] = "random string"
CORS(app)
db.init_app(app)

# CRUD Books
@app.route("/books")
def get_books():
    books = Books.query.all()
    book_list = [book.to_dict() for book in books]
    return json.dumps(book_list)

@app.route("/books/<id>", methods=['GET'])
def get_book(id):
    book = Books.query.get_or_404(id)
    return json.dumps(book.to_dict())

@app.route("/books/<id>", methods=['PUT'])
def update_book(id):
    book = Books.query.get_or_404(id)
    data = request.get_json()
    book.name = data['name']
    book.author = data['author']
    book.year_published = data['year_published']
    book.type = data['type']
    db.session.commit()
    return {"update": "success"}

@app.route("/books/<id>", methods=['DELETE'])
def delete_book(id):
    book = Books.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"delete": "success"}

@app.route("/books", methods=['POST'])
def add_book():
    data = request.get_json()
    book = Books(data['name'], data['author'], data['year_published'], data['type'])
    db.session.add(book)
    db.session.commit()
    return {"add": "success"}

# CRUD Customers
@app.route("/customers")
def get_customers():
    customers = Customers.query.all()
    customer_list = [customer.to_dict() for customer in customers]
    return json.dumps(customer_list)

@app.route("/customers/<id>", methods=['GET'])
def get_customer(id):
    customer = Customers.query.get_or_404(id)
    return json.dumps(customer.to_dict())

@app.route("/customers/<id>", methods=['PUT'])
def update_customer(id):
    customer = Customers.query.get_or_404(id)
    data = request.get_json()
    customer.name = data['name']
    customer.city = data['city']
    customer.age = data['age']
    db.session.commit()
    return {"update": "success"}

@app.route("/customers/<id>", methods=['DELETE'])
def delete_customer(id):
    customer = Customers.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return {"delete": "success"}

@app.route("/customers", methods=['POST'])
def add_customer():
    data = request.get_json()
    customer = Customers(data['name'], data['city'], data['age'])
    db.session.add(customer)
    db.session.commit()
    return {"add": "success"}


# CRUD loans
@app.route("/loans")
def get_loans():
    loans_list = [loan.to_dict() for loan in Loans.query.all()]
    json_data = json.dumps(loans_list)
    return json_data

@app.route("/loans/<id>", methods=['GET'])
def get_loan(id):
    loan = Loans.query.get_or_404(id)
    return json.dumps(loan.to_dict())

@app.route("/loans/<id>", methods=['DELETE'])
def delete_loan(id):
    loan = Loans.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return {"delete": "success"}

@app.route("/loans/<id>", methods=['PUT'])
def update_loan(id):
    loan = Loans.query.get_or_404(id)
    data = request.get_json()
    loan.customer_id = data['customer_id']
    loan.book_id = data['book_id']
    loan.loan_date = data['loand_date']
    loan.return_date = data['return_date']
    db.session.commit()
    return {"update": "success"}

@app.route('/loans', methods=['POST'])
def create_loan():
    # data = request.get_json()
    # customer = Customers(data['name'], data['city'], data['age'])
    # db.session.add(customer)
    # db.session.commit()

    data = request.get_json()
    loan = Loans(data['customer_id'], data['book_id'], data['loan_date'], data['return_date'] )
    db.session.add(loan)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

app.run(debug=True)
