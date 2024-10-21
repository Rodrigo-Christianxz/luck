# backend/app.py

from flask import Flask, request
from backend.models.historico import Historico
from backend.models.tarefas import GerenciadorDeTarefas
from backend.models.configuracoes import Configuracoes

app = Flask(__name__)
historico = Historico()
gerenciador = GerenciadorDeTarefas()
configuracoes = Configuracoes()

@app.route('/')
def home():
    return "Bem-vindo ao Luck Assistente Pessoal!"

@app.route('/tarefa', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.json['descricao']
    gerenciador.adicionar_tarefa(nova_tarefa)
    historico.adicionar_historico(nova_tarefa)  # Adiciona ao histórico
    return {"status": "tarefa adicionada"}, 201

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = gerenciador.listar_tarefas()
    return {"tarefas": [tarefa.descricao for tarefa in tarefas]}

if __name__ == '__main__':
    app.run(debug=True)
