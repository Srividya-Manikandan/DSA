class minheap:
    def __init__(self):
        self.heap=[]
    
    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return (2*i+1)
    
    def right(self,i):
        return (2*i+2)
    
    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,i):
        while i>0 and self.heap[i]<self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)

    def pop_min(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self,i):
        small=i
        l=self.left(i)
        r=self.right(i)
        if l<len(self.heap) and self.heap[l]<self.heap[small]:
            small=l
        if r<len(self.heap) and self.heap[r]<self.heap[small]:
            small=r
        if small!=i:
            self.heap[i], self.heap[small]=self.heap[small], self.heap[i]
            self.heapify_down(small)

    def get_min(self):
        if len(self.heap)==0:
            return None
        return self.heap[0]
    
    def disp(self):
        print(self.heap)

mn=minheap()
mn.insert(50)
mn.insert(10)
mn.insert(60)
mn.insert(30)
mn.insert(20)
mn.insert(40)
mn.disp()
print(f"Extract min: {mn.pop_min()}")
mn.disp()
print(f"Min: {mn.get_min()}")

class maxheap:
    def __init__(self):
        self.heap=[]
    
    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return 2*i+1
    
    def right(self,i):
        return 2*i+2
    
    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,i):
        while i>0 and self.heap[i]>self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
    
    def pop_max(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self,i):
        big=i
        l=self.left(i)
        r=self.right(i)
        if l<len(self.heap) and self.heap[l]>self.heap[big]:
            big=l
        if r<len(self.heap) and self.heap[r]>self.heap[big]:
            big=r
        if big!=i:
            self.heap[i],self.heap[big]=self.heap[big],self.heap[i]
            self.heapify_down(big)
    
    def get_max(self):
        if len(self.heap)==0:
            return None
        return self.heap[0]
    
    def disp(self):
        print(self.heap)

    def to_min(self):
        for i in range(len(self.heap)//2-1,-1,-1):
            self.heapify_down_min(i)

    def heapify_down_min(self,i):
        small=i
        l=self.left(i)
        r=self.right(i)
        if l<len(self.heap) and self.heap[l]<self.heap[small]:
            small=l
        if r<len(self.heap) and self.heap[r]<self.heap[small]:
            small=r
        if small!=i:
            self.heap[i], self.heap[small]=self.heap[small], self.heap[i]
            self.heapify_down_min(small)

    def is_min(self):
        return self._is_min(0)
    def _is_min(self,i):
        if i>len(self.heap)//2:
            return True
        l=self.left(i)
        r=self.right(i)
        if(l<len(self.heap) and self.heap[i]>self.heap[l]) or (r<len(self.heap) and self.heap[i]>self.heap[r]):
            return False
        return self._is_min(l) and self._is_min(r)

    def is_min1(self):
        for i in range(len(self.heap)//2):
            l=self.left(i)
            r=self.right(i)
            if(l<len(self.heap) and self.heap[i]>self.heap[l]) or (r<len(self.heap) and self.heap[i]>self.heap[r]):
                False
        return True

mx=maxheap()
mx.insert(50)
mx.insert(10)
mx.insert(60)
mx.insert(30)
mx.insert(20)
mx.insert(40)
mx.disp()
print(f"Extract max: {mx.pop_max()}")
mx.disp()
print(f"Max: {mx.get_max()}")
mx.to_min()
mx.disp()
print(f"Is mx min?: {mx.is_min()}")
print(f"Is mx min?: {mx.is_min1()}")