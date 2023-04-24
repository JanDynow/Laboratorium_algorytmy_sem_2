max = 0

while True:
    liczba = int(input("podaj liczbę naturalną: "))
    if liczba == 0:
        break
    if liczba > max:
        max = liczba
print("Największa liczba z podanych to: ", max)