import os
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib

# Função para treinar uma rede neural simples com scikit-learn
def treinar_rede(entradas, saidas):
    # Criar a pasta 'data' se não existir
    if not os.path.exists('data'):
        os.makedirs('data')

    # Normalizando os dados de entrada
    scaler = MinMaxScaler()
    entradas_normalizadas = scaler.fit_transform(entradas)

    # Dividindo os dados em treino e teste (10% para teste)
    X_train, X_test, y_train, y_test = train_test_split(entradas_normalizadas, saidas, test_size=0.1, random_state=42)

    # Definindo o modelo de rede neural com mais neurônios e regularização
    modelo = MLPRegressor(hidden_layer_sizes=(10,), max_iter=1000)

    # Treinando a rede neural
    modelo.fit(X_train, y_train)

    # Avaliando a rede no conjunto de teste
    score = modelo.score(X_test, y_test)
    print(f"Score de teste: {score}")

    # Salvando o modelo treinado
    joblib.dump(modelo, 'data/modelo_neural.pkl')

    return modelo

# Execução principal
if __name__ == "__main__":
    # Exemplo de entradas e saídas
    entradas = [
        [0.5, 0.3], [0.6, 0.8], [0.9, 0.1], [0.4, 0.7], [0.7, 0.9], [0.1, 0.2], [0.3, 0.5], [0.8, 0.6],
        [0.2, 0.9], [0.4, 0.4], [0.1, 0.5], [0.3, 0.9], [0.7, 0.2], [0.5, 0.1], [0.9, 0.7], [0.6, 0.3],
        [0.4, 0.2], [0.8, 0.9], [0.9, 0.6], [0.2, 0.1], [0.3, 0.8], [0.7, 0.4]
    ]
    saidas = [
        0.4, 0.7, 0.2, 0.5, 0.9, 0.3, 0.6, 0.8, 0.5, 0.4, 0.3, 0.7, 0.6, 0.2, 0.9, 0.8,
        0.5, 0.9, 0.6, 0.3, 0.7, 0.4
    ]

    # Executando o treinamento da rede neural
    treinar_rede(entradas, saidas)
