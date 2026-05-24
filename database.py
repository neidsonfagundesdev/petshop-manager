#importa o sqlite3 para criar um banco de dados
import sqlite3 as sql 

#Criando o banco. (cria o arquivo petshop.db automaticamente)
conn = sql.connect('petshop.db')
cursor = conn.cursor()

#Cria tabela dos cliente se não existir
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY
AUTOINCREMENT,
    nome TEXT NOT NULL, 
    endereco TEXT,
    telefone TEXT,           
    email TEXT,
    cpf TEXT UNIQUE NOT NULL 
)
""")

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")

# ******************* Funções para usar com o streamlit (app.py) ********************

#Essa função retorna uma conexão com o banco de dados
def conectar():
    return sql.connect('petshop.db')

#Essa função salva um objeto cliente no banco de dados
def salvar_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO clientes (nome, endereco, telefone, email, cpf)
            VALUES (?, ?, ?, ?, ?)           
        """, (cliente.nome, cliente.endereco, cliente.telefone, cliente.email, cliente.cpf))
        conn.commit()
        return True, "Cliente salvo com sucesso!"
    except sql.IntegrityError:
        return False, "Erro: CPF já cadastrado!"
    finally:
        conn.close()

#Essa função retorna todos os clientes cadastrados
def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes ORDER BY nome')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

#Essa função busca um cliente pelo CPF
def buscar_cliente_por_cpf(cpf):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE cpf = ?', (cpf, ))
    resultado = cursor.fetchall()
    conn.close()
    return resultado



