# backend/tests/test_api.py

import unittest
import json
from app import app

class TestLuckAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_adicionar_tarefa(self):
        resposta = self.app.post('/tarefa', json={"descricao": "Testar tarefa"})
        self.assertEqual(resposta.status_code, 201)
        self.assertIn(b'tarefa adicionada', resposta.data)

    def test_listar_tarefas(self):
        self.app.post('/tarefa', json={"descricao": "Testar tarefa"})
        resposta = self.app.get('/tarefas')
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b'Testar tarefa', resposta.data)

if __name__ == '__main__':
    unittest.main()
