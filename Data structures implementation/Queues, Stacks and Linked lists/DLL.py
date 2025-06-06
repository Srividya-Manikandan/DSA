class Node:
    def __init__(self,value):
        self.info=value
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.start=None
    def insert_begin(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        temp.next=self.start
        self.start.prev=temp
        self.start=temp
        return
    def insert_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p
        return
    def create(self):
        n=int(input("Enter no. of elements in the list: "))
        for i in range(n):
            data=int(input("Enter data: "))
            self.insert_end(data)
        return
    def display(self):
        if self.start is None:
            print("Empty list")
            return
        p=self.start
        while p is not None:
            print(p.info)
            p=p.next
        return
    def count(self):
        count=0
        if self.start is None:
            return count
        p=self.start
        while p is not None:
            count+=1
            p=p.next
        return count
    def delete(self,value):
        if self.start is None:
            print("Empty list")
            return
        if self.start.info==value and self.start.next is None:
            self.start=None
            return
        if self.start.info==value:
            self.start=self.start.next
            self.start.prev=None
            return
        p=self.start
        while p is not None:
            if p.info==value:
                break
            p=p.next
        if p is None:
            print("Value not found")
        else:
            if p.next is not None:
                p.next.prev=p.prev
            if p.prev is not None:
                p.prev.next=p.next
        return
list = DLL() 

list.create() 
        
while True:
    print("1.INSERT AT END") 
    print("2.DISPLAY") 
    print("3.Count the number of nodes")
    print("4.Insert at beginning")
    print("5.Deleting a value")
    print("6.Quit")
    
        
    option = int(input("Enter your choice : " ))

    if option == 1:
        val = int(input("Data to be inserted: "))
        list.insert_end(val)
    elif option == 2:
        list.display()
    elif option == 3:
        print(list.count())
    elif option == 4:
        val1 = int(input("Data to be inserted: "))
        list.insert_begin(val1)
    elif option == 5:
        val2 = int(input("Data to be deleted: "))
        list.delete(val2)
    elif option == 6:
        break
    else:
        print("wrong option")