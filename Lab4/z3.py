def znajdz_najwiekszy(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    else:
        lewa_polowa = lista[:n//2]
        prawa_polowa = lista[n//2:]
        max_lewa = znajdz_najwiekszy(lewa_polowa)
        max_prawa = znajdz_najwiekszy(prawa_polowa)
        return max_lewa if max_lewa > max_prawa else max_prawa
    
A=[5,19,8,22,10]
    
print(znajdz_najwiekszy(A))   
    
    
    
    
    
    