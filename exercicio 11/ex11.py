class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'\n{self.nome} tem {self.idade} anos.'
    
fulano = Pessoa("Gabriel", 21)
ciclano = Pessoa("Marocs", 18)

print(str(fulano))
print(str(ciclano))
