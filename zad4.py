#Zaprojektuj algorytm wyszukiwania w tablicy jednowymiarowej minimalnej wartości. 
tab = [-8,-5,-2,0,3,6,11,16,-11,25]
min_val = tab[0]
for i in range(1,len(tab)):
    if tab[i] < min_val:
        min_val = tab[i]
print(f"najmniejsza wartość tablicy to: {min_val}")









