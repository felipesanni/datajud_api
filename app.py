from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/estatisticas', methods=['GET'])
def get_estatisticas():
    url = "https://datajud-api.cnj.jus.br/v1/processos"
    headers = {"Authorization": "Bearer seu_token_aqui"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        estatisticas = {
            "processos_distribuidos": data["processos_distribuidos"],
            "processos_julgados": data["processos_julgados"],
            "processos_pendentes": data["processos_pendentes"]
        }
        return jsonify(estatisticas)
    else:
        return jsonify({"error": "Não foi possível obter as estatísticas"}), response.status_code
