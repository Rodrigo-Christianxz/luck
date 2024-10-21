# neural_network.py

import torch
import torch.nn as nn
import torch.optim as optim
import json

class ComandoModelo(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ComandoModelo, self).__init__()
        self.hidden = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.output = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        hidden_out = self.hidden(x)
        relu_out = self.relu(hidden_out)
        output_out = self.output(relu_out)
        return output_out

def treinar_modelo(dados):
    input_size = len(dados['input'][0])  # Tamanho dos dados de entrada
    hidden_size = 10  # Tamanho da camada oculta
    output_size = len(dados['output'])  # Número de classes de saída

    modelo = ComandoModelo(input_size, hidden_size, output_size)
    criterio = nn.CrossEntropyLoss()
    otimizador = optim.SGD(modelo.parameters(), lr=0.01)

    for epoch in range(100):  # Número de épocas
        for input_tensor, target in zip(dados['input'], dados['output']):
            input_tensor = torch.FloatTensor(input_tensor)
            target = torch.LongTensor([target])

            otimizador.zero_grad()
            output = modelo(input_tensor)
            perda = criterio(output.unsqueeze(0), target)
            perda.backward()
            otimizador.step()

    return modelo

def carregar_dados():
    # Exemplo de dados. Você deve substituir isso pelos seus dados reais.
    return {
        "input": [
            [1, 0, 0, 0],  # O que você pode fazer?
            [0, 1, 0, 0],  # Adicione uma tarefa.
            [0, 0, 1, 0],  # Mostre minhas tarefas.
            [0, 0, 0, 1]   # Comando adicional.
        ],
        "output": [
            0,  # Classe para "O que você pode fazer?"
            1,  # Classe para "Adicione uma tarefa."
            2,  # Classe para "Mostre minhas tarefas."
            1   # Classe para o comando adicional.
        ]
    }

if __name__ == "__main__":
    dados = carregar_dados()
    modelo = treinar_modelo(dados)
    print("Modelo treinado com sucesso!")
