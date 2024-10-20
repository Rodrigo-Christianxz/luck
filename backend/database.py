import sqlite3
import os

# Caminho para o banco de dados dentro de 'src/backend/'
DB_PATH = os.path.join(os.path.dirname(__file__), 'luck_database.db')

# Conectar ao banco de dados SQLite
def conectar_banco():
    conexao = sqlite3.connect(DB_PATH)
    return conexao

# Criar tabelas se não existirem
def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS configuracoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_configuracao TEXT,
        valor TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico_comandos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comando TEXT,
        resposta TEXT,
        data_execucao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas_pessoais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_tarefa TEXT,
        descricao TEXT,
        status TEXT
    )''')

    conexao.commit()
    conexao.close()

# Inicializar o banco de dados
if __name__ == "__main__":
    criar_tabelas()
