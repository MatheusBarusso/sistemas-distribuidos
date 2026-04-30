import produto 
import crud
import Pyro5.api
from serializador import registrar_serializadores

registrar_serializadores()

ns = Pyro5.api.locate_ns()
uri = ns.lookup("Matheus.Barusso")
server = Pyro5.api.Proxy(uri)



while True:
    print('┌──────────────────────────────────────────────────────────────────┐')
    opcao = input('| Choose an option (C)reate, (R)ead, (U)pdate, (D)elete or (E)xit  |\n| ')
    print('└──────────────────────────────────────────────────────────────────┘\n\n')  

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

            produto_criado = produto.Produto(codbar, nome, estoque, loc, preco)

            server.inserir(produto_criado)


        case 'R':  
                print('\n\n┌──────────────────────────────────────────────────────┐')
                id = int(input('| Insert the Codebar: '))
                resposta = server.buscar(id)

                if (resposta == None):
                    print("| \n| Product not found!")
                    print('└──────────────────────────────────────────────────────┘\n\n')
                else:
                    print('| \n| Product found!\n|\n| Name:', resposta.nome, '\n| Quantity in Stock:', resposta.estoque, '\n| Barcode:', resposta.codbar, '\n| Aisle:', resposta.loc, '\n| Price:', resposta.preco)
                    print('└──────────────────────────────────────────────────────┘\n\n')


        case 'U':
                print('\n\n┌──────────────────────────────────────────────────────┐')
                id = int(input('| Insert the Codebar: '))
                resposta = server.buscar(id)

                if (resposta == None):
                    print('|\n| Product not found, try again.')
                    print('└──────────────────────────────────────────────────────┘\n\n')
                else:
                    print('|\n| Product found! Insert the updated values: \n|')
                    nome = input('| Name: ')
                    estoque = int(input('| Quantity in Stock: '))
                    loc = int(input('| Aisle: '))
                    preco = float(input('| Price: '))
                    codbar = id
                    print('└──────────────────────────────────────────────────────┘\n\n')
    
                    produto_atualizado = produto.Produto(codbar, nome, estoque, loc, preco)

                    status = server.atualizar(produto_atualizado)

                    if (status == -1):
                        print('┌──────────────────────────────────────────────────────┐')
                        print('| Error in updating info\n\n')
                        print('└──────────────────────────────────────────────────────┘\n\n')
                    else:
                        print('┌──────────────────────────────────────────────────────┐')
                        print('| Info updated for selected Barcode!')
                        print('└──────────────────────────────────────────────────────┘\n\n')
            
        
        case 'D':
                print('\n\n┌──────────────────────────────────────────────────────┐')
                id = int(input('| Insert the Codebar: '))

                status = server.deletar(id)
                if (status == None):
                    print('|\n| Product deleted!\n')
                else:
                    print('|\n| Product not found, try again.\n')
                print('└──────────────────────────────────────────────────────┘\n\n')
        

        case 'E':
            print('| Closing the connection')
            print('└──────────────────────────────────────────────────────┘\n\n')  
            break      
         
        








                


