import conexao
import sqlite3
def exibir_cliente():
    conexao.conectar()
    resultado=conexao.cursor.execute("SELECT * FROM clientes").fetchall()
    for result in resultado:
        print("__________________________________________________________________")
        print("nome:",result[0])
        print("sobrenome:",result[1])
        print("idade:",result[2])
        print("cpf:",result[3])
        print("telefone:",result[4])
        print("endereco:",result[5])
        print("cidade:",result[6])
        print("estado:",result[7])
        print("__________________________________________________________________")
    #conexao.conn.close()

def consultar_cliente():
    conexao.conectar()
    cpf = input("qual o CPF deseja consultar: ")
    try:
        resultado=conexao.conn.execute('''SELECT * FROM clientes WHERE cpf = ?''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado")
            
        else:
            for result in resultado:
                print("__________________________________________________________________")
                print("nome:",result[0])
                print("sobrenome:",result[1])
                print("idade:",result[2])
                print("cpf:",result[3])
                print("telefone:",result[4])
                print("endereco:",result[5])
                print("cidade:",result[6])
                print("estado:",result[7])
                print("__________________________________________________________________")
        return cpf
    except sqlite3.Error as erro:
        print("erro ao tentar encontrar o CPF ",erro)
    #conexao.conn.close()