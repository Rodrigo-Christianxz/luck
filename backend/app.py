from flask import Flask, jsonify, request

app = Flask(__name__)

# Dicionário de respostas simples
comandos = {
    "O que você pode fazer?": "Posso ajudar com suas tarefas.",
}

# Lista de tarefas
tarefas = []

# Rota para comandos simples
@app.route('/comando', methods=['POST'])
def processar_comando():
    dados = request.get_json()
    comando = dados.get('comando')

    resposta = comandos.get(comando, "Comando não reconhecido.")
    
    return jsonify({"resposta": resposta})

# Adicionar uma nova tarefa
@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    dados = request.get_json()
    tarefa = dados.get('tarefa')
    
    if tarefa:
        tarefas.append(tarefa)
        return jsonify({"mensagem": f"Tarefa '{tarefa}' adicionada com sucesso!"})
    else:
        return jsonify({"erro": "Nenhuma tarefa fornecida."}), 400

# Listar todas as tarefas
@app.route('/listar_tarefas', methods=['GET'])
def listar_tarefas():
    if tarefas:
        return jsonify({"tarefas": tarefas})
    else:
        return jsonify({"mensagem": "Nenhuma tarefa encontrada."})

# Remover uma tarefa
@app.route('/remover_tarefa', methods=['POST'])
def remover_tarefa():
    dados = request.get_json()
    tarefa = dados.get('tarefa')
    
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        return jsonify({"mensagem": f"Tarefa '{tarefa}' removida com sucesso!"})
    else:
        return jsonify({"erro": "Tarefa não encontrada."}), 404

if __name__ == "__main__":
    app.run(debug=True)
