from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import joblib  # Para salvar o modelo

# Função para treinar uma rede neural simples com scikit-learn
def treinar_rede(entradas, saidas):
    # Dividindo os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(entradas, saidas, test_size=0.2, random_state=42)

    # Definindo o modelo de rede neural com múltiplas camadas perceptron
    modelo = MLPRegressor(hidden_layer_sizes=(10,), max_iter=1000)

    # Treinando a rede neural
    modelo.fit(X_train, y_train)

    # Avaliando a rede no conjunto de teste
    score = modelo.score(X_test, y_test)
    print(f"Score de teste: {score}")

    # Salvando o modelo treinado
    joblib.dump(modelo, 'src/data/modelo_neural.pkl')

    return modelo
