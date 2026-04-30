import sqlite3
import produto

class DB:

    def __init__(self):
        self.conexao = sqlite3.connect("database.db")
        cursor = self.conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mercado(codbar INTEGER PRIMARY KEY, nome, estoque, loc, preco)")
        self.conexao.commit()
        cursor.close()


    def inserir(self, produto):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO mercado(codbar, nome, estoque, loc, preco) VALUES (?, ?, ?, ?, ?)", (produto.codbar, produto.nome, produto.estoque, produto.loc, produto.preco))

            if (cursor.rowcount > 0):
                id = cursor.lastrowid
            else:
                id = None

            self.conexao.commit()
            cursor.close()
            return id
        except sqlite3.IntegrityError:
            return -1
        except Exception as err:
            print(f"Erro inesperado: {err}")
            return None
    

    def buscar(self, codbar):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mercado WHERE codbar = ?", (codbar,))
        retorno = cursor.fetchone()
        cursor.close()
        
        if (retorno == None):
            return None
        else:
            produto_encontrado = produto.Produto(retorno[0], retorno[1], retorno[2], retorno[3], retorno[4])
            return produto_encontrado
        
    

    def atualizar(self, produto):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE mercado SET nome = ?, estoque = ?, loc = ?, preco = ? WHERE codbar = ?", (produto.nome, produto.estoque, produto.loc, produto.preco, produto.codbar))
        self.conexao.commit()

        conf = cursor.rowcount > 0
        cursor.close()
        return conf


    def deletar(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM mercado WHERE codbar = ?", (id,))
        self.conexao.commit()
        cursor.execute("SELECT * FROM mercado WHERE codbar = ?", (id,))
        retorno = cursor.fetchone()
        cursor.close()
        return retorno
