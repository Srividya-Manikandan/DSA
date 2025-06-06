class Node:
    def __init__(self,value):
        self.info=value
        self.next=None

class CSLL:
    def __init__(self):
        self.start=None
    def create(self):
        n=int(input("No. of elements in the list: "))
        for _ in range(n):
            data=int(input("Enter the data to be entered: "))
            self.insert_end(data)
        return
    def insert_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            temp.next=self.start
            return
        p=self.start
        while p.next!=self.start:
            p=p.next
        temp.next=self.start
        p.next=temp
        return
    def insert_beginning(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            temp.next=self.start
            return
        p=self.start
        while p.next!=self.start:
            p=p.next
        p.next=temp
        temp.next=self.start
        self.start=temp
        return
    def delete(self,value):
        if self.start is None:
            print("Empty")
            return
        if self.start.info==value and self.start.next==self.start:
            self.start=None
            return
        p=self.start
        if self.start.info==value:
            while p.next!=self.start:
                p=p.next
            p.next=self.start.next
            self.start=self.start.next
            return
        prev=None
        while p.next!=self.start and p.info!=value:
            prev=p
            p=p.next
        if p.info==value:
            prev.next=p.next
        else:
            print("Element not found")
        return
    def reverse(self):
        if self.start is None or self.start.next==self.start:
            return
        prev=None
        p=self.start
        q=None
        while p is not None:
            q=p.next
            p.next=prev
            prev=p
            p=q
            if p==self.start:
                break
        self.start.next=prev
        self.start=prev
        return
    def disp(self):
        if self.start is None:
            print("Empty")
            return
        p=self.start
        while p.next!=self.start:
            print(p.info,end=" ")
            p=p.next
        print(p.info)
        return

list = CSLL()
list.create()
list.disp()
list.reverse()
list.disp()
list.insert_beginning(0)
list.disp()
list.delete(0)
list.disp()
list.delete(3)
list.disp()
list.delete(1)
list.disp()
list.delete(2)
list.disp()
