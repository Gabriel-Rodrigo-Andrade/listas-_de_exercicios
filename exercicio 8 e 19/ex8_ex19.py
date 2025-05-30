import time

class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, value):
        if not (0 <= value <= 23):
            raise ValueError("A hora deve estar entre 0 e 23")
        self._hora = value

    @property
    def minuto(self):
        return self._minuto

    @minuto.setter
    def minuto(self, value):
        if not (0 <= value <= 59):
            raise ValueError("O minuto deve estar entre 0 e 59")
        self._minuto = value

    @property
    def segundo(self):
        return self._segundo

    @segundo.setter
    def segundo(self, value):
        if not (0 <= value <= 59):
            raise ValueError("O segundo deve estar entre 0 e 59")
        self._segundo = value

    def mostrar_hora(self):
        #O :02d em uma f-string serve para formatar números inteiros
        print(f"\n-----------HORARIO------------\n{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}")

horario_f1 = Relogio(4, 20, 0)
horario_f1.mostrar_hora()

horario_tristeza = Relogio(8, 30 , 1)
horario_tristeza.mostrar_hora()

horario_felicidade = Relogio(18, 0, 1)
horario_felicidade.mostrar_hora()