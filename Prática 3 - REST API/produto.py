class Produto:
    def __init__(self, codbar, nome, estoque, loc, preco, categoria_id=None):
        self.codbar = codbar
        self.nome = nome
        self.estoque = estoque
        self.loc = loc
        self.preco = preco
        self.categoria_id = categoria_id
