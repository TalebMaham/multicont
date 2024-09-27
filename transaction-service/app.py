from flask import Flask, request, jsonify
import time
import requests

app = Flask(__name__)

@app.route('/transaction', methods=['POST'])
def transaction():
    panier = request.json
    time.sleep(2)  # Simuler le délai de transaction
    
    # Envoyer les données de la transaction au service Historique
    try:
        response = requests.post('http://historique:5004/historique', json={
            'transaction': panier,
            'date': time.strftime("%Y-%m-%d %H:%M:%S")
        })
        response.raise_for_status()  # Assurer que la requête a réussi
    except requests.exceptions.RequestException as e:
        return jsonify({"message": "Erreur lors de l'enregistrement de la transaction", "error": str(e)}), 500
    
    return jsonify({"message": "Transaction réussie", "panier": panier}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)


