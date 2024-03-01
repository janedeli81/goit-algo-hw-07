class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def findMinValue(node):
    current = node

    # Переміщуватися до найлівішого вузла
    while current.left is not None:
        current = current.left

    return current.val


# Приклад використання
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Найменше значення в дереві:", findMinValue(root))
