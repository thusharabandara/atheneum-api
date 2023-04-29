# Athenium API

Athenium API is a Flask-based web application that provides users with book information, including book titles, authors, publication dates, and descriptions. This API is designed to help book lovers easily access information about their favorite books.

## Getting Started

To use Athenium API, you will need to install the required dependencies. You can do this by running the following command:

```
pip install -r requirements.txt
```

After installing the dependencies, you can start the server by running the following command:

```
python app.py
```

The server will start on `localhost:5000`.

<!-- ## Endpoints

Athenium API provides the following endpoints:

### `GET /books`

Returns a list of books in the database. You can filter the books by title, author, or publication date by passing the corresponding query parameters:

```
/books?title=book_title
/books?author=author_name
/books?published_date=yyyy-mm-dd
```

### `GET /books/:id`

Returns information about a specific book. You can access a book by its ID.

### `POST /books`

Adds a new book to the database. The request body should include the following fields:

```
{
    "title": "book_title",
    "author": "author_name",
    "published_date": "yyyy-mm-dd",
    "description": "book_description"
}
```

### `PUT /books/:id`

Updates the information of a specific book. You can access a book by its ID. The request body should include the fields you want to update:

```
{
    "title": "new_book_title",
    "author": "new_author_name",
    "published_date": "new_yyyy-mm-dd",
    "description": "new_book_description"
}
```

### `DELETE /books/:id`

Removes a specific book from the database. You can access a book by its ID. -->

## Contributing

We welcome contributions to Athenium API. If you find any bugs or have any suggestions, please create a new issue or submit a pull request.

## License

Athenium API is licensed under the MIT License. See `LICENSE` for more information.