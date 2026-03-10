from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, desc):
        super().__init__(nome, preco)
        self.desc = desc

    def __str__(self):
        return self._nome