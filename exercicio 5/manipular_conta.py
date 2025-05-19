from ex5 import ContaBancaria

conta = ContaBancaria(1000)

while True:
    selecionar = int(input(f"\n---Escolha uma das opcoes para manipular sua conta bancaria ---\n 1. Depositar\n 2. Sacar\n 3. Extrato da conta\n 4. Sair\n ---------------\n"))
    if selecionar == 1:
        try:
            valor = float(input(f"Digite o valor que deseja depositar: "))
            conta.depositar(valor)
        except ValueError:
            print(f"--- Digite um valor numerico valido. ---")
    elif selecionar == 2:
        try:
            valor = float(input(f"Digite o valor que deseja sacar: "))
            conta.sacar(valor)
        except ValueError:
            print(f"--- Digite um valor valido. ----")
    elif selecionar == 3:
        conta.extrato()
    elif selecionar == 4:
        break
    else:
        print(f"Opcao invalida, tente novamente")