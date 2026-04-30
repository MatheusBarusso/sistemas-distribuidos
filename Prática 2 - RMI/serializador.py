from Pyro5.api import register_class_to_dict, register_dict_to_class
from produto import Produto

def produto_para_dict(objeto):
    return {
        "__class__": "produto.Produto",
        "codbar": objeto.codbar,
        "nome": objeto.nome,
        "estoque": objeto.estoque,
        "loc": objeto.loc,
        "preco": objeto.preco
    }

def dict_para_produto(nome_classe, dicionario):
    return Produto(
        dicionario["codbar"],
        dicionario["nome"],
        dicionario["estoque"],
        dicionario["loc"],
        dicionario["preco"]
    )

def registrar_serializadores():
    register_class_to_dict(Produto, produto_para_dict)
    register_dict_to_class("produto.Produto", dict_para_produto)