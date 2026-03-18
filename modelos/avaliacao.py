class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    # ===== PROPERTIES PARA O PYDANTIC =====

    @property
    def cliente(self):
        return self._cliente

    @property
    def nota(self):
        return self._nota