class Node:
    def __init__(self,value):
        self.info=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        self.count=0
        self.sum=0
        self.max=-1
    
    def level_order_insert(self,elements):
        if len(elements)==0:
            return
        self.root=Node(elements[0])
        queue=[self.root]
        i=1
        while i<len(elements):
            new=queue.pop(0)
            if elements[i]:
                new.left=Node(elements[i])
                queue.append(new.left)
                i+=1
            if i<len(elements) and elements[i]:
                new.right=Node(elements[i])
                queue.append(new.right)
                i+=1
        return

    def preorder_traversal(self,root):
        if root is None:
            return
        if root:
            self.count+=1
            self.sum+=root.info
            if self.max < self.root.info:
                self.max=self.root.info
            print(root.info,end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
        return
    
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.info,end=" ")
            self.inorder_traversal(root.right)
        return
    
    def postorder_traversal(self,root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.info,end=" ")
        return
    
    def level_order_traversal(self,root):
        queue=[]
        queue.append(root)
        while len(queue)!=0:
            new=queue.pop(0)
            print(new.info,end=" ")
            if new.left:
                queue.append(new.left)
            if new.right:
                queue.append(new.right)
        return

    def count_keys(self):
        return self.count
    
    def sum_keys(self):
        return self.sum
    
    def max_keys(self):
        return self.max
    
    def less_than_v(self,v,root):
        if root:
            if root.info<v:
                print(root.info,end=" ")
            self.less_than_v(v,root.left)            
            self.less_than_v(v,root.right)
        return              
        
    def height_bt(self):
        height = 0
        if self.root is None:
            return height
        p=self.root
        while p is not None:
            p=p.left
            height+=1
        return height
    


readlist=[1,2,3,4,5,6,7]
bt=BinaryTree()
bt.level_order_insert(readlist)
print("Preorder Traversal:")
bt.preorder_traversal(bt.root)
print("\nInorder Traversal:")
bt.inorder_traversal(bt.root)
print("\nPostorder Traversal:")
bt.postorder_traversal(bt.root)
print("\nLevel order Traversal:")
bt.level_order_traversal(bt.root)
print(f"\nNumber of items: {bt.count_keys()}")
print(f"Sum of keys: {bt.sum_keys()}")
print(f"Maximum of keys: {bt.max_keys()}")
bt.less_than_v(6,bt.root)
print(f"\nHeight of the tree: {bt.height_bt()}")