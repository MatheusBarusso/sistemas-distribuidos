import database
import Pyro5.api

@Pyro5.api.expose
class MercadoCRUD:
    def __init__(self):
        self.db = database.DB()

    def inserir(self, produto):
        return self.db.inserir(produto)

    def buscar(self, codbar):
        return self.db.buscar(codbar)

    def atualizar(self, produto):
        return self.db.atualizar(produto)

    def deletar(self, codbar):
        return self.db.deletar(codbar)