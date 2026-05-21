import database

class MercadoCRUD:
    def __init__(self):
        self.db = database.DB()

    def inserir(self, produto):
        return  self.db.inserir(produto)

    def buscar(self, codbar):
        return self.db.buscar(codbar)

    def atualizar(self, produto):
        return self.db.atualizar(produto)

    def deletar(self, codbar):
        return self.db.deletar(codbar)
    
    def inserir_categoria(self, nome):
        return self.db.inserir_categoria(nome)
    
    def buscar_categoria(self, nome):
        return self.db.buscar_categoria(nome)
    
    def deletar_categoria(self, nome):
        return self.db.deletar_categoria(nome)
    
    def listar_produtos_por_categoria(self, nome):
        return self.db.listar_produtos_por_categoria(nome)