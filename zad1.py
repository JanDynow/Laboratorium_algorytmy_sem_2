#Narysuj schemat blokowy algorytmu wyznaczającego pierwiastki równania kwadratowego. 
import math
a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))
delta = 0
if a != 0:
    delta = (b**2)-(4*a*c)
    print(f"Delta wynosi: {delta}")
    if delta > 0:
        x1 = (b*(-1) - math.sqrt(delta))/2*a
        x2 = (b*(-1) + math.sqrt(delta))/2*a
        print(f"Pierwsze miejsce zerowe to: {x1}")
        print(f"Drugie miejsce zerowe to: {x2}")
    elif delta == 0:
        x0 = (b*(-1))/2*a
        print(f"Miejsce zerowe wynosi: {x0}")
    else:
        print("Brak rozwiązań rzeczywistych")








