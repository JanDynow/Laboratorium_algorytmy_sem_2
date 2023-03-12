n = int(input("Podaj ilość liczb do wczytania: "))
count = 0

for i in range(1, n+1):
    x = int(input(f"Podaj {i}. liczbę całkowitą: "))
    if x < 0:
        count += 1

print(f"Ilość liczb ujemnych w ciągu wynosi: {count}")