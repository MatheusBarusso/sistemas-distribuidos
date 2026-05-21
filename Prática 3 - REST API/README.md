# CRUD por REST API

## Descrição do Problema

Na Atividade 1 o sistema CRUD foi implementado por meio de Sockets e envio de mensagens preparadas manualmente em bytes. Na Atividade 2 o sistema CRUD foi implementado utilizando middleware de RMI **Pyro**.

Para esta atividade o trabalho deve ser implementado por meio de REST, mantendo as funcionalidades do CRUD, mas agora com WebServices.

## Requisitos

- Validar as requisições recebidas para campos esperados e valores recebidos, com os valores fazendo sentido para o sistema implementado.
- Definir as rotas entre os verbos HTTP e os métodos da(s) classe(s) implementada(s).
- Utilizar os códigos HTTP corretos para erros e acertos.
- Utilizar os verbos HTTP corretos para as requisições.
- Adicionar um recurso que se relacione ao CRUD implementado anteriormente e que possa ser manipulado ao menos pelas operações de inserção e busca.
    - O segundo recurso pode ser feito com uma segunda classe para manipular ou simplificado, em forma de uma string, ou na mesma classe do CRUD.


## Execução

### 1. Iniciar o Webserver

Em um terminal, execute:

```bash
uvicorn main:app --reload
```

O WebServer Uvicorn roda por padrão na porta :8000

### 2. Acessar interface FastAPI

Em um navegador acessar:

```
http://127.0.0.1:8000/docs
```
