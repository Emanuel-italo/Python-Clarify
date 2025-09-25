import sqlite3

def conectar_banco():
    local = r"C:\Users\emanu\Downloads\Python - clarify\Python-Clarify\meuBanco.db"
    conexao = sqlite3.connect(local)
    return conexao

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    """)
    conexao.commit()
    conexao.close()

def inserir_usuarios(nome, idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios(nome, idade) VALUES (?, ?)", (nome, idade))
    conexao.commit()
    conexao.close()

def ver_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

# Uso
criar_tabela()
inserir_usuarios("Juliana", 9)
inserir_usuarios("Diego", 11)
inserir_usuarios("Horacio", 15)
inserir_usuarios("Caio", 18)
inserir_usuarios("Byanca", 19)
inserir_usuarios("Marcelo", 21)
ver_usuarios()
