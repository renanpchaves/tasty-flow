from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def buscar_nome(cls, nome):
        """
        Busca o restaurante por nome
        """
        for restaurante in cls.restaurantes:
            if restaurante._nome.lower() == nome.lower():
                return restaurante
        return None

    # ===== PROPERTIES PÚBLICAS PARA PYDANTIC =====
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def total_avaliacoes(self):
        return len(self._avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0.0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    @property
    def ativo(self):
        return self._ativo
    
    # ===== MÉTODOS DE NEGÓCIO =====
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    # Antigos metodos para exibir cardapio no app.py, antes de evoluir pra API.
    # @classmethod
    # def listar_restaurantes(cls):
    #     print(
    #         f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}"
    #     )
    #     for restaurante in cls.restaurantes:
    #         print(
    #             f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}"
    #         )
    # @property
    # def exibir_cardapio(self):
    #     print(f"Cardapio do restaurante {self._nome}: \n")
    #     for i, item in enumerate(self._cardapio, start=1):
    #         if hasattr(item, "desc"):
    #             mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.desc}"
    #             print(mensagem_prato)
    #         elif hasattr(item, "sabor"):
    #             mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho} | Sabor: {item.sabor}"
    #             print(mensagem_bebida)
    #         elif hasattr(item, "tipo"):
    #             mensagem_sobremesa = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tipo: {item.tipo} | Tamanho: {item.tamanho}"
    #             print(mensagem_sobremesa)