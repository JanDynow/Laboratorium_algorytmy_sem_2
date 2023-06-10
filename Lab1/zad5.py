# Zaprojektuj algorytm wyszukiwania w tablicy dwuwymiarowej minimalnej wartości w każdym
# wierszu. Po znalezieniu minimalnej wartości wstaw ją na początek danego wiersza (poprzez
# zamianę miejsc). 
tab = [[4,2,3],[9,18,6],[24,-10,-3],[-6,-5,-6]]
print(tab)
for i in tab:
    min_val = min(i)
    minimum = i.index(min_val)
    i[0],i[minimum] = i[minimum],i[0]
print(tab)





