import collections
class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.info=value
        self.next=None
class queue:
    def __init__(self):
        self.start=None
    def enqueue(self,temp):
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        return
    def dequeue(self):
        if self.start is None:
            return
        x=self.start
        self.start=self.start.next
        return x

def preorder(root):
    if root:
        print(root.info, end=" ")
        preorder(root.left)
        preorder(root.right)
    return

def inorder(root):
    if root:
        inorder(root.left)
        print(root.info,end=' ')
        inorder(root.right)
    return

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.info,end=" ")
    return

def level_order(root):
    # qu=collections.deque()
    # qu.append(root)
    # while qu:   
    #     new=qu.popleft()
    #     print(new.info,end=" ")
    #     if new.left:
    #         qu.append(new.left)
    #     if new.right:
    #         qu.append(new.right)
    # return
    q=queue()
    q.enqueue(root)
    while q.start:
        new=q.dequeue()
        print(new.info,end=" ")
        if new.left:
            q.enqueue(new.left)
        if new.right:
            q.enqueue(new.right)
    return
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

print("Preorder Traversal:")
preorder(root)
print("\nInorder Traversal:")
inorder(root)
print("\nPostorder Traversal:")
postorder(root)
print("\nLevel order Traversal:")
level_order(root)