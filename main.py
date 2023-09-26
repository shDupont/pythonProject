class Cliente:
    def __init__(self, nome, data_nascimento, contato_telefone, email, endereco, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.contato_telefone = contato_telefone
        self.email = email
        self.endereco = endereco
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"

class Node:
    def __init__(self, cliente):
        self.cliente = cliente
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def insert(self, cliente):
        self.root = self._insert(self.root, cliente)

    def _insert(self, node, cliente):
        if not node:
            return Node(cliente)

        if cliente.cpf < node.cliente.cpf:
            node.left = self._insert(node.left, cliente)
        elif cliente.cpf > node.cliente.cpf:
            node.right = self._insert(node.right, cliente)
        else:

            return node

        self._update_height(node)

        balance = self._balance_factor(node)


        if balance > 1:
            if cliente.cpf < node.left.cliente.cpf:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if cliente.cpf > node.right.cliente.cpf:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, cpf):
        result, comparacoes = self._search(self.root, cpf)
        if result:
            return result.cliente, comparacoes
        else:
            return None, comparacoes

    def _search(self, node, cpf, comparacoes=[]):
        if not node:
            return None, comparacoes

        comparacoes.append(node.cliente.cpf)

        if cpf == node.cliente.cpf:
            return node, comparacoes
        elif cpf < node.cliente.cpf:
            return self._search(node.left, cpf, comparacoes=comparacoes)
        else:
            return self._search(node.right, cpf, comparacoes=comparacoes)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return sorted(result, key=lambda cliente: cliente.nome)

    def _inorder_traversal(self, node, result):
        if not node:
            return
        self._inorder_traversal(node.left, result)
        result.append(node.cliente)
        self._inorder_traversal(node.right, result)



if __name__ == "__main__":
    tree = AVLTree()

    clientes = [
        Cliente("João Silva", "1990-05-15", "123-4567", "joao@gmail.com", "Rua A, Bairro X, Cidade Y", "11111111111"),
        Cliente("Maria Santos", "1985-08-20", "987-6543", "maria@yahoo.com", "Rua B, Bairro Z, Cidade X",
                "22222222222"),
        Cliente("Pedro Oliveira", "1982-03-10", "555-1234", "pedro@hotmail.com", "Rua C, Bairro Y, Cidade Z",
                "33333333333"),
        Cliente("Ana Pereira", "1995-11-25", "333-9999", "ana@outlook.com", "Rua D, Bairro W, Cidade V", "44444444444"),
        Cliente("Luiz Costa", "1988-07-02", "222-5678", "luiz@gmail.com", "Rua E, Bairro V, Cidade U", "55555555555"),
        Cliente("Laura Rodrigues", "1983-12-30", "777-9876", "laura@yahoo.com", "Rua F, Bairro U, Cidade T",
                "66666666666"),
        Cliente("Carlos Alves", "1998-09-05", "888-4321", "carlos@hotmail.com", "Rua G, Bairro T, Cidade S",
                "77777777777"),
        Cliente("Fernanda Nunes", "1980-02-14", "111-1111", "fernanda@outlook.com", "Rua H, Bairro S, Cidade R",
                "88888888888"),
        Cliente("Rafael Lima", "1987-06-18", "666-7890", "rafael@gmail.com", "Rua I, Bairro R, Cidade Q",
                "99999999999"),
        Cliente("Mariana Silva", "1993-04-28", "444-2345", "mariana@yahoo.com", "Rua J, Bairro Q, Cidade P",
                "10101010101"),
        Cliente("Lucas Santos", "1989-10-11", "555-8765", "lucas@hotmail.com", "Rua K, Bairro P, Cidade O",
                "11111111112"),
        Cliente("Isabela Oliveira", "1991-07-07", "777-5432", "isabela@outlook.com", "Rua L, Bairro O, Cidade N",
                "12121212121"),
        Cliente("Gustavo Pereira", "1984-01-03", "222-4321", "gustavo@gmail.com", "Rua M, Bairro N, Cidade M",
                "13131313131"),
        Cliente("Camila Ferreira", "1997-08-16", "999-1111", "camila@yahoo.com", "Rua N, Bairro M, Cidade L",
                "14141414141"),
        Cliente("Thiago Costa", "1994-03-22", "444-5678", "thiago@hotmail.com", "Rua O, Bairro L, Cidade K",
                "15151515151"),
        Cliente("Julia Rodrigues", "1986-12-09", "555-4321", "julia@outlook.com", "Rua P, Bairro K, Cidade J",
                "16161616161"),
        Cliente("Roberto Alves", "1981-05-27", "333-3456", "roberto@gmail.com", "Rua Q, Bairro J, Cidade I",
                "17171717171"),
        Cliente("Renata Nunes", "1996-02-02", "777-2222", "renata@yahoo.com", "Rua R, Bairro I, Cidade H",
                "18181818181"),
        Cliente("Marcos Lima", "1992-11-14", "222-6789", "marcos@hotmail.com", "Rua S, Bairro H, Cidade G",
                "19191919191"),
        Cliente("Aline Silva", "1983-07-26", "888-9876", "aline@outlook.com", "Rua T, Bairro G, Cidade F",
                "20202020202"),

    ]


    for i, cliente in enumerate(clientes, start=1):
        print(f"Cliente {i}:")
        print(cliente)
        tree.insert(cliente)

    print("\nLista de clientes em ordem alfabética:")
    clientes_ordem_alfabetica = tree.inorder_traversal()
    for cliente in clientes_ordem_alfabetica:
        print(cliente)

    print("\nBusca por CPF '22222222222':")
    cpf_busca = "22222222222"
    resultado_busca, comparacoes = tree.search(cpf_busca)
    if resultado_busca is not None:
        encontrado = resultado_busca
        print(f"\nCliente encontrado: {encontrado.nome}")
        print(f"Comparação necessária para encontrar: {len(comparacoes)}")
        print("Comparações feitas durante a busca:")
        for i, cpf_comparacao in enumerate(comparacoes):
            print(f"Comparação {i + 1}: {cpf_comparacao}")
    else:
        print(f"\nCliente com CPF {cpf_busca} não encontrado.")

    print("\nBusca por CPF '10101010101':")
    cpf_busca = "10101010101"
    resultado_busca, comparacoes = tree.search(cpf_busca)
    if resultado_busca is not None:
        encontrado = resultado_busca
        print(f"\nCliente encontrado: {encontrado.nome}")
        print(f"Comparação necessária para encontrar: {len(comparacoes)}")
        print("Comparações feitas durante a busca:")
        for i, cpf_comparacao in enumerate(comparacoes):
            print(f"Comparação {i + 1}: {cpf_comparacao}")
    else:
        print(f"\nCliente com CPF {cpf_busca} não encontrado.")

    print("\nBusca por email 'maria@yahoo.com':")
    email_busca = "maria@yahoo.com"
    encontrado_pelo_email = None
    for cliente in clientes:
        if cliente.email == email_busca:
            encontrado_pelo_email = cliente
            break

    if encontrado_pelo_email is not None:
        print(f"\nCliente encontrado pelo email: {encontrado_pelo_email.nome}")
    else:
        print(f"\nCliente com email {email_busca} não encontrado.")