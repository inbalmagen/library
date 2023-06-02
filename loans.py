from flask import Blueprint, request, json
from database import db
from models import Loans

loans_blueprint = Blueprint('loans', __name__)

@loans_blueprint.route("/", methods=['GET'])
def get_loans():
    loans_list = [loan.to_dict() for loan in Loans.query.all()]
    json_data = json.dumps(loans_list)
    return json_data

@loans_blueprint.route("/<id>", methods=['GET'])
def get_loan(id):
    loan = Loans.query.get_or_404(id)
    return json.dumps(loan.to_dict())

# Add other loan-related routes here
# Example: route for creating a loan
@loans_blueprint.route('/', methods=['POST'])
def create_loan():
    data = request.get_json()
    loan = Loans(data['customer_id'], data['book_id'], data['loan_date'], data['return_date'])
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
    loan.loan_date = data['loan_date']
    loan.return_date = data['return_date']
    db.session.commit()
    return {"update": "success"}


