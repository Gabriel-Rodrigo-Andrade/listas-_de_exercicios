import time

class CaixaDAgua:
    def __init__(self,capacidade_max, volume_atual):
        self.capacidade_max = capacidade_max
        self.volume_atual = volume_atual

    def encher(self):
        self.volume_atual = self.capacidade_max
        print(f"\nA caixa de agua esta cheia, com {self.capacidade_max} Litros.")

    def esvaziar(self):
        self.volume_atual = 0
        print(f"\nA caixa de agua esta vaazia, com {self.volume_atual}, Litros")

agua = CaixaDAgua(3.000, 1.000)
while True:
    selecao = int(input(f"\nEsvaziar ou Encher caixa d' agua\n1. Encher\n2. Esvaziar\n"))
    if selecao == 1:
        agua.encher()
    elif selecao == 2:
        agua.esvaziar()
    else:
        print(f"\nOpção Invalida, tente novamente.\n")
    time.sleep(2)