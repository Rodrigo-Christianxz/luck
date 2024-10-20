import torch
import torch.nn as nn
import torch.optim as optim

# Exemplo simples de uma rede neural
class RedeNeuralSimples(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RedeNeuralSimples, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Função de treino (Exemplo)
def treinar_rede(entradas, saidas, epochs=100, learning_rate=0.01):
    input_size = entradas.shape[1]
    hidden_size = 5
    output_size = saidas.shape[1]

    modelo = RedeNeuralSimples(input_size, hidden_size, output_size)
    criterio = nn.MSELoss()
    otimizador = optim.Adam(modelo.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        otimizador.zero_grad()
        predicao = modelo(entradas)
        perda = criterio(predicao, saidas)
        perda.backward()
        otimizador.step()

    # Salvar o modelo treinado
    torch.save(modelo.state_dict(), 'src/data/modelo_neural.pth')

    return modelo
