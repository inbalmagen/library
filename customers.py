from flask import Blueprint, request, json
from database import db
from models import Customers

customers_blueprint = Blueprint('customers', __name__)

@customers_blueprint.route("/", methods=['GET'])
def get_customers():
    customers = Customers.query.all()
    customer_list = [customer.to_dict() for customer in customers]
    return json.dumps(customer_list)

@customers_blueprint.route("/<id>", methods=['GET'])
def get_customer(id):
    customer = Customers.query.get_or_404(id)
    return json.dumps(customer.to_dict())

# Add other customer-related routes here
# Example: route for updating a customer
@customers_blueprint.route("/<id>", methods=['PUT'])
def update_customer(id):
    customer = Customers.query.get_or_404(id)
    data = request.get_json()
    customer.name = data['name']
    customer.city = data['city']
    customer.age = data['age']
    db.session.commit()
    return {"update": "success"}


@customers_blueprint.route("/", methods=['POST'])
def add_customer():
    data = request.get_json()
    customer = Customers(data['name'], data['city'], data['age'])
    db.session.add(customer)
    db.session.commit()
    return {"add": "success"}


@customers_blueprint.route("/<id>", methods=['DELETE'])
def delete_customer(id):
    customer = Customers.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return {"delete": "success"}



