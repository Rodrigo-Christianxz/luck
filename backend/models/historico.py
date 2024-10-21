# backend/models/historico.py

class Historico:
    def __init__(self):
        self.historico_tarefas = []

    def adicionar_historico(self, tarefa):
        self.historico_tarefas.append(tarefa)

    def listar_historico(self):
        return self.historico_tarefas
