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
        novo_nome=input("qual o novo sobrenome: ")
        conexao.cursor.execute("UPDATE clientes SET sobrenome = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("sobrenome alterado")

    elif dado_update == 'idade':
        novo_nome=input("qual o novo idade: ")
        conexao.cursor.execute("UPDATE clientes SET idade = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("idade alterado")

    elif dado_update == 'cpf':
        novo_nome=input("qual o novo cpf: ")
        conexao.cursor.execute("UPDATE clientes SET cpf = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("cpf alterado")

    elif dado_update == 'telefone':
        novo_nome=input("qual o novo telefone: ")
        conexao.cursor.execute("UPDATE clientes SET telefone = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("telefone alterado")

    elif dado_update == 'endereço':
        novo_nome=input("qual o novo endereço: ")
        conexao.cursor.execute("UPDATE clientes SET endereco = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("endereço alterado")

    elif dado_update == 'cidade':
        novo_nome=input("qual o nova cidade: ")
        conexao.cursor.execute("UPDATE clientes SET cidade = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("cidade alterado")

    elif dado_update == 'estado':
        novo_nome=input("qual o novo estado: ")
        conexao.cursor.execute("UPDATE clientes SET estado = '"+novo_nome+"' WHERE cpf = ?",(cpfpesquisar,))
        print("estado alterado")

    #conexao.conn.commit()
    else:
        print("deu ruim")
    