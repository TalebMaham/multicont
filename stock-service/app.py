from flask import Flask, jsonify

app = Flask(__name__)

# Exemple de stock
stock = [
    {"name": "Produit 1", "quantity": 100},
    {"name": "Produit 2", "quantity": 50},
    {"name": "Produit 3", "quantity": 200},
]

@app.route('/stock')
def get_stock():
    return jsonify(stock)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
