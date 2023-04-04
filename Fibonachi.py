def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Введите число n: "))
fib_n = fib(n)
print(fib_n)
