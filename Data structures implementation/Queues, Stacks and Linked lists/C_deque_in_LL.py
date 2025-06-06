class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.info=value
class C_Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def isEmpty(self):
        return self.count==0
    def size(self):
        return self.count
    def enqueue_right(self,value):
        temp=Node(value)
        if self.front is None:
            self.front=temp
            self.rear=temp
            self.front.prev=self.rear
            self.rear.next=self.front
        elif self.front==self.rear:
            self.front.next=temp
            temp.prev=self.front
            self.rear=temp
            self.rear.next=self.front
            self.front.prev=self.rear
        else:
            self.rear.next=temp
            temp.prev=self.rear
            self.rear=temp
            self.rear.next=self.front
            self.front.prev=self.rear
        self.count+=1
        return
    def enqueue_left(self,value):
        temp=Node(value)
        if self.front is None:
            self.front=temp
            self.rear=temp
            self.rear.next=self.front
            self.front.prev=self.rear
        else:
            self.front.prev=temp
            temp.next=self.front
            self.front=temp
            self.front.prev=self.rear
            self.rear.next=self.front
        self.count+=1
        return
    def dequeue_right(self):
        if self.isEmpty():
            print("Empty deque")
            return None
        elif self.front==self.rear:
            x=self.rear.info
            self.front=None
            self.count-=1
            return x
        else:
            y=self.rear.info
            self.rear.prev.next=self.front
            self.rear=self.rear.prev
            self.front.prev=self.rear
            self.count-=1
            return y
    def dequeue_left(self):
        if self.isEmpty():
            print("Empty deque")
            return None
        elif self.front==self.rear:
            x=self.front.info
            self.front=None
            self.count-=1
            return x
        else:
            y=self.front.info
            self.front.next.prev=self.rear
            self.front=self.front.next
            self.rear.next=self.front
            self.count-=1
            return y
    def disp(self):
        if self.isEmpty():
            print("Empty deque")
            return None
        p=self.front
        while p and p!=self.rear:
            print(p.info,end=" ")
            p=p.next
        print(p.info)
        return
    def peek(self):
        if self.isEmpty():
            print("Empty deque")
            return None
        else:
            return(self.front.info)
    def last(self):
        if self.isEmpty():
            print("Empty deque")
            return None
        else:
            return(self.rear.info)
deque = C_Deque()
print("Is Empty? ",deque.isEmpty())
deque.enqueue_left(10)
deque.disp()
print("Is Empty? ",deque.isEmpty())
deque.enqueue_right(20)
deque.disp()
deque.enqueue_left(30)
deque.disp()
deque.enqueue_left(40)
deque.disp()
deque.enqueue_right(50)
deque.disp()
deque.enqueue_left(60)
deque.disp()
print(deque.dequeue_left())
deque.disp()
print(deque.dequeue_right())
deque.disp()
deque.enqueue_left(70)
deque.disp()
print("Size: ",deque.size())
deque.disp()
print("Peek: ",deque.peek())
print("Last: ",deque.last())
print(deque.dequeue_left())
deque.disp()
print(deque.dequeue_left())
deque.disp()
print(deque.dequeue_right())
deque.disp()
print(deque.dequeue_right())
deque.disp()
print(deque.dequeue_right())
deque.disp()