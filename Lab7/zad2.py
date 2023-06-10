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
    
    def remove_ith_node(self, i):
        current = self.head
        previous = None
        count = 0

        # Przechodzimy do i-tego węzła
        while current is not None and count < i:
            previous = current
            current = current.getNext()
            count += 1
        # Jeśli i-ty węzeł został znaleziony
        if current is not None:
            # Jeśli i-ty węzeł jest głową listy
            if previous is None:
                self.head = current.getNext()
                return print('jestem tutaj')
            else:
                previous.setNext(current.getNext())
                return print("czy jestem tutaj")

            
          

mylist=unOrderdList()
mylist.add(12)
mylist.add(1)
mylist.add(23)
mylist.add(32)

print(mylist.size())
mylist.remove_ith_node(2)
print(mylist.size())
print(mylist.search(1))






