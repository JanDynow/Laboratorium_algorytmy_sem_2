def sumuj(A):
    n = len(A)
    if n == 1:
        return A[0]
    else:
        A1 = A[:n//2]
        A2 = A[n//2:]
        s1 = sumuj(A1)
        s2 = sumuj(A2)
        return s1 + s2
 
A=[10,67,15,9]
print(sumuj(A))






   
        