import conecta 
import adicionamdo_as_variaveis
import apagando_do_bd
import subisttuir
import criando_banco

criando_banco.criar_banco()
cont=1
while (cont !='0'):
    print("escolha\n1-adicionar dados\n2-apagar dados\n3-substituir dados\n4-encerrar")
    menu=int(input('qual função deseja realizar: '))
    if menu == '1':
        conecta.conectando()
        adicionamdo_as_variaveis.inserir_dados()
    elif menu == '2':
        conecta.conectando()
        apagando_do_bd.deletar()
    elif menu == '3':
        conecta.conectando()
        subisttuir.substituir()
    elif menu == '4':
        print("ate a proxima")
    else:
        print("opção invalida")
    cont=int(input('deseja realizar outra função? [1-sim 0-não]: '))