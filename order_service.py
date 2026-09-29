from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BOOK_SERVICE_URL = "http://localhost:5001"

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    book_id = data.get('book_id')

    try:
        response = requests.get(
            f"{BOOK_SERVICE_URL}/books"
        )

        books = response.json()

        for book in books:
            if book['id'] == book_id and book['stock'] > 0:
                order = {
                    "id": 1,
                    "book_id": book_id,
                    "status": "berhasil"
                }

                return jsonify(order), 201

        return jsonify({
            "error": "Buku tidak ditemukan atau stok habis"
        }), 400

    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Book Service tidak tersedia"
        }), 503


if __name__ == '__main__':
    app.run(port=5002, debug=True)