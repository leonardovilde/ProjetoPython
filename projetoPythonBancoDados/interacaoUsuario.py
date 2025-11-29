from time import sleep
from crud import readTable, createTable, deleteTable
import sqlite3

def menu_interacao():
    
    loop = True

    while loop != False:
        continuarSistema = input("Deseja continuar ou sair\nDigite 1 para Continuar e 2 para Sair: ")

        if continuarSistema == "1":
            print("Bem vindo ao nosso sistema!")
            print("Verificando se existem tabelas no banco...\n")
            
            conexao = sqlite3.connect("ProjetoPython.sqlite")
            cursor = conexao.cursor()

            readTable(cursor, conexao)

            createTable()

            deleteTable()
            

        elif continuarSistema == "2":

            for animacao in range(8):
                sleep(0.2)
                print("*")

            print("Você saiu do sistema.")
            loop = False


        else:
            print("Informe uma opção válida!\n")
            loop = True