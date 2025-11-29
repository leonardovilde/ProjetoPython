import sqlite3

def createTable():
            criarTabela = input("Deseja criar uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            if criarTabela == "1":
                nomeTabela = input("Qual o nome da tabela que deseja criar? ")
                print(f"Tabela '{nomeTabela}' criada com sucesso!\n")

            elif criarTabela == "2":
                print("A tabela não foi criada!\n")

            else:
                print("Opção inválida!\n")

def readTable(cursor, conexao):
     conexao = sqlite3.connect("ProjetoPython.sqlite")
     cursor = conexao.cursor()

     listarTabelas = "SELECT name FROM sqlite_master WHERE type='table';"

     cursor.execute(listarTabelas)

     tabelas = cursor.fetchall()

     if tabelas:
      for tabela in tabelas:
        print("Tabela", tabela[0])

     else: 
      print("nenhuma Tabela encontrada no banco atual")


def update():
    pass

def deleteTable():
            deletarTabela = input("Deseja deletar uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            if deletarTabela == "1":
                print("Deletando tabelas...\n")
                print("Tabela deletada com sucesso")

            elif deletarTabela == "2":
                print("A Tabela não foi deletada!\n")

            else:
                print("Opção inválida!\n")

            loop = True  

