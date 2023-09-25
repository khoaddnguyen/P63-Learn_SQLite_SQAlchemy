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


# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all()