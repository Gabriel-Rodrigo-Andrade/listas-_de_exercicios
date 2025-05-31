class Pedido:
    def __init__(self):
        self.nomes = []
        self.precos = []

    def adicionar_produto(self, nome, preco):
        self.nomes.append(nome)
        self.precos.append(preco)

    def calcular_total(self):
        return sum(self.precos)


pedido = Pedido()
pedido.adicionar_produto("Durateston", 120.0)
pedido.adicionar_produto("Deca-Durabolin", 150.0)
pedido.adicionar_produto("Hemogenin", 200.0)

print("Produtos no pedido:")
#zip pega 1 elemento de cada lista e faz um par (primeiro nome + primeiro preco...)
for nome, preco in zip(pedido.nomes, pedido.precos):
    #.2f usado para formatar a string com dois (120.00 ao invés de 120)
    print(f"{nome}: R$ {preco:.2f}")

print(f"\nTotal do pedido: R$ {pedido.calcular_total():.2f}")