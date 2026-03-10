from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, sabor):
        super().__init__(nome, preco)
        self.sabor = sabor

    def __str__(self):
        return self._nome

    def desconto(self):
        self._preco -= (self._preco*0.1)
        return super().desconto()