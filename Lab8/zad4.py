# lilista jdnokierunkowa

class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getdata(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext

#temp=Node(93)


class unOrderdList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self,item):
        temp= Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current= self.head
        count=0
        while current != None:
            count= count+1
            current = current.getNext()
        return count

    def search(self,item):
        current=self.head
        found=False
        while current != None and not found:
            if current.getdata() == item:
                found=True
            else:
                current=current.getNext()
        return found


    def remove(self,item):
        current=self.head
        previous= None
        found=False
        while not found:
            if current.getdata()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def display(self):
        current = list.head
        while current is not None:
            print(current.getdata())
            current = current.getNext()
        

    def addsort(self,item):
        temp = Node(item)

        if self.head is None or item <= self.head.getdata():
            # Wstawianie na początek listy lub do pustej listy
            temp.setNext(self.head)
            print("to jest pierwszy temp: ", temp.getdata())
            self.head = temp
        else:
            current = self.head
            previous = None

            while current is not None and item > current.getdata():
                previous = current
                print('to jest previous w while ', previous.getdata())
                current = current.getNext()
                print('to jest current w while ', current.getdata())

            # Wstawianie w środek lub na koniec listy
            temp.setNext(current)
            print("to jest temp: ", temp.getdata())
            previous.setNext(temp)
            print("to jest previous: ", previous.getdata())



list = unOrderdList()
list.addsort(8)
unOrderdList.display(list)
print(".............")
list.addsort(5)
unOrderdList.display(list)
print(".............")
list.addsort(2)
unOrderdList.display(list)
print(".............")
list.addsort(3)
unOrderdList.display(list)
print(".............")







