import sqlite3
from config.config import DATABASE

def start_db():
    try:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    email TEXT NOT NULL                        
                )
            ''')
    except Exception as e:
        print(f"Erro de conexão: {e}")        