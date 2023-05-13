import random
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def denqueue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

ludzie=['Brad','Billl','David','Susan','Jane','Kent']
q=Queue()

for x in ludzie:
    q.enqueue(x)

while q.size()>1:
    i=random.randint(1,15)
    while i!=0:
        tym=q.denqueue()
        q.enqueue(tym)
        i=i-1
    q.denqueue()

print(q.items)