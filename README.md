Library Management System API with Flask
This document provides an overview of a simple yet powerful Library Management System API built using Flask.

Features

CRUD Operations: Create, Read, Update, and Delete books.
Search Functionality: Find books by title, author, or both.
Lightweight Design: Ideal for small-scale libraries or personal projects.
API Endpoints

Add a Book (POST /create)

Request Body (JSON):
JSON
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "pages": [
        {"number": 1, "content": "Chapter 1 content"},
        {"number": 2, "content": "Chapter 2 content"}
    ]
}
Response:
Success (201): JSON containing the added book details (with lowercase title and author).
Error (400): Missing title or author, or book already exists.
Retrieve Books (GET /book)

Query Parameters (Optional):
title: Filter by book title.
author: Filter by book author.
Examples:
/book?title=The Great Gatsby (Search by title)
/book?author=F. Scott Fitzgerald (Search by author)
/book?title=The Great Gatsby&author=F. Scott Fitzgerald (Search by both)
Response:
Success (200): JSON array containing matching books (lowercase title and author).
Error (404): No books found.
Delete a Book (DELETE /delete)

Request Body (JSON):
JSON
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
Response:
Success (200): JSON with message "Book(s) successfully removed from the library".
Error (404): Book not found.
Update a Book (PUT /book)

Request Body (JSON):
JSON
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
Success (200): JSON containing the updated book details (lowercase title and author).
Error (404): Book not found.
Running the Application

Install Flask:
Bash
pip install flask
Save the code to a file (e.g., app.py).
Run the application:
Bash
python app.py
Access the API: http://127.0.0.1:5000 (Use tools like Postman, curl, or your browser to interact).
Example Use Cases

Add a Book:

Bash
curl -X POST http://127.0.0.1:5000/create -H "Content-Type: application/json" -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "pages": [
        {"number": 1, "content": "Chapter 1 content"},
        {"number": 2, "content": "Chapter 2 content"}
    ]
}'
Search for Books:

Bash
curl http://127.0.0.1:5000/book?title=The%20Great%20Gatsby
Delete a Book:

Bash
curl -X DELETE http://127.0.0.1:5000/delete -H "Content-Type: application/json" -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}'
Notes

Book titles and authors are stored and compared in lowercase for case-insensitivity.
A 404 error indicates
