class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        print(f"A area do retangulo e: {self.largura * self.altura}")

    def calcular_perimetro(self):
        print(f"O perimetro deste triangulo e: {2* (self.largura + self.altura)}")