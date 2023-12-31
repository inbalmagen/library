import json
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from database import db
from books import books_blueprint
from customers import customers_blueprint
from loans import loans_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SECRET_KEY'] = "random string"
CORS(app)
db.init_app(app)

# Register the blueprints
app.register_blueprint(books_blueprint, url_prefix='/books')
app.register_blueprint(customers_blueprint, url_prefix='/customers')
app.register_blueprint(loans_blueprint, url_prefix='/loans')

@app.route("/booksPage")
@app.route("/")
def get_books():
    # retrieve books from the database
    # ...
    return render_template("index1.html")

@app.route("/customersPage")
def get_customers():
    # retrieve customers from the database
    # ...
    return render_template("customers1.html")

@app.route("/loansPage")
def get_loans():
    # retrieve loans from the database
    # ...
    return render_template("loans1.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
