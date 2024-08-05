import sqlite3
import conexao
import selectCliente

def deletar():
    conexao.conectar()
    global cpfApaga
    cpfApaga = selectCliente.consultar_cliente()
    try:
        if(cpfApaga !=[]):
            conexao.cursor.execute("DELETE FROM clientes WHERE cpf = ?" ,(cpfApaga,))
        
            conexao.conn.commit()
            #conexao.conn.close()
            print("removido com sucesso")
    
    except sqlite3.Error as erro:
        print("erro: ",erro)