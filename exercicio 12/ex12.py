class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def validar_email(self):
        if '@' not in self.email:
            raise ValueError(f"\nE-mail invalido: deve conter '@'")
        else: 
            print(f"\nE-mail verificado com sucesso.\n")
        
cadastro1 = Usuario("Gabriel", "gabrielandrade0472@gmail.com")
cadastro2 = Usuario("Joao Vitor", "bacelark13gmail.com.br")

cadastro1.validar_email()
cadastro2.validar_email()