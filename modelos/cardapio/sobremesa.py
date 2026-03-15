from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return self._nome

    def desconto(self):
        self._preco -= (self._preco*0.10)
        return super().desconto()
    
    # ===== PROPERTIES PRO PYDANTIC (todict()) =====

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco