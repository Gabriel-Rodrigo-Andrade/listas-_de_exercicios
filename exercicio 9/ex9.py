import time

class Elevador:
    def __init__(self, andar_atual=0):
        self.andar_atual = andar_atual

    def subir(self, valor):
        self.andar_atual += valor
        print(f"\n-----------------\nSeu andar atual e: {self.andar_atual}\n----------------")
        time.sleep(3)

    def descer(self, valor):
        if self.andar_atual - valor < 0:
            print(f"\nEste elevador nao leva ao subsolo.")
        else:
            self.andar_atual -= valor
            print(f"\n-----------------\nSeu andar atual e: {self.andar_atual}\n-----------------\n")
        time.sleep(3)

andar = Elevador()

while True:
    selecao = int(input(f"\nVoce deseja subir ou descer ?\n1. Subir\n2. Descer\n"))
    if selecao == 1:
        valor = int(input(f"\nQuantos andares deseja subir ?"))
        andar.subir(valor)
    elif selecao == 2: 
        valor = int(input(f"\nQuantos andares deseja descer ?"))
        andar.descer(valor)
    else:
        print(f"\n---Opcao invalida, tente novamente.---")
    time.sleep(2)