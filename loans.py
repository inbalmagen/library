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

# Add more routes as needed

