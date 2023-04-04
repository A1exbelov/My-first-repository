def fib(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            next_num = fib_seq[i-1] + fib_seq[i-2]
            fib_seq.append(next_num)
        return fib_seq

n = int(input("Введите число n: "))
fib_seq = fib(n)
print(fib_seq)
