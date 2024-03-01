class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def findMaxValue(node):
    current = node

    # Йти до найправішого вузла
    while current.right is not None:
        current = current.right

    return current.val


# Приклад використання
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)

print("Найбільше значення в дереві:", findMaxValue(root))
