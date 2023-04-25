#zadeklarować 2 zmienne 1 boolowska zakładająca ze stos jest poprawny oraz zmienna index służąca do przechopdzenia do przechodzenia po elementach listy
# wchodzimy do while dopóki index jest mniejszy od size(stosu) lub do wystapienia pierwszego błędu
# odczytaj kolejny znak kolejnymkrokiem bedczie jeśli znak jest ( dodaj znak na stos w przeciwnym wypadku oznacza że jest to ) sprawdź czy stos jest pusty to pod zmienna podstaw false
# w przeciwnym wypadku ściąg element ze stosu i przejdź do klolejnego elementu
#

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


s = Stack()
a= "(())()()"
tab = list(a)
l = len(a)
i=0
b=0
#print(tab)
while i < l:
    if tab[i] == '(':
        s.push(tab[i])
        #print('otwierajacy')
    else:
        if s.isEmpty():
            b=+1
        else:
            s.pop()
            #print('zamykajacy')
    i += 1
if b == 0:
    if s.isEmpty():
        print("Wszystko jest pootwierane i pozamykane")
    else:
        print("Brakuje otwierających nawiasów: ", s.size())
        #print(s.size())
else:
    print("za dużo zamykających: ", b)





