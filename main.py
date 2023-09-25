# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# to view table, download and open DB Browser for SQLite
# Create/open .db file
# db = sqlite3.connect("books-collection.db")

# Create a cursor/mouse/pointer
# cursor = db.cursor()

# Create a table named "books". Comment out once the table is created.
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# create the app
app = Flask(__name__)

# crate database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all()

# Create a record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()