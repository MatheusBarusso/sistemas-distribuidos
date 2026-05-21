import sqlite3
import produto

class DB:

    def __init__(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mercado(codbar INTEGER PRIMARY KEY, nome, estoque, loc, preco, categoria_id INTEGER, FOREIGN KEY(categoria_id) REFERENCES categorias(id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS categorias(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL UNIQUE)")
        conexao.commit()
        cursor.close()
        conexao.close()


    def inserir(self, produto):
        try:
            conexao = sqlite3.connect("database.db")
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO mercado(codbar, nome, estoque, loc, preco, categoria_id) VALUES (?, ?, ?, ?, ?, ?)", (produto.codbar, produto.nome, produto.estoque, produto.loc, produto.preco, produto.categoria_id))

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
        cursor.execute("SELECT mercado.codbar, mercado.nome, mercado.estoque, mercado.loc, mercado.preco, categorias.nome FROM mercado JOIN categorias ON mercado.categoria_id = categorias.id WHERE mercado.codbar = ?", (codbar,))
        retorno = cursor.fetchone()
        cursor.close()
        conexao.close()
        
        if (retorno == None):
            return retorno
        
        return {
        "codbar": retorno[0],
        "nome": retorno[1],
        "estoque": retorno[2],
        "loc": retorno[3],
        "preco": retorno[4],
        "categoria": retorno[5]
        }
        
    
    def atualizar(self, produto):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("UPDATE mercado SET nome = ?, estoque = ?, loc = ?, preco = ?, categoria_id = ? WHERE codbar = ?", (produto.nome, produto.estoque, produto.loc, produto.preco, produto.categoria_id, produto.codbar))
        conexao.commit()

        conf = cursor.rowcount > 0
        cursor.close()
        conexao.close()
        return conf


    def deletar(self, codbar):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT mercado.codbar, mercado.nome, mercado.estoque, mercado.loc, mercado.preco, categorias.nome FROM mercado JOIN categorias ON mercado.categoria_id = categorias.id WHERE mercado.codbar = ?", (codbar,))
        retorno = cursor.fetchone()
        if (retorno == None):
            cursor.close()
            conexao.close()
            return retorno
        else:
            produto_deletado = {
                "codbar": retorno[0],
                "nome": retorno[1],
                "estoque": retorno[2],
                "loc": retorno[3],
                "preco": retorno[4],
                "categoria": retorno[5]
            }
            cursor.execute("DELETE FROM mercado WHERE codbar = ?", (codbar,))
            conexao.commit()
            cursor.close()
            conexao.close()
            return produto_deletado
        

    def inserir_categoria(self, nome):
        try:
            conexao = sqlite3.connect("database.db")
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO categorias(nome) VALUES (?)", (nome,))
            id_categoria = cursor.lastrowid
            conexao.commit()
            cursor.close()
            conexao.close()
            return id_categoria
        
        except sqlite3.IntegrityError:
            return -1
        except Exception as err:
            print(f"Unexpect error: {err}")
            return None
    
    def buscar_categoria(self, nome):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM categorias WHERE LOWER(nome) = LOWER(?)", (nome,))
        retorno = cursor.fetchone()
        cursor.close()
        conexao.close()

        if retorno is None:
            return None
        
        return {
            "id": retorno[0],
            "nome": retorno[1]
        }
    
    def deletar_categoria(self, nome):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM categorias WHERE LOWER(nome) = LOWER(?)", (nome,))
        retorno = cursor.fetchone()
        
        if (retorno is None):
            cursor.close()
            conexao.close()
            return None
        
        id_categoria = retorno[0]

        cursor.execute("SELECT COUNT(*) FROM mercado WHERE categoria_id = ?", (id_categoria,))

        quantidade_produtos = cursor.fetchone()[0]

        if (quantidade_produtos > 0):
            cursor.close()
            conexao.close()
            return "In_Use"
        
        cursor.execute("DELETE FROM categorias WHERE id = ?", (retorno[0],))
        conexao.commit()

        categoria_deletada = {
            "id": retorno[0], 
            "nome": retorno[1]
        }

        cursor.close()
        conexao.close()

        return categoria_deletada
    

    def listar_produtos_por_categoria(self, nome_categoria):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM categorias WHERE LOWER(nome) = LOWER(?)", (nome_categoria,))
        categoria = cursor.fetchone()

        if (categoria is None):
            cursor.close()
            conexao.close()
            return None
        
        id_categoria = categoria[0]

        cursor.execute("SELECT mercado.codbar, mercado.nome, mercado.estoque, mercado.loc, mercado.preco, categorias.nome FROM mercado JOIN categorias ON mercado.categoria_id = categorias.id WHERE mercado.categoria_id = ?", (id_categoria,))

        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()

        return {
            "categoria": {
                "id": categoria[0],
                "nome": categoria[1]
            },
            "produtos": [
                {
                    "codbar": p[0],
                    "nome": p[1],
                    "estoque": p[2],
                    "loc": p[3],
                    "preco": p[4],
                    "categoria": p[5]
                }
                for p in produtos
            ]
        }
