def wyniki(i):
    print("wywołano")
    if(i<3):
        # print("mniejsze od 3")
        return 1 

    if (i%2==0):
        # print("parzyste")
        return (wyniki(i-3)+(wyniki(i-1)+1))
    else:
        # print("modulo")
        return (wyniki((i-1)%7))

print(wyniki(4))