class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class SLL:
    def __init__(self):
        self.start = None

    def create_list(self):
        for i in range(70):
            data = i
            self.insert_at_end(data)

    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start = temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp

    def split(self):
        count = 1
        odd = SLL()
        even = SLL()
        p=self.start
        while p is not None:
            count=count+1
            if count % 2 == 1:
                odd.insert_at_end(p.info)
            if count % 2 == 0:
                even.insert_at_end(p.info)
            p=p.link
        odd.display_list()
        print()
        even.display_list()

    def display_list(self):
        if self.start is None:
            print("Empty list")
            return
        p=self.start
        while p is not None:
            print(p.info,end=" ")
            p=p.link
        return

list = SLL() 

list.create_list()

list.split()