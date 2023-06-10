import select
from flask import Blueprint, request, json
from database import db
from models import Loans
from customers import Customers
from books import Books
from datetime import datetime, timedelta
from sqlalchemy import select
from sqlalchemy.orm import aliased

loans_blueprint = Blueprint('loans', __name__)

@loans_blueprint.route("/", methods=['GET'])
def get_loans():
    
    query = db.session.query(Loans, Books, Customers).join(Books).join(Customers)
    # LoansAlias = aliased(Loans)
    # BooksAlias = aliased(Books)
    # CustomersAlias = aliased(Customers)

    # Construct the query with left joins
    # query = select(Loans, Books, Customers).\
    #     select_from(LoansAlias).\
    #     outerjoin(BooksAlias, LoansAlias.book_id == BooksAlias.id).\
    #     outerjoin(CustomersAlias, LoansAlias.customer_id == CustomersAlias.id)
    loans = query.all()
    loans_list = [Loans.to_dict_with_names(loan) for loan in loans]
    json_data = json.dumps(loans_list)
    return json_data

@loans_blueprint.route("/<id>", methods=['GET'])
def get_loan(id):
    loan = Loans.query.get_or_404(id)
    return json.dumps(loan.to_dict())

# Add other loan-related routes 
# Creating a loan
@loans_blueprint.route('/', methods=['POST'])
def create_loan():
    data = request.get_json()
    customer_id = data.get('customer_id')
    book_id = data.get('book_id')
    customer = Customers.query.get(data['customer_id'])
    book = Books.query.get(data['book_id'])  

    # Set loan_date as today's date
    loan_date = datetime.now().strftime('%Y-%m-%d')


    # Check if customer exists
    if not customer:
        return {'error': 'Customer not found.'}, 404 

     # Check if book exists
    if not book:
        return {'error': 'Book not found.'}, 404
    
     # Calculate return date based on loan type
    if book.type == '1':
        return_date = datetime.strptime(loan_date, '%Y-%m-%d') + timedelta(days=10)
    elif book.type == '2':
        return_date = datetime.strptime(loan_date, '%Y-%m-%d') + timedelta(days=5)
    elif book.type == '3':
        return_date = datetime.strptime(loan_date, '%Y-%m-%d') + timedelta(days=2)
    else:
        return {'error': 'Invalid Book type.'}, 400
                  

    loan = Loans(data['customer_id'], data['book_id'], loan_date, return_date.strftime('%Y-%m-%d'))
    db.session.add(loan)
    db.session.commit()
    return {"add": "success"}

@loans_blueprint.route("/<id>", methods=['DELETE'])
def delete_loan(id):
    loan = Loans.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return {"delete": "success"}

@loans_blueprint.route("/<id>", methods=['PUT'])
def update_loan(id):
    loan = Loans.query.get_or_404(id)
    data = request.get_json()
    loan.customer_id = data['customer_id']
    loan.book_id = data['book_id']
    db.session.commit()
    return {"update": "success"}


