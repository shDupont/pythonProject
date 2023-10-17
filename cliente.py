class Cliente:
    def __init__(self, nome, data_nasc, telefone, email, endereco, cpf):
        self.nome = nome
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.cpf = cpf

    def __str__(self):
        return (f"(nome: {self.nome},"
                f" cpf: {self.cpf},"
                f" data_nasc: {self.data_nasc},"
                f" telefone: {self.telefone},"
                f" email: {self.email},"
                f" endereco: {self.endereco})")
