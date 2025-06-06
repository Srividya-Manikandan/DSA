class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
class Queue:
    def __init__(self):
        self.start=None
    def enqueue(self,value):
        temp=Node(value)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
    def dequeue(self):
        if self.start is None:
            print("Queue is empty")
            return
        dequeued = self.start
        self.start=self.start.next
        return dequeued.info
    def Rear(self):
        if self.start is None:
            print("Queue is empty")
            return
        p=self.start
        while p.next is not None:
            p=p.next
        return p.info
    def Front(self):
        if self.start is None:
            print("Queue is empty")
            return
        return self.start.info
    def isEmpty(self):
        if self.start is None:
            return True
        else:
            return False
    def size(self):
        count=0
        if self.start is None:
            return count
        p=self.start
        while p is not None:
            count+=1
            p=p.next
        return count
    def create_queue(self):
        n=int(input("Enter the number of nodes: "))
        for i in range(n):
            x=int(input("Enter the value of nodes: "))
            self.enqueue(x)
    def display_queue(self):
        if self.start is None:
            print("Queue is empty")
            return
        p=self.start
        while p is not None:
            print(p.info,end='<--')
            p=p.next
        print()
q1=Queue()
q1.create_queue()
q1.display_queue()
q1.enqueue(4)
print(q1.dequeue())
print(q1.Front())
print(q1.Rear())
print(q1.size())
q1.display_queue()