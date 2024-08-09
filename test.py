import sqlite3

# Conecta ao banco de dados (ou cria um, se não existir)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Cria uma tabela com uma coluna ID que é autoincrementada
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)''')

# Função para adicionar um novo usuário e retornar o ID gerado
def add_user(name):
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    return cursor.lastrowid

# Adiciona um novo usuário e obtém o ID gerado
new_id = add_user('Alice')
print(f'O ID gerado para o novo usuário é: {new_id}')

# Fecha a conexão com o banco de dados
conn.close()