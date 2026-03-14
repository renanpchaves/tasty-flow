from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho, sabor):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        self.sabor = sabor


    def __str__(self):
        return self._nome
    
    def desconto(self):
        self._preco -= (self._preco * 0.08)
        return super().desconto()
    
    # ===== PYDANTIC (to_dict()) =====

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco