import sqlite3
import produto

class DB:

    def __init__(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mercado(codbar INTEGER PRIMARY KEY, nome, estoque, loc, preco)")
        conexao.commit()
        cursor.close()
        conexao.close()


    def inserir(self, produto):
        try:
            conexao = sqlite3.connect("database.db")
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO mercado(codbar, nome, estoque, loc, preco) VALUES (?, ?, ?, ?, ?)", (produto.codbar, produto.nome, produto.estoque, produto.loc, produto.preco))

            if (cursor.rowcount > 0):
                id = cursor.lastrowid
            else:
                id = None

            conexao.commit()
            cursor.close()
            conexao.close()
            return id
        except sqlite3.IntegrityError:
            return -1
        except Exception as err:
            print(f"Erro inesperado: {err}")
            return None
    

    def buscar(self, codbar):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM mercado WHERE codbar = ?", (codbar,))
        retorno = cursor.fetchone()
        cursor.close()
        conexao.close()
        
        if (retorno == None):
            return retorno
        else:
            produto_encontrado = produto.Produto(retorno[0], retorno[1], retorno[2], retorno[3], retorno[4])
            return produto_encontrado
        
    

    def atualizar(self, produto):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("UPDATE mercado SET nome = ?, estoque = ?, loc = ?, preco = ? WHERE codbar = ?", (produto.nome, produto.estoque, produto.loc, produto.preco, produto.codbar))
        conexao.commit()

        conf = cursor.rowcount > 0
        cursor.close()
        conexao.close()
        return conf


    def deletar(self, id):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM mercado WHERE codbar = ?", (id,))
        retorno = cursor.fetchone()
        if (retorno == None):
            cursor.close()
            conexao.close()
            return retorno
        else:
            cursor.execute("DELETE FROM mercado WHERE codbar = ?", (id,))
            conexao.commit()
            produto_encontrado = produto.Produto(retorno[0], retorno[1], retorno[2], retorno[3], retorno[4])
            cursor.close()
            conexao.close()
            return produto_encontrado
