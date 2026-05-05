# CRUD por RMI

## Descrição do Problema

Na Atividade 1 o sistema CRUD foi implementado por meio de Sockets e envio de mensagens preparadas manualmente em bytes.

Para esse trabalho o sistema deve usar middleware de RMI **Pyro**, mantendo o funcionamento do CRUD implementado na atividade 1.

## Requisitos

- O sistema deve se tornar orientado a objetos (uma classe do CRUD com os devidos métodos) e serem disponibilizados repotamente. O RMI já faz a codificação de parâmetros, portanto as chamadas dos métodos devem ser feitas como se fosse em uma chamada local.
- Os métodos de busca e remoção do CRUD **devem retornar objeto(ou lista de objetos, se for um buscar tudo), e ao menos o método de inserção deve receber um objeto como parâmetro (o de atualização pode, opcialmente, receber um objeto com os dados a serem atualizados).**
- Um relatório deve ser elaborado com base em captures do software **Wireshark**, analisando:
    - Qual protocolo de transporte foi utilizado.
    - Como a mensagem foi codificada (como o método foi identificado, quais campos existiam no pacote do Pyro e outras informações relevantes).
    - Troca inicial entre cliente e servidor.
- Para o **nameservice** utilizar os primeiro e últino nome.

## Execução

### 1. Iniciar o Name Server do Pyro

Em um terminal, execute:

```bash
pyro5-ns
```

O Name Server roda, por padrão, na porta `9090`.

### 2. Iniciar o servidor

Em outro terminal, execute o servidor:

```bash
python servidor.py
```


### 3. Iniciar o cliente

Em outro terminal, execute:

```bash
python cliente.py
```

O cliente deve localizar o objeto remoto registrado no Name Server, criar o proxy e permitir que o usuário execute as operações do CRUD pelo menu.
