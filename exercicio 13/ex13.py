class Produto:
    def __init__(self, preco):
        # Inicializa o preço do produto com o valor passado ao criar o objeto
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        # Calcula o valor do desconto com base na porcentagem informada
        desconto = self.preco * (porcentagem / 100)
        # Subtrai o desconto do preço original
        self.preco -= desconto
        return self.preco

preco = float(input("Digite o preço do produto: "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

# Cria um objeto Produto com o preço informado
produto = Produto(preco)
# Aplica o desconto informado e armazena o novo preço
novo_preco = produto.aplicar_desconto(porcentagem)
print(f"Preço com desconto: {novo_preco}")