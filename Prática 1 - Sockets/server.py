import socket
import struct
import database

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET -> Rede Interna

banco = database

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
            carga = int.from_bytes(dados.recv(2), 'big')
            serie = int.from_bytes(dados.recv(1), 'little')
            repeticoes = int.from_bytes(dados.recv(1), 'big')
            dificuldade = struct.unpack('>d', dados.recv(8))

            id = banco.inserir(nome, carga, serie, repeticoes, dificuldade)
            if id is None:
                id = -1 

            mensagem =id.to_bytes(2, 'big', signed=True)
            dados.send(mensagem)


