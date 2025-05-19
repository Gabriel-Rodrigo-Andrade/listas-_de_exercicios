class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def detalhes(self):
        print(f"\n-----------------\nTitulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}")