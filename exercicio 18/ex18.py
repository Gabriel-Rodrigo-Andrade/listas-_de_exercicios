class Cadastro:
    def __init__(self):
        #O parâmetro pessoa seria usado apenas se você quisesse criar o objeto já com uma lista de nomes
        self.pessoa = []

    def adicionar_nome(self, nome):
        self.pessoa.append(nome)
    
    def listar_pessoas (self):
        for i in enumerate(self.pessoa):
            print(f"{i}")

cadastro = Cadastro()

while True:
    selecao = int(input(f"\n1. Adicionar nome\n2. Listar nomes\n3. Finalizar operacao\n\n"))
    if selecao == 1:
        nome = str(input(f"\nDigite o nome da pessoa a ser adicionada: "))
        cadastro.adicionar_nome(nome)
    elif selecao == 2:
        cadastro.listar_pessoas()
    elif selecao == 3:
        break
    else:
        print(f"\nOpcao Invalida, digite uma opcao valida!\n")
