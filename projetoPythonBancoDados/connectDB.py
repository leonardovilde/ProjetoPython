import sqlite3

conexao = sqlite3.connect("ProjetoPython.sqlite")

cursor = conexao.cursor()

comandoSQL = '''
CREATE TABLE IF NOT EXISTS Tabelas (
id INTEGER,
nome TEXT NOT NULL
)
'''

cursor.execute (comandoSQL)
conexao.commit()
conexao.close()