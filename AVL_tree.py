class Node:
    def __init__(self, cliente):
        self.cliente = cliente
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return (f"(cliente: {self.cliente.cpf},"
                f" height: {self.height})")


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
        elif not node.left and not node.right:
            node.height = 1
        else:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, z):
        y = z.right
        temp = y.left

        y.left = z
        z.right = temp

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

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
            if self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, cpf):
        result, comparisons = self._search(self.root, cpf, None)
        if result:
            return result.cliente, comparisons
        else:
            return None, comparisons

    def _search(self, node, cpf, comparisons):
        if comparisons is None:
            comparisons = []

        if not node:
            return None, comparisons

        comparisons.append(node.cliente.cpf)

        if cpf == node.cliente.cpf:
            return node, comparisons
        elif cpf < node.cliente.cpf:
            return self._search(node.left, cpf, comparisons)
        else:
            return self._search(node.right, cpf, comparisons)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if not node:
            return
        self._inorder_traversal(node.left, result)
        result.append(node.cliente)
        self._inorder_traversal(node.right, result)

    def get_all_balance_factors(self):
        result = []
        self._get_all_balance_factors(self.root, result)
        return result

    def _get_all_balance_factors(self, node, result):
        if not node:
            return
        self._get_all_balance_factors(node.right, result)
        self._get_all_balance_factors(node.left, result)

        node_info = ''
        if node == self.root:
            node_info = "node[root]"
        elif node.height == 1:
            node_info = "node[leaf]"
        else:
            node_info = "node[common]"

        node_info += f" height: {node.height} bf: {self._balance_factor(node)}"

        result.append(node_info)
