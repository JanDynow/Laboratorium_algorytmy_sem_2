def hanoi(n, A, B, C):
    if n > 0:  
        hanoi(n-1, A, C, B)
        print("Przenieś dysk", n, "z kija", A, "na kij", C)
        hanoi(n-1, B, A, C)
print(hanoi(3,'startowy','roboczy','docelowy'))
        
        
        
        
        
        