import json
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite3'
app.config['SECRET_KEY'] = "random string"
CORS(app)

db = SQLAlchemy(app)

# Books Model
class Books(db.Model):
    id = db.Column('book_id', db.Integer, primary_key=True)
    ISBN = db.Column(db.String(100))
    book_name = db.Column(db.String(50))
    author_name = db.Column(db.String(50))
    publish_date = db.Column(db.String(200))
    publisher = db.Column(db.String(10))

    def __init__(self, ISBN, book_name, author_name, publisher, publish_date):
        self.ISBN = ISBN
        self.book_name = book_name
        self.author_name = author_name
        self.publish_date = publish_date
        self.publisher = publisher

    def to_dict(self):
        return {
            'id': self.id,
            'ISBN': self.ISBN,
            'book_name': self.book_name,
            'author_name': self.author_name,
            'publish_date': self.publish_date,
            'publisher': self.publisher
        }

# Students Model
class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    student_name = db.Column(db.String(50))
    adress = db.Column(db.String(50))
    phone = db.Column(db.String(200))
    identity_card = db.Column(db.String(10))

    def __init__(self, student_name, adress, phone, identity_card):
        self.student_name = student_name
        self.adress = adress
        self.phone = phone
        self.identity_card = identity_card

    def to_dict(self):
        return {
            'id': self.id,
            'student_name': self.student_name,
            'adress': self.adress,
            'phone': self.phone,
            'identity_card': self.identity_card
        }

# Loans Model
class Loans(db.Model):
    id = db.Column('loan_id', db.Integer, primary_key=True)
    CustID = db.Column(db.String(50))
    BookID = db.Column(db.String(50))
    Loandate = db.Column(db.String(200))
    Returndate = db.Column(db.String(10))

    def __init__(self, CustID, BookID, Loandate, Returndate):
        self.CustID = CustID
        self.BookID = BookID
        self.Loandate = Loandate
        self.Returndate = Returndate

    def to_dict(self):
        return {
            'id': self.id,
            'CustID': self.CustID,
            'BookID': self.BookID,
            'Loandate': self.Loandate,
            'Returndate': self.Returndate
        }
# CRUD Books
@app.route("/book")
def home():
    books_list = [book.to_dict() for book in Books.query.all()]
    json_data = json.dumps(books_list)
    return json_data

@app.route("/delBooks/<id>", methods=['DELETE'])
def del_book(id=-1):
    book = Books.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"delete": "success"}

@app.route("/updBooks/<id>", methods=['PUT'])
def upd_book(id=-1):
    book = Books.query.get(id)
    data = request.get_json()
    book.ISBN = data['ISBN']
    book.book_name = data['bookName']
    book.author_name = data['authorName']
    book.publish_date = data['publishDate']
    book.publisher = data['publisher']
    db.session.commit()
    return {"update": "success"}

@app.route('/newbook', methods=['POST'])
def new():
    data = request.get_json()
    ISBN = data['ISBN']
    book_name = data['bookName']
    author_name = data['authorName']
    publish_date = data['publishDate']
    publisher = data['publisher']

    new_book = Books(ISBN, book_name, author_name, publisher, publish_date)
    db.session.add(new_book)
    db.session.commit()
    return {"create": "success"}

# CRUD students
@app.route("/stu")
def home1():
    students_list = [student.to_dict() for student in Students.query.all()]
    json_data = json.dumps(students_list)
    return json_data

@app.route("/delStu/<id>", methods=['DELETE'])
def del_student(id=-1):
    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return {"delete": "success"}

@app.route("/updStu/<id>", methods=['PUT'])
def upd_student(id=-1):
    student = Students.query.get(id)
    data = request.get_json()
    student.student_name = data['studentName']
    student.adress = data['adress']
    student.phone = data['phone']
    student.identity_card = data['identityCard']
    db.session.commit()
    return {"update": "success"}

@app.route('/newStu', methods=['POST'])
def newS():
    data = request.get_json()
    student_name = data['studentName']
    adress = data['adress']
    phone = data['phone']
    identity_card = data['identityCard']

    new_student = Students(student_name, adress, phone, identity_card)
    db.session.add(new_student)
    db.session.commit()
    return {"create": "success"}

# CRUD loans
@app.route("/loan")
def home2():
    loans_list = [loan.to_dict() for loan in Loans.query.all()]
    json_data = json.dumps(loans_list)
    return json_data

@app.route("/delLoan/<id>", methods=['DELETE'])
def del_loan(id=-1):
    loan = Loans.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return {"delete": "success"}

@app.route("/updLoan/<id>", methods=['PUT'])
def upd_loan(id=-1):
    loan = Loans.query.get(id)
    data = request.get_json()
    loan.CustID = data['CustID']
    loan.BookID = data['BookID']
    loan.Loandate = data['Loandate']
    loan.Returndate = data['Returndate']
    db.session.commit()
    return {"update": "success"}

@app.route('/newLoan', methods=['POST'])
def newL():
    data = request.get_json()
    CustID = data['CustID']
    BookID = data['BookID']
    Loandate = data['Loandate']
    Returndate = data['Returndate']

    new_loan = Loans(CustID, BookID, Loandate, Returndate)
    db.session.add(new_loan)
    db.session.commit()
    return {"create": "success"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
