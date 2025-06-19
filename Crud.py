import sqlite3

def conectar():
    return sqlite3.connect('database.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            token TEXT,
            legenda TEXT,
            termo TEXT,
            intervalo INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def criar_usuario(nome, token, legenda, termo, intervalo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, token, legenda, termo, intervalo)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, token, legenda, termo, intervalo))
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Cria a tabela automaticamente ao importar
criar_tabela()
