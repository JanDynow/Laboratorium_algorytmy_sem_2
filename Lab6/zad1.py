tabx=[1,2,3,4,5,6]
tabw=[4,6,1,3,7,3]
licznik=0
mianownik=0
for i in range(len(tabx)):
    for j in range(len(tabw)):
        a=tabx[i]*tabw[j]
        licznik=licznik+a
        b=tabw[j]
        mianownik=mianownik+b
xw=licznik/mianownik
print(xw)
        









