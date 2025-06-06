from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None  # New parent pointer
    
class LinkedListBinaryTree:
    def __init__(self):
        self.root = None
    
    def insertRoot(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            print(f"Root {data} added")
        else:
            print("Root already exists")
    
    def insertLeft(self, parent, data):
        if parent is None:
            print("Parent node is None")
            return
        if parent.left is None:
            parent.left = TreeNode(data)
            parent.left.parent = parent  # Set the parent reference
            print(f"Left child {data} added to parent {parent.data}")
        else:
            print(f"Left child already exists for parent {parent.data}")
            
            
    def insertRight(self, parent, data):
        if parent is None:
            print("Parent node is None")
            return
        if parent.right is None:
            parent.right = TreeNode(data)
            parent.right.parent = parent  # Set the parent reference
            print(f"Right child {data} added to parent {parent.data}")
        else:
            print(f"Right child already exists for parent {parent.data}")
            
            
    def search(self, node, data):
        """ Recursive search function to find a node with the given data """
        if node is None:
            return None
        if node.data == data:
            return node
        left_search = self.search(node.left, data)
        if left_search is not None:
            return left_search
        return self.search(node.right, data)
    
    
    def inorderTraversal(self, node):
        if node:
            self.inorderTraversal(node.left)
            print(node.data, end=' ')
            self.inorderTraversal(node.right)
            
            
    def preorderTraversal(self, node):
        if node:
            print(node.data, end=' ')
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)
            
            
    def postorderTraversal(self, node):
        if node:
            self.postorderTraversal(node.left)
            self.postorderTraversal(node.right)
            print(node.data, end=' ')
            
            
    def levelOrderTraversal(self):
        """ Level-order traversal using a queue (deque for efficiency) """
        if self.root is None:
            return
        queue = deque([self.root])  # Initialize deque with the root node
        while queue:
            current = queue.popleft()  # Remove and return the leftmost element in O(1) time
            print(current.data, end=' ')  # Print the current node's data
            if current.left:
                queue.append(current.left)  # Add left child to the queue
            if current.right:
                queue.append(current.right)  # Add right child to the queue
                
                
    def swapSubtrees(self, node1, node2):
        """ Swap the subtrees rooted at node1 and node2 """
        if node1 is None or node2 is None:
            return
        # Swap the subtrees
        node1.left, node2.left = node2.left, node1.left
        node1.right, node2.right = node2.right, node1.right
        # Update parent references
        if node1.left:
            node1.left.parent = node1
        if node1.right:
            node1.right.parent = node1
        if node2.left:
            node2.left.parent = node2
        if node2.right:
            node2.right.parent = node2
            
            
    def swapValues(self, node1, node2):
        """ Swap the values of two nodes """
        if node1 is None or node2 is None:
            return
        # Swap the values
        node1.data, node2.data = node2.data, node1.data
        
        
    def findHeight(self, node):
        """ Recursive function to calculate height of the binary tree """
        if node is None:
            return -1
        left_height = self.findHeight(node.left)                                                                                                                                                                                                                                                                                                                   
        right_height = self.findHeight(node.right)
        return max(left_height, right_height) + 1
    
    
    def findSize(self, node):
        """ Recursive function to calculate the size (number of nodes) of the binary tree """
        if node is None:
            return 0
        return self.findSize(node.left) + self.findSize(node.right) + 1
    
    
    def findMin(self, node):
        """ Find the minimum value in the binary tree (recursive) """
        if node is None:
            return float('inf')
        left_min = self.findMin(node.left)
        right_min = self.findMin(node.right)
        return min(node.data, left_min, right_min)
    
    
    def findMax(self, node):
        """ Find the maximum value in the binary tree (recursive) """
        if node is None:
            return float('-inf')
        left_max = self.findMax(node.left)
        right_max = self.findMax(node.right)
        return max(node.data, left_max, right_max)
    
    
    def deleteTree(self):
        """ Deletes the entire tree """
        self.root = None
        print("Tree deleted")
        
        
    def isBalanced(self, node):
        """ Check if the tree is balanced (difference between left and right subtree heights <= 1) """
        if node is None:
            return True
        left_height = self.findHeight(node.left)
        right_height = self.findHeight(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)
    
    
    def mirror(self, node):
        """ Create a mirror image of the binary tree """
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.mirror(node.left)
        self.mirror(node.right)
        
        
    def deleteNode(self, key):
        """ Deletes a node from the binary tree """
        if self.root is None:
            print("Tree is empty")
            return

        # Perform level-order traversal to find the node to delete and the deepest node
        queue = deque([self.root])
        node_to_delete = None
        deepest_node = None
        parent_of_deepest = None

        while queue:
            current = queue.popleft()
            if current.data == key:
                node_to_delete = current

            # Track the deepest node
            deepest_node = current
            if current.left:
                queue.append(current.left)
                parent_of_deepest = current.left
            if current.right:
                queue.append(current.right)
                parent_of_deepest = current.right

        if node_to_delete:
            # Replace the data of node to delete with the deepest node's data
            node_to_delete.data = deepest_node.data

            # Remove the deepest node
            if parent_of_deepest and parent_of_deepest == deepest_node:
                if parent_of_deepest == parent_of_deepest.parent.left:
                    parent_of_deepest.parent.left = None
                else:
                    parent_of_deepest.parent.right = None
            else:
                if deepest_node == self.root:
                    self.root = None
                else:
                    if deepest_node == deepest_node.parent.left:
                        deepest_node.parent.left = None
                    else:
                        deepest_node.parent.right = None

            print(f"Node with key {key} deleted")
        else:
            print(f"Node with key {key} not found")
    
    
if __name__ == "__main__":
    tree = LinkedListBinaryTree()
    tree.insertRoot(10)
    root = tree.root
    tree.insertLeft(root, 5)
    tree.insertRight(root, 20)
    tree.insertLeft(root.left, 3)
    tree.insertRight(root.left, 7)
    tree.insertLeft(root.right, 15)
    tree.insertRight(root.right, 30)
    print("Inorder Traversal: ", end="")
    tree.inorderTraversal(tree.root)
    print("\nDeleting node 20...")
    tree.deleteNode(20)
    print("Inorder Traversal after deletion: ", end="")
    tree.inorderTraversal(tree.root)
    
    # Example of swapping values
    node1 = tree.search(root, 5)
    node2 = tree.search(root, 20)
    if node1 and node2:
        print("\nSwapping values of nodes 5 and 20...")
        tree.swapValues(node1, node2)
    
    print("Inorder Traversal after swapping values: ", end="")
    tree.inorderTraversal(tree.root)
    
    # Example of swapping subtrees
    node1 = tree.search(root, 5)
    node2 = tree.search(root, 30)
    if node1 and node2:
        print("\nSwapping subtrees rooted at nodes 5 and 30...")
        tree.swapSubtrees(node1, node2)
    
    print("Inorder Traversal after swapping subtrees: ", end="")
    tree.inorderTraversal(tree.root)