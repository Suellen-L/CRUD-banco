import sqlite3

def criar_banco():
   
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text, idade integer, email text)")