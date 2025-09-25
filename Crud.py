import sqlite3

def conectar_banco ():
    local = r"C:\Users\emanu\Downloads\Python - clarify\Python-Clarify\meuBanco.db"
    conexao = sqlite3.connect(local)
    return conexao


def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXIST usuarios (" \
    "id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "nome TEXT," \
    "idade INTEGER" \
    ")")
    
    conexao.commit()
    conexao.close()

    def inserir_usuarios(nome,idade):
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("""INSERT INTO usuarios(nome, idade) VALUES (?,?)""",(nome, idade))
    conexao.commit()
    conexao.close()

def ver_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FRON usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()