# Business requirment:we want to build a library app which is perform daily library operations and this app is hosted on cloud
# we want to perform operations like add book, delete book, update book, search book and list all books
# app hosted on docker nginx server and we want to use flask framework for backend development and react for frontend development

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for books (in a real app, this would be a database)
books = []

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = {
        "id": len(books) + 1,
        "title": data.get("title"),
        "author": data.get("author"),
        "isbn": data.get("isbn")
    }
    books.append(book)
    return jsonify(book), 201

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book["id"] == book_id:
            data = request.get_json()
            book["title"] = data.get("title", book["title"])
            book["author"] = data.get("author", book["author"])
            book["isbn"] = data.get("isbn", book["isbn"])
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# Search for a book
@app.route('/books/search', methods=['GET'])
def search_books():
    title = request.args.get("title")
    author = request.args.get("author")
    isbn = request.args.get("isbn")

    results = []
    for book in books:
        if title and title.lower() in book["title"].lower():
            results.append(book)
        elif author and author.lower() in book["author"].lower():
            results.append(book)
        elif isbn and isbn == book["isbn"]:
            results.append(book)

    return jsonify(results), 200

# List all books
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books), 200

# Root route
@app.route('/', methods=['GET'])
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':

# Initialize sample data
    for i in range(1,50):
        books.append({
            "id": i,
            "title": f"Book Title {i}",
            "author": f"Author {i}",
            "isbn": f"ISBN-{i:05d}" 
        })
        

    
    app.run(debug=True)

