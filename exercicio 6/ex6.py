import time

class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        print(f"{self.velocidade + qual_acelereacao}")
        time.sleep(3)

    def frear(self):
        self.velocidade = max(0, self.velocidade - qual_frenagem)
        print(f"A velocidade atual e: {self.velocidade} Km/h\n")
        time.sleep(3)

carro1 = Carro("Mercedes", "A45 AMG", 180)
carro2 = Carro("BMW", "M3 competition", 230)

while True:
    selecao = int(input(f"--- Qual carro deseja controlar ? ---\n1. {carro1.marca}, {carro1.modelo}\n2. {carro2.marca}, {carro2.modelo}\n"))
    if selecao == 1:
        try:
            while True:
                controle = int(input(f"------------\n1. Acelerar\n2. Frear\n"))
                if controle ==  1:
                    qual_acelereacao = int(input(f"------------\nQuantos Km irao ser adicionados: "))
                    carro1.acelerar()
                if controle == 2:
                    qual_frenagem = int(input(f"------------\nQuantos Km irao ser diminuidos: "))
                    carro1.frear()
                else:
                    print(f"\n-------------\nOpção invalida, tente novamente.")
                    time.sleep(2)
        except ValueError:
            print(f"\n-------OPCAO INVALIDA---------")

    if selecao == 2:
            try:
                while True:
                    controle = int(input(f"------------\n1. Acelerar\n2. Frear\n"))
                    if controle ==  1:
                        qual_acelereacao = int(input(f"------------\nQuantos Km irao ser adicionados: "))
                        carro2.acelerar()
                    if controle == 2:
                        qual_frenagem = int(input(f"------------\nQuantos Km irao ser diminuidos: "))
                        carro2.frear()
                    else:
                        print(f"\n-------------\nOpção invalida, tente novamente.")
                        time.sleep(2)

            except ValueError:
                print(f"\n-------OPCAO INVALIDA---------")

    else:
        print(f"\n-------------\nOpção invalida, tente novamente.\n-------------\n")
        time.sleep(2)