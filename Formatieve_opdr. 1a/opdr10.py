def fib(n, n1=0, n2=1):
    while n > 1:
        return fib(n-1, n2, n2+n1)
    print(n2)

fib(9)

