class Pessoa:
    # Método construtor, inicializa os atributos nome e idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para mostrar o nome da pessoa
    def mostrar_nome(self):
        print(f"Nome da pessoa: {self.nome}")

    # Método para mostrar a idade da pessoa
    def mostrar_idade(self):
        print(f"Idade: {self.idade}")

    def apresentar(self):
        print(f"\nOlá, meu nome é {self.nome} e tenho {self.idade} anos")