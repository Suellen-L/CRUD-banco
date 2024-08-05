import conexao
conexao.conectar()
def criar():
    criar_tabela = "CREATE TABLE IF NOT EXISTS clientes(nome string, sobrenome string, idade integer, cpf integer, telefone integer, endereco string, cidade string, estado string)"
    conexao.cursor.execute(criar_tabela)