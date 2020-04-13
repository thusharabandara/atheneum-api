# import relevant libraries
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# initialize app
app = Flask(__name__)
# create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atheneum.db'
# initialize db
db = SQLAlchemy(app)

# create table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    authors = db.Column(db.String(250), nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    isbn13 = db.Column(db.String(100), nullable=False)
    lang_code = db.Column(db.String(50), nullable=False)
    num_pages = db.Column(db.Integer, nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False)
    publisher = db.Column(db.String(250), nullable=False)

# construct dictionary
def dict_factory(cursor, row):
    # create an empty dictionary
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    # return resultant dictionary
    return dict


# establish the database connectivity
def connect_athenaeum_db():
    # initialize db connection
    con = sqlite3.connect('atheneum.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    # return cursor
    return cur


# map urls to functions (routing)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# handle page/server not found error
@app.errorhandler(404)
def page_server_not_found(ex):
    return render_template('404.html')

# return all books stored in the db
@app.route('/api/v1.0/resources/books/all', methods=['GET'])
def api_all_books():
    # establish the db connectivity by calling method
    cur = connect_athenaeum_db()
    # execute query to fetch all book details
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    # return the resultant book info in json format
    return jsonify(all_books)

# filter books according to the api request
@app.route('/api/v1.0/resources/books', methods=['GET'])
def api_filter_books():
    # get all arguments from the api request
    query_paras = request.args

    # extract values from args
    title = query_paras.get('title') 
    authors = query_paras.get('authors')
    isbn = query_paras.get('isbn')
    lang_code = query_paras.get('lang_code')
    num_pages = query_paras.get('num_pages')
    # min_pages = query_paras.get('min_pages')
    # max_pages = query_paras.get('max_pages')
    publication_date = query_paras.get('publication_date')
    publisher = query_paras.get('publisher')

    # initialize the master query
    master_query = "SELECT * FROM books WHERE"
    # initialize a list to store requested values 
    filter_values = []

    # if title exists
    if title:
        # contact with the master query
        master_query += ' title=? AND'
        # append title
        filter_values.append(title)
    # if authors exist
    if authors:
        # contact with the master query
        master_query += ' authors=? AND'
        # append authors
        filter_values.append(authors)
    # if isbn exists
    if isbn:
        # contact with the master query
        master_query += ' isbn=? AND'
        # append isbn
        filter_values.append(isbn)
    # if lang_code exists
    if lang_code:
        # contact with the master query
        master_query += ' lang_code=? AND'
        # append lang_code
        filter_values.append(lang_code)
    # if num_pages exists
    if num_pages:
        # contact with the master query
        master_query += ' num_pages=? AND'
        # append num_pages
        filter_values.append(num_pages)
    # if publication_date exists
    if publication_date:
        # contact with the master query
        master_query += ' publication_date=? AND'
        # append publication_date
        filter_values.append(publication_date)
    # if publisher exists
    if publisher:
        # contact with the master query
        master_query += ' publisher=? AND'
        # append publisher
        filter_values.append(publisher)
    # if there is no such requested value
    if not (title or authors or isbn or lang_code or num_pages or publication_date or publisher):
        return page_server_not_found(404)

    # complete the master_query
    master_query = master_query[:-4] + ';'

    # establish the db connectivity by calling method
    cur = connect_athenaeum_db()
    # execute master_query to fetch books corresponds to filter_values if any
    filtered_result = cur.execute(master_query, filter_values).fetchall()

    # return filtered_result in json format
    return jsonify(filtered_result)

# run server
if __name__ == "__main__":
    app.run(debug=True)