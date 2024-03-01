class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sumOfValues(node):
    if node is None:
        return 0
    else:
        return node.val + sumOfValues(node.left) + sumOfValues(node.right)

# Приклад використання
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print("Сума всіх значень в дереві:", sumOfValues(root))
