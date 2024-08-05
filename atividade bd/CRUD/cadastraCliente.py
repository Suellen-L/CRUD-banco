import sqlite3
import conexao

def cadastra_cliente():
    try:
        conexao.conectar()
        nome=input("qual o seu nome? ")
        sobrenome=input("qual seu sobrenome? ")
        idade=int(input("qual a sua idade? "))
        cpf=int(input("qual o seu CPF? "))
        telefone=input("qual seu telefone? ")
        endereco=input("qual o seu endereço? ")
        cidade=input("qual a sua cidade? ")
        estado=input("qual o seu estado? ")

        inserir_clientes="INSERT INTO clientes VALUES ('"+nome+"', '"+sobrenome+"', '"+str(idade)+"', '"+str(cpf)+"', '"+str(telefone)+"', '"+endereco+"', '"+cidade+"', '"+estado+"')"
        conexao.cursor.execute(inserir_clientes)
        conexao.conn.commit()
        conexao.conn.close()
        print("cadastro concluido")
    except sqlite3.Error as erro:
        print("erro no cadastro",erro)