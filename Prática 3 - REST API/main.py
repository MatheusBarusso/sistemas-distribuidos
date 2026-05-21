from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field #BaseModel -> Cria modelo de dados p/ API // Field -> Validação nos campos
from crud import MercadoCRUD
from produto import Produto

app = FastAPI()
crud = MercadoCRUD()

# Dicionário de respostas HTTP usados
# 201 -> Válido
# 409 -> PK já registrada
# 404 -> Não encontrado
# 200 -> OK
# 500 -> Erro inesperado

class ProdutoEntrada(BaseModel):
    codbar: int = Field(gt = 0)
    nome: str = Field(min_length = 1)
    estoque: int = Field(ge = 0)
    loc: int = Field(gt = 0)
    preco: float = Field(gt = 0)
    categoria: str = Field(min_length=1)

class ProdutoAtualizacao(BaseModel):
    nome: str = Field(min_length = 1)
    estoque: int = Field(ge = 0)
    loc: int = Field(gt = 0)
    preco: float = Field(gt = 0)
    categoria: str = Field(min_length=1)

class CategoriaEntrada(BaseModel):
    nome: str = Field(min_length=1)

#####################

def produto_para_dict(produto):
    return {
        "codbar": produto.codbar,
        "nome": produto.nome,
        "estoque": produto.estoque,
        "loc": produto.loc,
        "preco": produto.preco,
        'categorias_id': produto.categoria_id
    }

####################

@app.get("/produtos/{codbar}")
def buscar_produto(codbar: int): # GET /produtos/codbar -> buscar_produto(codbar) -> db.buscar(codbar) -> JSON ou 404
    produto = crud.buscar(codbar)

    if produto is None:
        raise HTTPException(status_code=404, detail="Product not found!")
    
    return produto



@app.post("/produtos", status_code=status.HTTP_201_CREATED)
def criar_produto(dados: ProdutoEntrada): # POST /produtos -> recebe JSON -> Valida campos -> cria Produto -> crud.inserir() -> 201 Created ou 409/500
    categoria = crud.buscar_categoria(dados.categoria)

    if (categoria is None):
        raise HTTPException(status_code=404, detail="Category not found.")

    novo_produto = Produto(
        dados.codbar,
        dados.nome,
        dados.estoque,
        dados.loc,
        dados.preco,
        categoria["id"]
    )

    resposta = crud.inserir(novo_produto)

    if (resposta == -1):
        raise HTTPException(status_code=409, detail="Invalid Codebar! Product already registered!")

    if (resposta is None):
        raise HTTPException(status_code=500, detail="Unexpected error registering the product.")
    
    return {
        "mensagem": "Product created!",
        "produto": {
            "codbar": novo_produto.codbar,
            "nome": novo_produto.nome,
            "estoque": novo_produto.estoque,
            "loc": novo_produto.loc,
            "preco": novo_produto.preco,
            "categoria": categoria["nome"]
        }
    }



@app.put("/produtos/{codbar}")
def atualizar_produto(codbar: int, dados: ProdutoAtualizacao): # PUT /produtos/{codbar} -> recebe codbar -> novos dados JSON -> valida dados -> verifica se produto existe -> atualiza banco -> 200 OK
    produto_existente = crud.buscar(codbar)
    categoria = crud.buscar_categoria(dados.categoria)

    if (produto_existente is None):
        raise HTTPException(status_code=404, detail="Product not found!")
    
    if (categoria is None):
        raise HTTPException(status_code=404, detail="Category not found.")

    
    produto_atualizado = Produto(
        codbar,
        dados.nome,
        dados.estoque,
        dados.loc,
        dados.preco,
        categoria["id"],
    )

    atualizado = crud.atualizar(produto_atualizado)

    if (atualizado is False):
        raise HTTPException(status_code=500, detail="Unexpected error updating the product.")
    
    return {
        "mensagem": "Product updated!",
        "produto": {
            "codbar": produto_atualizado.codbar,
            "nome": produto_atualizado.nome,
            "estoque": produto_atualizado.estoque,
            "loc": produto_atualizado.loc,
            "preco": produto_atualizado.preco,
            "categoria": categoria["nome"]
        }
    }



@app.delete("/produtos/{codbar}")
def deletar_produto(codbar:int): # DELETE /produtos/{codbar} -> recebe codbar -> crud.deletar(codbar) -> 200 ou 404
    produto_deletado = crud.deletar(codbar)

    if (produto_deletado is None):
        raise HTTPException(status_code=404, detail="Product not found!")
    
    return {
        "mensagem": "Product deleted!",
        "produto": produto_deletado
    }



@app.post("/categorias", status_code=status.HTTP_201_CREATED)
def criar_categoria(dados: CategoriaEntrada): # POST /categorias -> JSON com nome -> valida nome -> insere no banco -> 201
    id_categoria = crud.inserir_categoria(dados.nome)

    if (id_categoria == -1):
        raise HTTPException(status_code=409, detail="Category already registered")
    
    if (id_categoria is None):
        raise HTTPException(status_code=500, detail="Unexpected error creating category.")
    
    return {
        "mensagem": "Category created!",
        "categoria": {
            "id": id_categoria,
            "nome": dados.nome
        }
    }


@app.get("/categorias/{nome}")
def buscar_categoria(nome: str): # GET /categorias/{nome} -> busca pelo nome -> 200 ou 404
    categoria = crud.buscar_categoria(nome)

    if (categoria is None):
        raise HTTPException(status_code=404, detail="Category not found")
    
    return categoria


@app.delete("/categorias/{nome}")
def deletar_categoria(nome: str): # DELETE /categorias/{nome} -> busca pelo nome -> 404 ou 200
    categoria_deletada = crud.deletar_categoria(nome)

    if (categoria_deletada is None):
        raise HTTPException(status_code=404, detail="Category not found")
    
    if (categoria_deletada == "In_Use"):
        raise HTTPException(status_code=409, detail="Category has registered products, unable to delete until it is empty.")
    
    return {
        "mensagem": "Category deleted!",
        "categoria": categoria_deletada
    }



@app.get("/categorias/{nome}/produtos") # GET /categorias{nome} -> busca todos pela categoria -> 404 ou 200
def listar_produtos_por_categoria(nome: str):
    resultado = crud.listar_produtos_por_categoria(nome)

    if (resultado is None):
        raise HTTPException(status_code=404, detail="Category not found")
    
    return resultado
    
