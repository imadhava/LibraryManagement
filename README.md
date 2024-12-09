Library Management System API - Flask

Welcome to the Library Management System API! This simple yet powerful system allows you to manage a collection of books, perform CRUD operations, and search for books by title, author, or both. Designed for simplicity and clarity, this API is perfect for small-scale library systems or personal projects.

Features
Add Books: Create new books with titles, authors, and content for multiple pages.
Retrieve Books: Search for books by title, author, or both.
Update Books: Update book information, including title, author, and page content.
Delete Books: Remove books from the library by specifying title and author.
API Endpoints
1. Add a Book

Endpoint: /create
Method: POST
Description: Adds a new book to the library.
Request Body:
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "pages": [
        {"number": 1, "content": "Chapter 1 content"},
        {"number": 2, "content": "Chapter 2 content"}
    ]
}
Response:
Success (201):
{
    "message": "Book successfully added to the library",
    "title": "the great gatsby",
    "author": "f. scott fitzgerald",
    "pages": [
        {"page_number": 1, "content": "Chapter 1 content"},
        {"page_number": 2, "content": "Chapter 2 content"}
    ]
}
Error (400): Missing title or author, or book already exists.
2. Retrieve Books

Endpoint: /book
Method: GET
Description: Retrieves books based on title, author, or both.
Query Parameters:
title (optional): Filter by book title.
author (optional): Filter by book author.
Examples:
Search by title: /book?title=The Great Gatsby
Search by author: /book?author=F. Scott Fitzgerald
Search by both: /book?title=The Great Gatsby&author=F. Scott Fitzgerald
Response:
Success (200):
[
    {
        "title": "the great gatsby",
        "author": "f. scott fitzgerald",
        "pages": [
            {"page_number": 1, "content": "Chapter 1 content"},
            {"page_number": 2, "content": "Chapter 2 content"}
        ]
    }
]
Error (404): No books found.
3. Delete a Book

Endpoint: /delete
Method: DELETE
Description: Deletes a book from the library based on title and author.
Request Body:
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
Response:
Success (200):
{
    "message": "Book(s) successfully removed from the library"
}
Error (404): Book not found.
4. Update a Book

Endpoint: /book
Method: PUT
Description: Updates the details of an existing book.
Request Body:
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "new_title": "The Greatest Gatsby",
    "new_author": "Fitzgerald",
    "pages": [
        {"number": 1, "content": "Updated Chapter 1"},
        {"number": 2, "content": "Updated Chapter 2"}
    ]
}
Response:
Success (200):
{
    "message": "Book details updated successfully",
    "title": "the greatest gatsby",
    "author": "fitzgerald",
    "pages": [
        {"page_number": 1, "content": "Updated Chapter 1"},
        {"page_number": 2, "content": "Updated Chapter 2"}
    ]
}
Error (404): Book not found.
Running the Application
Install Flask: Make sure you have Python installed. Then, install Flask using pip:
pip install flask
Run the Application: Save the code to a file (e.g., app.py) and run it:
python app.py
Access the API: The application will run on http://127.0.0.1:5000. Use tools like Postman, curl, or your browser to interact with the API.
Example Use Cases
Add a Book:

Request:

curl -X POST http://127.0.0.1:5000/create -H "Content-Type: application/json" -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "pages": [
        {"number": 1, "content": "Chapter 1 content"},
        {"number": 2, "content": "Chapter 2 content"}
    ]
}'
Search for Books:

Request:

curl http://127.0.0.1:5000/book?title=The%20Great%20Gatsby
Delete a Book:

Request:

curl -X DELETE http://127.0.0.1:5000/delete -H "Content-Type: application/json" -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}'
Notes
The book title and author are case-insensitive; they are stored and compared in lowercase.
If no books match the search, you will receive a 404 error.
You must include both title and author to delete or update a book.
