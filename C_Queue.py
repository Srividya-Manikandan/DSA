class Circular_Queue:
    def __init__(self,max_size):
        self.items=[None]*max_size
        self.front=0
        self.count=0
    def isEmpty(self):
        return self.count==0
    def isFull(self):
        if self.count==len(self.items):
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isFull():
            print("Queue is full")
            return
        i=(self.front+self.count)%len(self.items)
        self.items[i]=value
        self.count+=1
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        x=self.items[self.front]
        self.items[self.front]=None
        self.front=(self.front+1)%len(self.items)
        self.count-=1
        return x
    def disp(self):
        if self.front==0:
            print(self.items)
        else:
            for i in range(self.front,len(self.items)):
                if self.items[i] is not None:
                    print(self.items[i],end=" ")
            for i in range(0,self.front):
                if self.items[i] is not None:
                    print(self.items[i],end=" ")
            print()

queue=Circular_Queue(5)
print("Is Empty? ",queue.isEmpty())
print("Is Full? ",queue.isFull())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.disp()
print("Is Full? ",queue.isFull())
print("Is Empty? ",queue.isEmpty())
print(queue.dequeue())
print(queue.dequeue())
queue.disp()
queue.enqueue(60)
queue.disp()