def fib(n):
    t=[]
    for i in range(n):
        if i == 0:
            t.append(0)
        elif i == 1:
            t.append(1)
        elif i > 1:
            t.append(t[i - 1] + t[i - 2])


print(fib(3))












