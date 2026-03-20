import socket
import struct
import database

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET -> Rede Interna

banco = database.DB()

endereco = ('127.0.0.1', 55555) #servidor sobe e espera cliente (TPC) se for UDP cliente antes

sock.bind(endereco) #vincula socket responder nessa porta

sock.listen(10) #n = num de vagas / fila de espera p conexao

[dados, _] = sock.accept() #espera que alguem venha pedir conexao na porta definida -> abre dados tbem
#accept eh bloqueante

while True:
    opcode = dados.recv(1) #ler 1 byte
    if (opcode is None): #verifica erro
        break
    
    opcode = opcode.decode()
    match opcode: 
        case 'C': #literalmente processo de envio mas ao contrario. IMPORTANTE: CONSUMIR BYTES NA ORDEM E TAMANHO CORRETO
            tam = int.from_bytes(dados.recv(1), 'big')
            nome = dados.recv(tam).decode()
            estoque = int.from_bytes(dados.recv(4), 'big')
            codbar = int.from_bytes(dados.recv(6), 'big')
            loc = int.from_bytes(dados.recv(1), 'big')
            preco = struct.unpack('>d', dados.recv(8))[0]

            conf = banco.inserir(codbar, nome, estoque, loc, preco)
            status = 0 if conf else -1

            mensagem = status.to_bytes(2, 'big', signed=True)
            dados.send(mensagem)

        
        case 'R':
            id = int.from_bytes(dados.recv(6), 'big')
            tupla = banco.buscar(id)
            codbar = tupla [0] #maybe remover dps --> ja usa codbar p/ consultar
            nome = tupla[1]
            estoque = tupla[2]
            loc = tupla[3]
            preco = tupla[4]

            nome_b = nome.encode()
            mensagem = len(nome_b).to_bytes(1, 'big') + nome_b
            mensagem += estoque.to_bytes(4, 'big')
            mensagem += loc.to_bytes(1, 'big')
            mensagem += struct.pack('>d', preco)

            dados.send(mensagem)


        case 'U':
            id = int.from_bytes(dados.recv(6), 'big')
            tupla = banco.buscar(id)

            if not tupla:
                status = 1
            else:
                status = 0
                
            mensagem = status.to_bytes(2, 'big', signed=True)
            dados.send(mensagem)

            tam = int.from_bytes(dados.recv(1), 'big')
            nome = dados.recv(tam).decode()
            estoque = int.from_bytes(dados.recv(4), 'big')
            loc = int.from_bytes(dados.recv(1), 'big')
            preco = struct.unpack('>d', dados.recv(8))[0]

            conf = banco.atualizar(id, nome, estoque, loc, preco)
            status = 0 if conf else -1

            mensagem = status.to_bytes(2, 'big', signed=True)
            dados.send(mensagem)





