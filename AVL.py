class AVLNode:
    """Class representing a node in an AVL Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initial height is 1


class AVLTree:
    """Class representing the AVL Tree."""
    
    def __init__(self):
        self.root = None  # Initialize the tree with an empty root

    def get_height(self, node):
        """Helper function to get the height of a node."""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """Calculate and return the balance factor of a node."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)


    def rotate_right(self, y):
        """Perform a right rotation."""
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        """Perform a left rotation."""
        y = x.right
        T2 = y.left

        # Rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, key):
        """Insert a key into the AVL tree."""
        def _insert(node, key):
            # Standard BST insertion
            if not node:
                return AVLNode(key)

            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)

            # Update height of the current node
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

            # Get the balance factor
            balance = self.get_balance(node)

            # Rebalancing the tree
            if balance > 1:  # Left-heavy
                if key < node.left.key:  # Left-Left Case
                    return self.rotate_right(node)
                else:  # Left-Right Case
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)

            if balance < -1:  # Right-heavy
                if key > node.right.key:  # Right-Right Case
                    return self.rotate_left(node)
                else:  # Right-Left Case
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)

            return node  # Return the unchanged node pointer

        # Update the root of the tree after insertion
        self.root = _insert(self.root, key)

    def get_min_value_node(self, node):
        """Find the node with the smallest key in the subtree rooted at `node`."""
        p=node
        while p.left is not None:
            p=p.left
        return p

    def delete(self, key):
        """Delete a key from the AVL tree."""
        def _delete(node, key):
            if not node:
                return node

            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Node with one or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Node with two children: Get the inorder successor
                temp = self.get_min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)

            # Update height
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            balance = self.get_balance(node)

            # Rebalance
            if balance > 1:  # Left-heavy
                if self.get_balance(node.left) >= 0:  # Left-Left Case
                    return self.rotate_right(node)
                else:  # Left-Right Case
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)

            if balance < -1:  # Right-heavy
                if self.get_balance(node.right) <= 0:  # Right-Right Case
                    return self.rotate_left(node)
                else:  # Right-Left Case
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)

            return node

        self.root = _delete(self.root, key)

    def preorderTraversal(self, node):
        """Pre-order traversal of the AVL tree."""
        if node:
            print(node.key, end=' ')
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)


# Example usage
if __name__ == "__main__":
    avl = AVLTree()

    # Insert elements
    elements = [10, 20, 30, 40, 50, 25]
    for el in elements:
        avl.insert(el)

    # Pre-order traversal
    print("Pre-order traversal of the constructed AVL tree is:")
    avl.preorderTraversal(avl.root)
    avl.delete(40)
    print("\nPre-order traversal after deleting 40:")
    avl.preorderTraversal(avl.root)    