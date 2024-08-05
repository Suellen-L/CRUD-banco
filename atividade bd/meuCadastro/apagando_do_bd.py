import sqlite3

def deletar(idade):
    
    idade=int(input('qual idade deseja deletar: '))
    try:
    
        banco = sqlite3.connect('primeiro_banco.db')
    
        cursor = banco.cursor()

        cursor.execute("DELETE from pessoas WHERE idade = "+str(idade)+"")
    
        banco.commit()
        banco.close()
        print("removido com sucesso")
    
    except sqlite3.Error as erro:
        print("erro: ",erro)