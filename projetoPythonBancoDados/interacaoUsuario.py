from time import sleep

def menu_interacao():
    
    loop = True

    while loop != False:
        continuarSistema = input("Deseja continuar ou sair\nDigite 1 para Continuar e 2 para Sair: ")

        if continuarSistema == "1":
            print("Você Continuou!")
            print("Verificando se existem tabelas no banco...\n")

            
            criarTabela = input("Deseja criar uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            if criarTabela == "1":
                nomeTabela = input("Qual o nome da tabela que deseja criar? ")
                print(f"Tabela '{nomeTabela}' criada com sucesso!\n")

            elif criarTabela == "2":
                print("Nenhuma tabela será criada!\n")

            else:
                print("Opção inválida!\n")


            
            deletarTabela = input("Deseja deletar uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            if deletarTabela == "1":
                print("Deletando tabelas...\n")

            elif deletarTabela == "2":
                print("Nenhuma tabela será deletada!\n")

            else:
                print("Opção inválida!\n")

            loop = True  



        elif continuarSistema == "2":

            for animacao in range(10):
                sleep(0.3)
                print("*")

            print("Você saiu do sistema.")
            loop = False


        else:
            print("Informe uma opção válida!\n")
            loop = True