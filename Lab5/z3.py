n = int(input("podaj rozmiar ciagu: "))
t=[]
for i in range(n):
    if n == 0:
        t.append(1)
    elif n == 1:
        t.append(1)
    else:
        t.append((2*t[i-1]) - t[i-2])

print(t)

