import database
import Pyro5.api

@Pyro5.api.expose
class MercadoCRUD:
    def __init__(self):
        self.db = database.DB()
        self.daemon = None

    def set_daemon(self, daemon):
        self.daemon = daemon

    def desligar(self):
        if self.daemon is not None:
            print('┌────────────────────────────────────────────┐')
            print('| Client closed the connection to the server')
            print('└────────────────────────────────────────────┘')
            self.daemon.shutdown()

    def inserir(self, produto):
        return  self.db.inserir(produto)

    def buscar(self, codbar):
        return self.db.buscar(codbar)

    def atualizar(self, produto):
        return self.db.atualizar(produto)

    def deletar(self, codbar):
        return self.db.deletar(codbar)