import socket
import struct #p decode o float -> sem conversao direta

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET -> Rede Interna
#manda dados p/ server

endereco = ('127.0.0.1', 55555) #Localhost - Porta 50K+
sock.connect(endereco)

while True:
    opcao = input('Choose an option (C)reate, (R)ead, (U)pdate, (D)delete or (E)xit')

    match opcao:
        case 'C':
            print('Insert the following informations about the training: ')
            nome = input('Name: ')
            carga = int(input('Load: '))
            serie = int(input('Series: '))
            repeticoes = int(input('Repetitions: '))
            dificuldade = float(input('Dificulty: '))
            nome_b = nome.encode()

            mensagem = opcao.encode()
            mensagem += len(nome_b).to_bytes(1, 'big') + nome_b #recebe tamanho e ordem dos bits (LSB / MSB) -> big/little endian
            mensagem += carga.to_bytes(2, 'big')
            mensagem += serie.to_bytes(1, 'little')
            mensagem += repeticoes.to_bytes(1, 'big')
            mensagem += struct.pack('>d', dificuldade) #bytes decimal

            sock.send(mensagem)
            id_b = sock.recv(2) #numero de bytes a serem lidos
            id = int.from_bytes(id_b, 'big', signed=True)
            if (id == -1):
                print('Error in registering')
            else:
                print('Registered with id: ', str(id))
