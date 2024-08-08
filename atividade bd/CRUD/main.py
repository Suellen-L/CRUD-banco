#importação das blibliotecas
import sqlite3
from funcaoMenu import menu
import conexao
import criarTabela
import cadastraCliente
import selectCliente
import updateCliente
import deleteCliente

criarTabela.criar()

opcao=menu()
while (opcao!='6'):
    if(opcao=='1'):
        cadastraCliente.cadastra_cliente()
    elif(opcao=='2'):
        selectCliente.exibir_cliente()
    elif(opcao=='3'):
        selectCliente.consultar_cliente()
    elif(opcao=='4'):
        updateCliente.alterar_dados()
    elif(opcao=='5'):
        deleteCliente.deletar()
    elif(opcao=='6'):
       l
    opcao=menu()
