import sqlite3
from config.config import DATABASE

def start_db():
    """
    Inicializa o banco de dados SQLite.

    Cria a tabela 'cliente' no banco de dados,
    caso ela ainda não exista. A tabela contém os seguintes campos:

        - id (INTEGER, chave primária, autoincrementável)
        - nome (TEXT, obrigatório)
        - cpf (TEXT, obrigatório)
        - email (TEXT, obrigatório)

    Em caso de erro, uma mensagem será exibida.

    """
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