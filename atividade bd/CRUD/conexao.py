import sqlite3
#criação de função para conectar ao banco de dados
def conectar():
    try:
        global conn
        conn=sqlite3.connect("cadastro.db")
        global cursor
        cursor=conn.cursor()
        print("__________________________________________________________________")
        print("conexão com o banco realizada com sucesso!")
        print("__________________________________________________________________")
    except sqlite3.Error as erro:
        print("__________________________________________________________________")
        print("erro de conexão com o banco de dados")
        print("__________________________________________________________________")