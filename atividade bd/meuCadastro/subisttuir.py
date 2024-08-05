import sqlite3
def substituir():
    
    nome(input('informe o nome que ira subistituir: '))
    idade =int(input('informe a idade da pessoa que sera substituida: '))

    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    nome=input('imforme o nome que ira substituir: ')
    idade=int(input('insira a idade da pessoa a ser substituida: '))

    cursor.execute("UPDATE pessoas SET nome = '"+nome+"' WHERE idade = "+str(idade)+"")