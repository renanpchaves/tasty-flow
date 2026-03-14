from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao, categoria):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.categoria = categoria

    def __str__(self):
        return self._nome
    
    def desconto(self):
        self._preco -= (self._preco*0.05)
        return super().desconto()
    
    # ===== PROPERTIES PRO PYDANTIC (todict()) =====

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco