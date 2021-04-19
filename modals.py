from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/flask_test"
app.config['SQLALCHEMY_BINDS'] = {'one':"mysql+pymysql://root:password@localhost/flask_test/customer_title",
    'two':"mysql+pymysql://root:password@localhost/flask_test/customer_name",
'three' :"mysql+pymysql://root:password@localhost/flask_test/customer_contact",
'four': "mysql+pymysql://root:password@localhost/flask_test/post_code",
'five':"mysql+pymysql://root:password@localhost/flask_test/city",
'six':"mysql+pymysql://root:password@localhost/flask_test/customer_login"}

db = SQLAlchemy(app)

class Title(db.model):



class User(db.Model):
    __tablename__ = 'Customer_Login'
    id = db.Column(db.Integer, unique=True,primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.Integer(8), nullable=False)
    contact_number = db.Column(db.Integer(30), nullable=False)
    Address =  db.Column(db.String(50), nullable=False)
    post_code = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

#class Customer_name(db.Model):
    __tablename__ =




#class Customer_contact(db.model):
    #__tablename__ =
