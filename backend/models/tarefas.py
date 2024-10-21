# backend/models/tarefas.py

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        nova_tarefa = Tarefa(descricao)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        return self.tarefas
