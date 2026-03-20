import socket
import struct #p decode o float -> sem conversao direta

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET -> Rede Interna
#manda dados p/ server

endereco = ('127.0.0.1', 55555) #Localhost - Porta 50K+
sock.connect(endereco)

while True:
    print('┌──────────────────────────────────────────────────────────────────┐')
    opcao = input('| Choose an option (C)reate, (R)ead, (U)pdate, (D)elete or (E)xit |\n└──────────────────────────────────────────────────────────────────┘\n')

    match opcao:
        case 'C':
            print('\n\n┌──────────────────────────────────────────────────────┐')
            print('| Insert the following informations about the product: |')
            nome = input('| Name: ')
            estoque = int(input('| Quantity in Stock: '))
            codbar  = int(input('| Barcode: '))
            loc = int(input('| Aisle: '))
            preco = float(input('| Price: '))
            print('└──────────────────────────────────────────────────────┘\n\n')
            nome_b = nome.encode()

            mensagem = opcao.encode()
            mensagem += len(nome_b).to_bytes(1, 'big') + nome_b #recebe tamanho e ordem dos bits (LSB / MSB) -> big/little endian
            mensagem += estoque.to_bytes(4, 'big')
            mensagem += codbar.to_bytes(6, 'big')
            mensagem += loc.to_bytes(1, 'big')
            mensagem += struct.pack('>d', preco) #bytes decimal

            sock.send(mensagem)
            status_b = sock.recv(2) #numero de bytes a serem lidos
            status = int.from_bytes(status_b, 'big', signed=True)
            if (status == -1):
                print('Error in registering\n\n')
            else:
                print('Registered using Barcode as id\n\n')

        case 'R':
            print('\n\n┌──────────────────────────────────────────────────────┐')
            id = int(input('| Insert the Codebar: '))
            mensagem = opcao.encode() + id.to_bytes(6, 'big')
            sock.send(mensagem)

            tam = int.from_bytes(sock.recv(1), 'big')
            nome = sock.recv(tam).decode()
            estoque = int.from_bytes(sock.recv(4), 'big')
            loc = int.from_bytes(sock.recv(1), 'big')
            preco = struct.unpack('>d', sock.recv(8))[0]

            print('| \n| Product found!\n|\n| Name:', nome, '\n| Quantity in Stock:', estoque, '\n| Barcode:', id, '\n| Aisle:', loc, '\n| Price:', preco)
            print('└──────────────────────────────────────────────────────┘\n\n')


        case 'U':
            while True: 
                print('\n\n┌──────────────────────────────────────────────────────┐')
                id = int(input('| Insert the Codebar: '))
                mensagem = opcao.encode() + id.to_bytes(6, 'big')
                sock.send(mensagem)

                status_b = sock.recv(2)
                status = int.from_bytes(status_b, 'big', signed=True)
                if (status == 1):
                    print('|\n| Product not found, try again.')
                if (status == 0):
                    print('|\n| Product found! Insert the updated values: ')
                    nome = input('| Name: ')
                    estoque = int(input('| Quantity in Stock: '))
                    loc = int(input('| Aisle: '))
                    preco = float(input('| Price: '))
                    print('└──────────────────────────────────────────────────────┘\n\n')
    
                    nome_b = nome.encode()
                    mensagem = len(nome_b).to_bytes(1, 'big') + nome_b
                    mensagem += estoque.to_bytes(4, 'big')
                    mensagem += loc.to_bytes(1, 'big')
                    mensagem += struct.pack('>d', preco)
                    sock.send(mensagem)

                    status_b = sock.recv(2) #numero de bytes a serem lidos
                    status = int.from_bytes(status_b, 'big', signed=True)
                    if (status == -1):
                        print('Error in updating info\n\n')
                        break
                    else:
                        print('Info updated for selected Barcode!\n\n')
                        break








                


