import sqlite3

def createTable():
      print('Criando tabela....')

def readTable(conexao, cursor):
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
    print("Deletando....")

