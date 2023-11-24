def fibo(n):
    fib1 = 0
    fib2 = 1
    fiboseries = [fib1,fib2]
    while(n-2>0):
        fibonext = fib1 + fib2
        fiboseries.append(fibonext)
        fib1 = fib2
        fib2 = fibonext
        n -= 1
    return fiboseries

n=7

fibonaciseries = fibo(n)
print(fibonaciseries)