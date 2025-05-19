import time
class ContaBancaria:

    def __init__(self, valor_disponivel):
        self.valor_disponivel = valor_disponivel
        self.deposito = []
        self.saque = []

    def depositar(self, valor):
        self.deposito.append(valor)
        self.valor_disponivel += valor
        print(f"------- SUCESSO --------\n")
        print(f"O valor {valor} foi depositado")
        time.sleep(3)

    def sacar(self, valor):
        if valor <= self.valor_disponivel:
            self.saque.append(valor)
            self.valor_disponivel -= valor
            print(f"------- SUCESSO --------\n")
            print(f"O valor {valor} foi sacado\n --------------")
            time.sleep(3)
        else:
            print(f"------- ERRO AO SACAR --------\n")
            print(f"Voce nao tem este valor disponivel para saque, verifique seu extrato e solicite um saque válido\n --------------")
            time.sleep(3)

    def extrato(self):
        print(f"------ EXTRATO DA CONTA ------\n")
        print(f"Depositos: {self.deposito}\n")
        print(f"Saques: {self.saque}\n")
        print(f"Saldo disponivel: {self.valor_disponivel}\n ----------")
        time.sleep(5)