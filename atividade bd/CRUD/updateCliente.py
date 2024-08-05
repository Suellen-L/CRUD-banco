import conexao
import selectCliente

def alterar_dados():
    conexao.conectar()
    print("[alteração de dados]")
    global cpfpesquisar
    cpfpesquisar = selectCliente.consultar_cliente()
    if(cpfpesquisar != []):
        dado_update=input("qual sera alterado?\nnome\nsobrenome\nidade\ntelefone\nendereço\ncidade\nestado\n").lower()
        atualizacao(dado_update)

def atualizacao(dado_update):
    conexao.conectar()
    if dado_update == 'nome':
        novo_nome=input("qual o novo nome: ")
        conexao.cursor.execute("UPDATE clientes SET nome = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("nome alterado")

    elif dado_update == 'sobrenome':
        novo_nome=input("qual o novo nome: ")
        conexao.cursor.execute("UPDATE clientes SET sobrenome = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("nome alterado")

    elif dado_update == 'nome':
        novo_nome=input("qual o novo nome: ")
        conexao.cursor.execute("UPDATE clientes SET nome = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("nome alterado")

    elif dado_update == 'nome':
        novo_nome=input("qual o novo nome: ")
        conexao.cursor.execute("UPDATE clientes SET nome = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("nome alterado")

    elif dado_update == 'nome':
        novo_nome=input("qual o novo nome: ")
        conexao.cursor.execute("UPDATE clientes SET nome = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("nome alterado")

    elif dado_update == 'nome':
        novo_nome=input("qual o novo nome: ")
        conexao.cursor.execute("UPDATE clientes SET nome = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("nome alterado")

    #conexao.conn.commit()
    else:
        print("deu ruim")
    