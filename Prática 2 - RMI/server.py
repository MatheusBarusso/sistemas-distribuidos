import Pyro5.api
from crud import MercadoCRUD
from serializador import registrar_serializadores

registrar_serializadores()

daemon = Pyro5.api.Daemon()
ns = Pyro5.api.locate_ns()

crud = MercadoCRUD

uri = daemon.register(crud)
ns.register("Matheus.Barusso", uri)

print("Servidor Pronto")
print("URI:", uri)

daemon.requestLoop()