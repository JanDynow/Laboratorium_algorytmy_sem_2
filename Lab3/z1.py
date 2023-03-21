# Zapoznaj się z poniższym algorytmem NWD, a następnie zaproponuj schemat blokowy
# algorytmu oraz jego implementację (rozwiązanie należy zaproponować w formie iteracyjnej
# i rekurencyjnej).

#wersja iteracyjna

def nwdIter(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print(nwdIter(12,18))

#wersja rekurencyjna

def nwdRek(a,b):
    if a!=b:
        if a>b:
            return nwdRek(a-b,b)#a=a-b
        else:
            return nwdRek(a,b-a)#b=b-a
    return a
print(nwdRek(12,18))

#wersja druga
def nwdIterII(a,b):
    while b!=0:
        temp = b
        b = a % b
        a = temp
    return a
print(nwdIterII(12,18))

def nwdRekII(a,b):
    if b!=0:
        return nwdRekII(b,a%b)
    return a
print(nwdRekII(12,18))




