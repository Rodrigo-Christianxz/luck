# database.py

import sqlite3

def conectar_bd():
    conn = sqlite3.connect('luck_database.db')
    return conn
