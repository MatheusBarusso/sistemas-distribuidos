# CRUD com Sockets

## Descrição do Problema

Este projeto consiste no desenvolvimento de um sistema do tipo **CRUD (Create, Read, Update, Delete)** utilizando **comunicação via sockets**.

O sistema deve permitir a manipulação de um recurso à escolha (por exemplo: agenda de contatos, controle de estoque, cadastro de usuários, etc.), implementando operações básicas de:

- **Create (Inserção)**: adicionar novos registros
- **Read (Leitura)**: consultar registros a partir de uma chave
- **Update (Atualização)**: alterar dados de um registro existente
- **Delete (Remoção)**: excluir registros a partir de uma chave

## Comunicação Cliente-Servidor

O sistema deve operar em um modelo **cliente-servidor**, onde:

- O cliente envia requisições ao servidor via socket
- O servidor processa essas requisições e retorna respostas
- Todas as operações devem ocorrer **na mesma conexão**, que permanece aberta até o cliente encerrar

## Estrutura de Comunicação

Deve ser implementado um **formato próprio de pacote de dados**, responsável por:

- Identificar o tipo de operação (CRUD)
- Transportar os parâmetros necessários
- Codificar e decodificar as informações transmitidas

Importante:
- Não é permitido utilizar serialização pronta (como JSON, XML, etc.)
- A codificação dos dados deve ser implementada manualmente

## Modelagem dos Dados

O recurso escolhido deve:

- Possuir **pelo menos 5 atributos**
- Incluir **tipos de dados variados** (ex: texto e número)
- Ter uma **chave primária** para identificação dos registros

Regras adicionais:
- Caso utilize um `id` numérico como chave primária:
  - Deve existir pelo menos **mais um atributo numérico**
  - O `id` **não conta** como um dos 5 atributos mínimos (totalizando 6 atributos)

## Armazenamento

Os dados devem ser armazenados em um **banco de dados**, seguindo estas diretrizes:

- Cada atributo deve ser armazenado separadamente (não como uma única string)
- O sistema deve manipular diretamente os campos estruturados

## Processamento das Requisições

Ao receber um pacote, o servidor deve:

1. Identificar o tipo de operação solicitada
2. Interpretar corretamente os parâmetros recebidos
3. Executar a ação correspondente no banco de dados
4. Retornar uma resposta adequada ao cliente