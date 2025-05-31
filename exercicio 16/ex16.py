class CaixaRegistradora:
    def __init__(self):
        self._total = 0

    def registrar(self, valor):
        self._total += valor

    def total(self):
        return self._total

caixa = CaixaRegistradora()
caixa.registrar(10)
caixa.registrar(5)
print(caixa.total())
