class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_detalhes(self):
        print (f"Nome do produto: {self.nome} \n Preco: {self.preco}")
        print (f"----------------------")