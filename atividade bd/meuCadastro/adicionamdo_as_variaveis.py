import sqlite3
def inserir_dados(nome,idade,email):
   
    nome=input('imforme o nome: ')
    idade=int(input('informe a idade: '))
    email=input('informe o email: ')

    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    
    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"')")

    banco.commit()
    