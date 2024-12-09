from flask import Flask, request, jsonify

app = Flask(__name__)

class Page:
    def __init__(self, number: int, content: str):
        self.number = number
        self.content = content

class Book:
    def __init__(self, name: str, author: str, pages: list[Page]):
        self.name = name.lower()
        self.author = author.lower()
        self.pages = pages

books = []

def find_books(name=None, author=None):
    if name and author:
        return [book for book in books if book.name == name.lower() and book.author == author.lower()]
    elif name:
        return [book for book in books if book.name == name.lower()]
    elif author:
        return [book for book in books if book.author == author.lower()]
    return []

@app.route('/create', methods=['POST'])
def create_book():
    data = request.json
    name = data.get('name')
    author = data.get('author')
    pages_data = data.get('pages', [])
    if not name or not author:
        return jsonify({'error': 'Name and author are required'}), 400
    if find_books(name=name, author=author):
        return jsonify({'error': 'Book already exists'}), 400
    pages = [Page(number=page['number'], content=page['content']) for page in pages_data]
    new_book = Book(name=name, author=author, pages=pages)
    books.append(new_book)
    return jsonify({
        'message': 'Book created successfully',
        'name': new_book.name,
        'author': new_book.author,
        'pages': [{'number': page.number, 'content': page.content} for page in new_book.pages]
    }), 201

@app.route('/book', methods=['GET'])
def get_book():
    name = request.args.get('name', '').lower()
    author = request.args.get('author', '').lower()
    found_books = find_books(name=name if name else None, author=author if author else None)
    if not found_books:
        return jsonify({'error': 'No books found'}), 404
    return jsonify([{
        'name': book.name,
        'author': book.author,
        'pages': [{'number': page.number, 'content': page.content} for page in book.pages]
    } for book in found_books])

@app.route('/delete', methods=['DELETE'])
def delete_book():
    data = request.json
    name = data.get('name', '').lower()
    author = data.get('author', '').lower()
    book_to_delete = find_books(name=name, author=author)
    if not book_to_delete:
        return jsonify({'error': 'Book not found'}), 404
    for book in book_to_delete:
        books.remove(book)
    return jsonify({'message': 'Book(s) deleted successfully'})

@app.route('/book', methods=['PUT'])
def update_book():
    data = request.json
    name = data.get('name', '').lower()
    author = data.get('author', '').lower()
    book_to_update = find_books(name=name, author=author)
    if not book_to_update:
        return jsonify({'error': 'Book not found'}), 404
    book = book_to_update[0]
    new_name = data.get('new_name')
    new_author = data.get('new_author')
    pages_data = data.get('pages')
    if new_name:
        book.name = new_name.lower()
    if new_author:
        book.author = new_author.lower()
    if pages_data:
        book.pages = [Page(number=page['number'], content=page['content']) for page in pages_data]
    return jsonify({
        'message': 'Book updated successfully',
        'name': book.name,
        'author': book.author,
        'pages': [{'number': page.number, 'content': page.content} for page in book.pages]
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
