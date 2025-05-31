class Temperatura:
    def __init__(self, celcius):
        self.celcius = celcius

    def fahrenheit(self):
        return (self.celcius * 9/5) + 32

celcius = float(input("Digite a temperatura em Celsius: "))
temp = Temperatura(celcius)
print(f"Temperatura em Fahrenheit: {temp.fahrenheit()}")