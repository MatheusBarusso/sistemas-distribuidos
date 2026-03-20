import sqlite3

class DB:

    def __init__(self):
        self.conexao = sqlite3.connect("database.db")
        cursor = self.conexao.cursos()
        cursor.execute("CREATE TABLE IF NOT EXISTS academia(id INTEGER PRIMARY KEY, nome, carga, serie, repeticoes, dificuldade)")
        self.conexao.commit()
        cursor.close()

    def inserir(self, nome, carga, serie, repeticoes, dificuldade):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO academia(nome, carga, serie, repeticoes, dificuldade) VALUES (?, ?, ?, ?, ?)", (nome, carga, serie, repeticoes, dificuldade))

        if (cursor.rowcount > 0):
            id = cursor.lastrowid
        else:
            id = None

        self.conexao.commit()
        cursor.close()
        return id