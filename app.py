from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="

# Função para obter os dados de um endpoint específico da API Datajud
def obter_dados_datajud(endpoint):
    url = f"https://datajud-api.cnj.jus.br{endpoint}"
    headers = {"Authorization": f"APIKey {API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Não foi possível obter os dados"}, response.status_code

@app.route('/api/<path:endpoint>', methods=['GET'])
def consulta_datajud(endpoint):
    dados = obter_dados_datajud(f"/v1/{endpoint}")
    return jsonify(dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
