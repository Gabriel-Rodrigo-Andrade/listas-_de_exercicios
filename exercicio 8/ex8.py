import time

class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def mostrar_hora(self):
        #O :02d em uma f-string serve para formatar números inteiros
        print(f"\n-----------HORARIO------------\n{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}")

horario_f1 = Relogio(4, 20, 0)
horario_f1.mostrar_hora()

horario_tristeza = Relogio(8, 30 , 1)
horario_tristeza.mostrar_hora()

horario_felicidade = Relogio(18, 0, 1)
horario_felicidade.mostrar_hora()