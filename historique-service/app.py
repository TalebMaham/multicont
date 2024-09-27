from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

historique = []

@app.route('/historique')
def get_historique():
    return jsonify(historique)

@app.route('/historique', methods=['POST'])
def ajouter_historique():
    transaction = request.json
    historique.append({
        "transaction": transaction,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return jsonify(historique), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
