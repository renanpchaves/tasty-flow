from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida:
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome,preco)
        self._tamanho = tamanho