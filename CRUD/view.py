#Importação da biblioteca SQLite
import sqlite3 as lite

#CRUD
#CREATE = INSERIR/CRIAR
#READY = ACESSAR/MOSTRAR
#UPDATE  = ATUALIZAR
#DELETE = DELETAR/APAGAR


#CRIANDO CONEXAO:
con = lite.connect("dados.db")

 
#INSERIR INFORMAÇÃO:
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

        
        
        
#ACESSAR INFORMAÇÃO:
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista



#ATUALIZAR INFORMAÇÃO:
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, sobre=? WHERE id=?"
        cur.execute(query, i)
        
        
#DELETar informação:
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)