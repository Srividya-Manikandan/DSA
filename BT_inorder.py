class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, elements):
        if not elements:
            return None

        self.root = Node(elements[0])
        queue = [self.root]
        i = 1

        while i < len(elements):  
            current = queue.pop(0)

            if i < len(elements) and elements[i] is not None:
                current.left = Node(elements[i])
                queue.append(current.left)
            i += 1

            if i < len(elements) and elements[i] is not None:
                current.right = Node(elements[i])
                queue.append(current.right)
            i += 1

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

# Example usage
if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5, 6, 7]  # Level-order input
    tree = BinaryTree()
    tree.insert_level_order(elements)

    print("Inorder Traversal of the tree:")
    tree.inorder_traversal(tree.root)