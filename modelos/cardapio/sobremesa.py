from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, desc, tipo, tamanho):
        super().__init__(nome, preco)
        self.desc = desc
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

    def desconto(self):
        self._preco -= (self._preco*0.10)
        return super().desconto()