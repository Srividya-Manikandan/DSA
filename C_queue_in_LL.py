class Node():
    def __init__(self,value):
        self.info=value
        self.next=None
class C_queue():
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def isEmpty(self):
        return self.front==None
    def size(self):
        return self.count
    def enqueue(self,value):
        temp=Node(value)
        if self.front is None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.rear.next=self.front
        self.count+=1
        return
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty to dequeue something")
            return None
        if self.front==self.front.next:
            x=self.front
            self.front=None
            return x.info
        y=self.front
        self.rear.next=self.front.next
        self.front=self.front.next
        self.count-=1
        return y.info
    def peek(self):
        return self.front.info
    def last(self):
        return self.rear.info
    def disp(self):
        if self.isEmpty():
            print("Empty list")
            return
        elif self.front==self.front.next:
            print(self.front.info)
            return
        else:
            p=self.front
            while p and p!=self.rear:
                print(p.info,end=" ")
                p=p.next
            print(self.rear.info)
            return
queue = C_queue()
print("Is Empty? ",queue.isEmpty())
queue.enqueue(10)
print("Is Empty? ",queue.isEmpty())
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.disp()
queue.enqueue(60)
queue.disp()
print(queue.dequeue())
print(queue.dequeue())
queue.disp()
queue.enqueue(60)
print("Size: ",queue.size())
queue.disp()
print("Peek: ",queue.peek())
print("Last: ",queue.last())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.disp()