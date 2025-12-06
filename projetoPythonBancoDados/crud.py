import sqlite3

def readTable(conexao, cursor):
    conexao = sqlite3.connect("ProjetoPython.sqlite")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()

    if tabelas:
        for tabela in tabelas:
            print("Tabela:", tabela[0])
    else:
        print("Nenhuma tabela encontrada no banco atual.")


def createTable(cursor, conexao):
    print("Criando tabelas...")
    conexao = sqlite3.connect("ProjetoPython.sqlite")

    cursor.execute("DROP TABLE IF EXISTS clientes")
    cursor.execute("DROP TABLE IF EXISTS produtos")
    cursor.execute("DROP TABLE IF EXISTS pedidos")
    cursor.execute("DROP TABLE IF EXISTS fornecedores")
    cursor.execute("DROP TABLE IF EXISTS categorias")

    cursor.execute("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            data_nascimento DATE
        );
    """)

    cursor.execute("""
        CREATE TABLE produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL,
            estoque INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data DATE,
            valor_total REAL,
            status TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE fornecedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT,
            telefone TEXT,
            cidade TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT
        );
    """)

    conexao.commit()
    print(" Tabelas criadas com sucesso!\n")


def InsertSql(conexao, cursor):
    conexao = sqlite3.connect("ProjetoPython.sqlite")

    print("Inserindo dados...")

    cursor.execute("""
        INSERT INTO clientes (nome, email, telefone, data_nascimento) VALUES
        ('Leonardo Amorim', 'leonardo@gmail.com', '1199999-0001', '1996-08-15'),
        ('Maria Silva', 'maria.silva@gmail.com', '1198888-0002', '1990-05-10'),
        ('João Pereira', 'joao.pereira@gmail.com', '1197777-0003', '1988-11-02'),
        ('Ana Souza', 'ana.souza@gmail.com', '1196666-0004', '2001-03-23'),
        ('Carlos Santos', 'carlos.santos@gmail.com', '1195555-0005', '1999-12-01');
    """)

    cursor.execute("""
        INSERT INTO produtos (nome, preco, estoque) VALUES
        ('Camiseta Básica', 49.90, 30),
        ('Calça Jeans', 120.00, 15),
        ('Boné Preto', 35.50, 40),
        ('Tênis Esportivo', 220.00, 10),
        ('Moletom Cinza', 149.90, 25);
    """)

    cursor.execute("""
        INSERT INTO pedidos (data, valor_total, status) VALUES
        ('2024-01-10', 170.40, 'Finalizado'),
        ('2024-02-05', 240.00, 'Finalizado'),
        ('2024-02-10', 49.90, 'Pendente'),
        ('2024-03-22', 120.00, 'Cancelado'),
        ('2024-04-01', 390.00, 'Finalizado');
    """)

 
    cursor.execute("""
        INSERT INTO fornecedores (nome, cnpj, telefone, cidade) VALUES
        ('Fornec Roupas LTDA', '12.345.678/0001-90', '1199999-1111', 'São Paulo'),
        ('Moda Brasil SA', '98.765.432/0001-00', '1192222-3333', 'Campinas'),
        ('Estilo Urbano ME', '22.333.444/0001-55', '1194444-2222', 'Santos'),
        ('Tecidos Premium', '77.888.999/0001-88', '1191111-7777', 'Jundiaí'),
        ('SP Imports', '11.222.333/0001-44', '1190000-1110', 'Guarulhos');
    """)

  
    cursor.execute("""
        INSERT INTO categorias (nome, descricao) VALUES
        ('Roupas', 'Vestuário em geral'),
        ('Calçados', 'Calçados esportivos e casuais'),
        ('Acessórios', 'Bonés e cintos'),
        ('Inverno', 'Roupas de frio'),
        ('Esportivo', 'Materiais esportivos');
    """)

    conexao.commit()

    print("\n Dados inseridos com sucesso!")
    print("📋 Listando todas as tabelas:\n")

    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()

    for tabela in tabelas:
        nome = tabela[0]
        print(f"\n Tabela: {nome}")

        cursor.execute(f"SELECT * FROM {nome}")
        linhas = cursor.fetchall()

        if linhas:
            for linha in linhas:
                print(" ", linha)
        else:
            print("   (vazia)")




def deleteTable(cursor, conexao, nomeTabelaParaDeletar):
    """
    Exclui todos os registros da tabela passada pelo usuário.
    """
    comando = f"DELETE FROM {nomeTabelaParaDeletar} WHERE id IN (1, 2)"  
    cursor.execute(comando)
    conexao.commit()
    print(f"✔ Registros da tabela {nomeTabelaParaDeletar} foram excluídos!")