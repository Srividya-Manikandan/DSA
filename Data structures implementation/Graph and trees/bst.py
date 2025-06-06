class Node:
    def __init__(self,data):
        self.info=data
        self.left=None
        self.right=None
        self.parent=None

class BST:
    def __init__(self):
        self.root=None
    
    def insert1(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        p=self.root
        while p is not None:
            parent=p
            if data<p.info:
                p=p.left
            elif data>p.info:
                p=p.right
            else:
                return
        temp=Node(data)
        if data<parent.info:
            parent.left=temp
            parent.left.parent=parent
        elif data>parent.info:
            parent.right=temp
            parent.right.parent=parent

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_correctly(self.root,data)
        return
    
    def insert_correctly(self,p,data):
        if data<p.info:
            if p.left is None:
                temp=Node(data)
                temp.parent=p
                p.left=temp
            else:
                self.insert_correctly(p.left,data)
        if data>p.info:
            if p.right is None:
                temp=Node(data)
                temp.parent=p
                p.right=temp
            else:
                self.insert_correctly(p.right,data)

    def search1(self,data):
        p=self.root
        while p is not None:
            if p.info==data:
                return True
            elif data<p.info:
                p=p.left
            else:
                p=p.right
        return False

    def search(self,data):
        return self._search(self.root,data)

    def _search(self,root,data):
        if root is None:
            return False
        if root.info==data:
            return True
        elif data<root.info:
            return self._search(root.left,data)
        elif data>root.info:
            return self._search(root.right,data)
        return
    
    def preorder(self,root):
        if root:
            print(root.info,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.info,end=" ")

    def inorder_print(self,root):
        if root:
            self.inorder_print(root.left)
            print(root.info, end=" ")
            self.inorder_print(root.right)

    def large2(self):
        if self.root:
            p=self.root
            while p.right is not None:
                p=p.right
            if p.parent==self.root:
                print(f"2nd largest: {p.left.info}")
            else:
                print(f"2nd largest: {p.parent.info}")
        return
    
    def small2(self):
        if self.root:
            p=self.root
            while p.left is not None:
                p=p.left
            print(f"2nd largest: {p.parent.info}")
    
    def kthsmall(self,k):
        nodes=[]
        self.inorder_append(nodes,self.root)
        if k>len(nodes):
            return
        else:
            return nodes[k-1]
        
    def kthlarge(self,k):
        nodes=[]
        self.inorder_append(nodes,self.root)
        nodes.reverse()
        if k>len(nodes):
            return
        else:
            return nodes[k-1]

    def level(self,key):
        level = 1
        p=self.root
        while p is not None:
            if key<p.info:
                p=p.left
                level+=1
            elif key>p.info:
                p=p.right
                level+=1
            else:
                return level
        return
    
    def height(self):
        return self._height(self.root)
    
    def _height(self,root):
        if root is None:
            return 0
        lh=self._height(root.left)
        rh=self._height(root.right)
        return max(lh,rh) + 1

    def minkey1(self):
        if self.root is None:
            return
        p=self.root
        while p.left is not None: #while p.right is not None:
            p=p.left #p=p.right
        return p.info
    
    def minkey(self):
        if self.root is None:
            return None
        else:
            return self._minkey(self.root).info #return self._maxkey(self.root).info
        
    def _minkey(self,root):
        if root.left is None: #if root.right is None:
            return root
        else:
            return self._minkey(root.left) #return self._maxkey(root.right)

    # def maxkey1(self):
    #     if self.root is None:
    #         return
    #     p=self.root
    #     while p.right is not None:
    #         p=p.right
    #     return p.info
    
    # def maxkey(self):
    #     if self.root is None:
    #         return None
    #     else:
    #         return self._maxkey(self.root).info
    # def _maxkey(self,root):
    #     if root.right is None:
    #         return root
    #     else:
    #         return self._maxkey(root.right)

    # def sumk(self,k):
    #     nodes=[]
    #     self.inorder_append(nodes,self.root)
    #     left,right=0,len(nodes)-1
    #     while left<right:
    #         sum=nodes[left]+nodes[right]
    #         if sum<k:
    #             left+=1
    #         elif sum>k:
    #             right-=1
    #         else:
    #             return nodes[left],nodes[right]
    #     return None,None

    def inorder_append(self,arr,root):
        if root:
            self.inorder_append(arr,root.left)
            arr.append(root.info)
            self.inorder_append(arr,root.right)

    # def inorder_append(self,arr,root):
    #     if root:
    #         self.inorder_append(arr,root.left)
    #         arr.append(root)
    #         self.inorder_append(arr,root.right)
    # def subtrees(self):
    #     if self.root:
    #         count=0
    #         return self._subtrees(self.root,count)
    #     return

    # def _subtrees(self,root,c):
    #     if root.left or root.right:
    #         if root.left:
    #             c=self._subtrees(root.left,c)
    #         if root.right:
    #             c=self._subtrees(root.right,c)
    #         c+=1
    #         return c
    #     else:
    #         return c
        
    # def level_order(self):
    #     q=[]
    #     q.append(self.root)
    #     while len(q)!=0:
    #         new=q.pop(0)
    #         print(new.info,end=" ")
    #         if new.left:
    #             q.append(new.left)
    #         if new.right:
    #             q.append(new.right)
    #     print()
    #     return

    # def left_view(self):
    #     if self.root:
    #         q=[self.root]
    #         while len(q)!=0:
    #             l = len(q)
    #             for i in range(l):
    #                 new=q.pop(0)
    #                 if i==0:
    #                     print(new.info,end=" ")
    #                 if new.left:
    #                     q.append(new.left)
    #                 if new.right:
    #                     q.append(new.right)
    #         print()
    #     return

    # def top_view(self):
    #     if self.root:
    #         topmap={}
    #         q=[(self.root,0)]
    #         while len(q)!=0:
    #             new, hd=q.pop(0)
    #             if hd not in topmap:
    #                 topmap[hd]=new.info
    #             if new.left:
    #                 q.append((new.left,hd-1))
    #             if new.right:
    #                 q.append((new.right,hd+1))
    #         for hd in topmap:
    #             print(topmap[hd],end=" ")
    #         print()
    #     return

    # def bottom_view(self):
    #     if self.root:
    #         botmap={}
    #         q=[(self.root,0)]
    #         while len(q)!=0:
    #             new,hd=q.pop(0)
    #             botmap[hd]=new.info
    #             if new.left:
    #                 q.append((new.left,hd-1))
    #             if new.right:
    #                 q.append((new.right,hd+1))
    #         for hd in botmap:
    #             print(botmap[hd],end=" ")
    #         print()
    #     return

    # def mirror(self,root):
    #     if root is None:
    #         return
    #     self.mirror(root.left)
    #     self.mirror(root.right)
    #     root.left, root.right = root.right, root.left

    # def inorder_successor1(self,key):
    #     successor=None
    #     p=self.root
    #     while p:
    #         if key < p.info:
    #             successor=p
    #             p=p.left
    #         elif key > p.info:
    #             p=p.right
    #         else:
    #             break
    #     if not p:
    #         return None
    #     if p.right:
    #         r=p.right
    #         while r.left:
    #             r=r.left
    #         successor=r
    #     return successor

    # def inorder_successor(self,key):
    #     if self.root:
    #         nodes=[]
    #         self.inorder_append(nodes,self.root)
    #         i=nodes.index(key)
    #         if i>len(nodes)-1:
    #             return None
    #         else:
    #             return nodes[i+1]
    #     return

    # def min_diff(self):
    #     if self.root:
    #         nodes=[]
    #         self.inorder_append(nodes,self.root)
    #         min_diff=float('inf')
    #         for i in range(1,len(nodes)):
    #             diff=nodes[i]-nodes[i-1]
    #             min_diff=min(diff,min_diff)
    #         return min_diff
    #     return

    # def delete(self,key):
    #     if self.root:
    #         p=self.find_node(key)
    #         if p is None:
    #             return
    #         if p.left is None and p.right is None:
    #             if p.parent:
    #                 if p.parent.left==p:
    #                     p.parent.left=None
    #                 else:
    #                     p.parent.right=None
    #             else:
    #                 self.root=None
    #         elif p.left is not None and p.right is not None:
    #             r=self.inorder_successor1(p.info)
    #             store=r.info
    #             self.delete(r.info)
    #             p.info=store
    #         else:
    #             if p.left:
    #                 child=p.left
    #             else:
    #                 child=p.right
    #             if p.parent:
    #                 if p.parent.left==p:
    #                     p.parent.left=child
    #                 else:
    #                     p.parent.right=child
    #             else:
    #                 self.root=child
    #             child.parent = p.parent
    #     return
    # def find_node(self,key):
    #     if self.root:
    #         p=self.root
    #         while p is not None:
    #             if p.info==key:
    #                 return p
    #             elif key<p.info:
    #                 p=p.left
    #             else:
    #                 p=p.right
    #     return

    def display(self):
        self._display(self.root,0)
    def _display(self,root,level):
        if root is None:
            return
        self._display(root.right,level+1)
        for _ in range(level):
            print("  ",end=" ")
        print(root.info)
        self._display(root.left,level+1)

    def merge2(self,bst1,bst2):
        arr1=[]
        arr2=[]
        self.inorder_append(arr1,bst1)
        self.inorder_append(arr2,bst2)
        for x in arr2:
            arr1.append(x)
        arr1.sort()
        # merged = self.mergearray(arr1,arr2)
        #return self.sorted_to_bst(merged)
        return self.sorted_to_bst(arr1)
    
    def sorted_to_bst(self,arr):
        if len(arr)==0:
            return None
        mid=len(arr)//2
        root=Node(arr[mid])
        root.left=self.sorted_to_bst(arr[:mid])
        root.right=self.sorted_to_bst(arr[mid+1:])
        return root

    # def mergearray(self,arr1,arr2):
    #     merged = []
    #     i=j=0
    #     while i<len(arr1) and j<len(arr2):
    #         if arr1[i].info<arr2[j].info:
    #             merged.append(arr1[i])
    #             i+=1
    #         else:
    #             merged.append(arr2[j])
    #             j+=1
    #     while i<len(arr1):
    #         merged.append(arr1[i])
    #         i+=1
    #     while i<len(arr2):
    #         merged.append(arr2[j])
    #         j+=1
    #     return merged

    def diag_sum(self,root):
        if not root:
            return []
        diag_sums={}
        q=[(root,0)]
        while len(q)!=0:
            node,level=q.pop(0)
            while node:
                if level in diag_sums:
                    diag_sums[level]+=node.info
                else:
                    diag_sums[level]=node.info
                if node.left:
                    q.append((root.left,level+1))
                node=node.right
        sums=[]
        for i in diag_sums:
            sums.append(diag_sums[i])
        return sums


bst=BST()
bst.insert(5)#5
bst.insert(3)
bst.insert(8)
#bst.inorder_print(bst.root)
print()
# print(bst.search(2))#3
# print(bst.search1(3))#2
bst.insert1(6)#4
bst.insert1(4)
bst.insert1(2)
# bst.inorder_print(bst.root)
# print()
# bst.large2()#6
# bst.small2()#6
# #x=int(input("Enter a val to know the level: "))
# print(f"Level of x: {bst.level(5)}")#7
# print(f"The minimum key(i): {bst.minkey1()}")#8
# print(f"The minimum key(r): {bst.minkey()}")#9
# print(f"The maximum key(i): {bst.maxkey1()}")#10
# print(f"The maximum key(r): {bst.maxkey()}")#11
# print("Preorder traversal:",end=" ")#12
# bst.preorder(bst.root)
# print()
# print("Inorder traversal:",end=" ")
# bst.inorder_print(bst.root)#13
# print()
# print("Postorder traversal:",end=" ")#14
# bst.postorder(bst.root)
# print()
# print("Level order traversal:",end=" ")
# bst.level_order()
# print(f"The height of tree: {bst.height()}")#15
# #k=int(input("Sum number: "))
# print(f"The pair of nodes with sum k: {bst.sumk(10)}")#16
# print(f"No. of subtrees: {bst.subtrees()}")#17
# print("Left view:",end=" ")#18
# bst.left_view()
# print("Top view:",end=" ")#19
# bst.top_view()
# print("Bottom view:",end=" ")#20
# bst.bottom_view()
# # tri=BST()
# # for x in [5,3,2,4,8,6]:
# #     tri.insert(x)
# # tri.level_order()
# bst.mirror(bst.root)
# print("Mirror of bst:",end=" ")
# bst.level_order()
# bst.mirror(bst.root)
# #key=int(input("Inorder successor of: "))
# print(f"Inorder successor of key: {bst.inorder_successor(6)}")
# print(f"The minimum difference: {bst.min_diff()}")
# bst.delete(8)
# bst.level_order()
# bst.delete(3)
# bst.level_order()
# bst.delete(2)
# bst.level_order()
# bst.delete(5)
# bst.level_order()
# print(f"kth smallest (k=3): {bst.kthsmall(3)}")
# print(f"kth largest (k=3): {bst.kthlarge(3)}")
print("Display bst1:")
bst.display()

bst2=BST()
bst2.insert(7)
bst2.insert(1)
bst2.insert(9)

print("Display bst2:")
bst2.display()

bst3=BST()
bst3.root=bst3.merge2(bst.root,bst2.root)
print("Display bst3:")
bst3.display()
print(bst2.diag_sum(bst2.root))