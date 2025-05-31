class Aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        media_semestre = (self.nota1 + self.nota2) / 2
        return media_semestre

    def aprovado(self):
        # Chama o método media() para obter a média do aluno
        if self.media() >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

informar_nota1 = float(input(f"\nDigite qual foi sua nota no PRIMEIRO bimestre: "))
informar_nota2 = float(input(f"\nDigite qual foi sua nota no SEGUNDO bimestre: "))
notas = Aluno(informar_nota1, informar_nota2)
print(f"Média: {notas.media()}")
print(f"Situação: {notas.aprovado()}")