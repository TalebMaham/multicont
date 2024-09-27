from flask import Flask, request, jsonify

app = Flask(__name__)

panier = []

@app.route('/panier', methods=['GET'])
def get_panier():
    return jsonify(panier)

@app.route('/panier', methods=['POST'])
def ajouter_au_panier():
    produit = request.json
    panier.append(produit)
    return jsonify(panier), 201

@app.route('/panier/retirer', methods=['POST'])
def retirer_du_panier():
    produit = request.json
    panier[:] = [p for p in panier if p['name'] != produit['name']]
    return jsonify(panier), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
