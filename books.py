from flask import Blueprint, request, json
from database import db
from models import Books

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route("/", methods=['GET'])
def get_books():
    books = Books.query.all()
    book_list = [book.to_dict() for book in books]
    return json.dumps(book_list)

@books_blueprint.route("/<id>", methods=['GET'])
def get_book(id):
    book = Books.query.get_or_404(id)
    return json.dumps(book.to_dict())

# Add other book-related routes here
# Example: route for adding a book
@books_blueprint.route("/", methods=['POST'])
def add_book():
    data = request.get_json()
    book = Books(data['name'], data['author'], data['year_published'], data['type'])
    db.session.add(book)
    db.session.commit()
    return {"add": "success"}

# Add more routes as needed

