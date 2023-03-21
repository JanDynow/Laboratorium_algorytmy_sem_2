#Narysuj schemat blokowy algorytmu, który sprawdza czy podana przez użytkownika wartość występuje w tablicy jednowymiarowej. 
n = int(input("podaj liczbe i sprawdz czy istnieje w tablicy: "))
tab = [-8,-5,-2,0,3,6,11,16]
for i in range(len(tab)):
    if tab[i] == n:
        print("istnieje")
else:
    print("nie istnieje")
