import sqlite3

class DB:

    def __init__(self):
        self.conexao = sqlite3.connect("database.db")
        cursor = self.conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mercado(codbar INTEGER PRIMARY KEY, nome, estoque, loc, preco)")
        self.conexao.commit()
        cursor.close()

    def inserir(self, codbar, nome, estoque, loc, preco):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO mercado(codbar, nome, estoque, loc, preco) VALUES (?, ?, ?, ?, ?)", (codbar, nome, estoque, loc, preco))

        if (cursor.rowcount > 0):
            id = cursor.lastrowid
        else:
            id = None

        self.conexao.commit()
        cursor.close()
        return id
    
    def buscar(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mercado WHERE codbar = ?", (id,))
        retorno = cursor.fetchone()
        cursor.close()
        return retorno
    
    def atualizar(self, id, nome, estoque, loc, preco):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE mercado SET nome = ?, estoque = ?, loc = ?, preco = ? WHERE codbar = ?", (nome, estoque, loc, preco, id))
        self.conexao.commit()
        cursor.close()