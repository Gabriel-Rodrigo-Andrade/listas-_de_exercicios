import time

class Contator:
    def __init__(self, valor):
        self.valor = valor

    def incrementar(self):
        self.valor += 1

    def zerar(self):
        self.valor = 0

    def mostrar(self):
        print(f"Valor atual do contador: {self.valor}")

contador = Contator(0)

while True:
    selecao = int(input(f"\n1. Adicionar\n2. Zerar\n3. Mostrar\n\n"))
    if selecao == 1:
        contador.incrementar()
        print("Valor incrementado! - "{contador.valor})
    elif selecao == 2:
        contador.zerar()
        print("Contador zerado! - "{contador.valor})
    elif selecao == 3:
        contador.mostrar()
    else:
        print(f"\n-------------\nOpção invalida, tente novamente.\n-------------\n")
        time.sleep(2)