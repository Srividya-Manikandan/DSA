class Node:
    def __init__(self,value):
        self.info = value 
        self.link = None 
        

class SingleLinkedList:

    def __init__(self):
        self.start = None
    
    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for _ in range(n):
            data = int(input("Enter the element to be inserted : "))
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
    
    def insert_at_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def delete_element(self, value):
        if self.start is None:
            print("Empty list")
            return
        if self.start.info == value:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
            if p.link.info==value:
                break
            p=p.link
        if p.link is None:
            print(value,"- Not in list")
        else:
            p.link = p.link.link
            


    def count_nodes(self):
        count = 0
        if self.start is None:
            return count
        p=self.start
        while p is not None:
            count=count+1
            p=p.link
            
        return count
    
    def display_list(self):
        if self.start is None:
            print("Empty list")
            return
        p=self.start
        while p is not None:
            print(p.info,"\t")
            p=p.link
        return

list = SingleLinkedList() 

list.create_list() 
        
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
        list.insert_at_end(val)
    elif option == 2:
        list.display_list()
    elif option == 3:
        print(list.count_nodes())
    elif option == 4:
        val1 = int(input("Data to be inserted: "))
        list.insert_at_beginning(val1)
    elif option == 5:
        val2 = int(input("Data to be deleted: "))
        list.delete_element(val2)
    elif option == 6:
        break
    else:
        print("wrong option")
