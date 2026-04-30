class Produto:
    def __init__(self, codbar, nome, estoque, loc, preco):
        self.codbar = codbar
        self.nome = nome
        self.estoque = estoque
        self.loc = loc
        self.preco = preco

produto1 = Produto(123456, "Arroz", 20, 4, 25.90)
produto2 = Produto(1234567, "Arroz2", 21, 5, 30.90)

print(produto1.codbar, produto2.codbar)