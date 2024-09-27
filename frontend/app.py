from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Frontend: Page principale
@app.route('/')
def index():
    # Récupérer les produits du service stock
    produits = requests.get('http://stock:5001/stock').json()
    # Récupérer le panier du service panier
    panier = requests.get('http://panier:5002/panier').json()
    return render_template('index.html', produits=produits, panier=panier)

# Route pour ajouter un produit au panier
@app.route('/ajouter-au-panier', methods=['POST'])
def ajouter_au_panier():
    produit = request.json
    response = requests.post('http://panier:5002/panier', json=produit)
    return response.json()

# Route pour retirer un produit du panier
@app.route('/retirer-du-panier', methods=['POST'])
def retirer_du_panier():
    produit = request.json
    response = requests.post('http://panier:5002/panier/retirer', json=produit)
    return response.json()

# Route pour effectuer une transaction
@app.route('/acheter', methods=['POST'])
def acheter():
    panier = requests.get('http://panier:5002/panier').json()
    response = requests.post('http://transaction:5003/transaction', json=panier)
    return response.json()

@app.route('/historique')
def historique():
    # Récupérer l'historique des transactions depuis le microservice
    historique_transactions = requests.get('http://historique:5004/historique').json()
    return render_template('historique.html', historique=historique_transactions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
