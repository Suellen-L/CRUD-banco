import sqlite3

def conectando():
   
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()