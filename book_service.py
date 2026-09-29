from flask import Flask, jsonify

app = Flask(__name__)

# Database bohongan
books = [
    {
        "id": 1,
        "title": "Belajar Flask",
        "stock": 5
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(port=5001, debug=True)