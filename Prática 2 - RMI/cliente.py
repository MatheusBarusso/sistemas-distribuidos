import produto 
import crud
import Pyro5.api
from serializador import registrar_serializadores
import Pyro5.errors
import os

registrar_serializadores()

ns = Pyro5.api.locate_ns()
uri = ns.lookup("Matheus.Barusso")
server = Pyro5.api.Proxy(uri)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('┌──────────────────────────────────────────────────────────────────┐')
    opcao = input('| Choose an option (C)reate, (R)ead, (U)pdate, (D)elete or (E)xit  |\n| ')
    print('└──────────────────────────────────────────────────────────────────┘')  

    match opcao:
        case 'C':
            print('┌──────────────────────────────────────────────────────┐')
            print('| Insert the following informations about the product: |')
            nome = input('| Name: ')
            estoque = int(input('| Quantity in Stock: '))
            codbar  = int(input('| Barcode: '))
            loc = int(input('| Aisle: '))
            preco = float(input('| Price: '))

            produto_criado = produto.Produto(codbar, nome, estoque, loc, preco)
            resposta = server.inserir(produto_criado)


            if (resposta == -1):
                 print('| Invalid Codebar! Product already registered!')
            elif (resposta == None):
                 print('| Something went wrong')
            else:
                 print('| Product created!')
            
            print('└──────────────────────────────────────────────────────┘\n\n')
            print('┌───────────────────────────────────┐')
            print("| Press enter to continue...")
            input('└───────────────────────────────────┘')
            limpar_tela()



        case 'R':  
                print('┌──────────────────────────────────────────────────────┐')
                id = int(input('| Insert the Codebar: '))
                resposta = server.buscar(id)

                if (resposta == None):
                    print("| \n| Product not found!")
                    print('└──────────────────────────────────────────────────────┘\n\n')
                else:
                    print('| \n| Product found!\n|\n| Name:', resposta.nome, '\n| Quantity in Stock:', resposta.estoque, '\n| Barcode:', resposta.codbar, '\n| Aisle:', resposta.loc, '\n| Price:', resposta.preco)
                    print('└──────────────────────────────────────────────────────┘\n\n')
                
                print('┌───────────────────────────────────┐')
                print("| Press enter to continue...")
                input('└───────────────────────────────────┘')
                limpar_tela()


        case 'U':
                print('┌──────────────────────────────────────────────────────┐')
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

                    if (status == False):
                        print('┌──────────────────────────────────────────────────────┐')
                        print('| Error in updating info\n\n')
                        print('└──────────────────────────────────────────────────────┘\n\n')
                    else:
                        print('┌──────────────────────────────────────────────────────┐')
                        print('| Info updated for selected Barcode!')
                        print('└──────────────────────────────────────────────────────┘\n\n')
                
                print('┌───────────────────────────────────┐')
                print("| Press enter to continue...")
                input('└───────────────────────────────────┘')
                limpar_tela()
            
        
        case 'D':
                print('┌──────────────────────────────────────────────────────┐')
                id = int(input('| Insert the Codebar: '))

                status = server.deletar(id)
                if (status == None):
                    print("| \n| Product not found!")
                    print('└──────────────────────────────────────────────────────┘\n\n')
                else:
                    print('| \n| Following product was deleted!\n|\n| Name:', status.nome, '\n| Quantity in Stock:', status.estoque, '\n| Barcode:', status.codbar, '\n| Aisle:', status.loc, '\n| Price:', status.preco)
                    print('└──────────────────────────────────────────────────────┘\n\n')

                print('┌───────────────────────────────────┐')
                print("| Press enter to continue...")
                input('└───────────────────────────────────┘')
                limpar_tela()
        

        case 'E': 
            try:
                print('┌───────────────────────────┐')
                print('| Closing the connection...')
                print('└───────────────────────────┘\n\n') 
                server.desligar()
            except Pyro5.errors.ConnectionClosedError:
                 pass
            break      
         
        








                


