class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
class SSL:
    def __init__(self):
        self.start=None
    def create(self):
        n=int(input("No. of elements in list: "))
        for _ in range(n):
            data = int(input("Data to be entered: "))
            self.insert_end(data)
    def insert_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        return
    def disp(self):
        if self.start is None:
            print("Empty")
            return
        p=self.start
        while p is not None:
            print(p.info, end=" ")
            p=p.next
        print()
    def insert_after_specified(self,data,value):
        temp=Node(data)
        p=self.start
        while p is not None:
            if p.info==value:
                break
            p=p.next
        if p is None:
            print("Invalid data")
        else:
            temp.next=p.next
            p.next=temp
    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next_node = p.next
            p.next = prev
            prev = p
            p = next_node
        self.start= prev
    def bubble_data(self):
        if self.start is None:
            print("Empty")
        end = None
        while end!=self.start:
            p=self.start
            swapped=False
            while p.next!=end:
                if p.info > p.next.info:
                    p.info , p.next.info = p.next.info , p.info
                    swapped=True
                p=p.next
            end=p
            if swapped==False:
                break
        self.disp()
        return
    def bubble_link(self):
        if self.start is None:
            print("Empty")
        end = None
        while end!=self.start:
            p=self.start
            prev=None
            swapped=False
            while p.next!=end:
                q=p.next
                if p.info > q.info:
                    if p==self.start:
                        self.start=q
                    else:
                        prev.next=q
                    p.next=q.next
                    q.next=p
                    p,q=q,p
                prev=p
                p=p.next
            end=p
            if swapped==False:
                break
        self.disp()
        return
list = SSL()
list.create()
data = int(input("Enter the data to be inserted: "))
value = int(input("Specify after which the data has to be inserted: "))
list.insert_after_specified(data,value)
list.disp()
list.reverse_list()
list.disp()
list.bubble_data()
list.bubble_link()