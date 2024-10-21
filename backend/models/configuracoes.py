# backend/models/configuracoes.py

class Configuracoes:
    def __init__(self):
        self.config = {
            "modo": "normal",
            "notificacoes": True
        }

    def get_config(self):
        return self.config

    def set_config(self, key, value):
        self.config[key] = value
