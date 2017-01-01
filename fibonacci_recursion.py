#!/usr/bin/env python3
# find #n Fibonacci number

fib_arr = []

def fibonacci(n):
    if n in (0, 1):
        return(1)
    else:
        return(fibonacci(n-2) + fibonacci(n-1))

n = int(input("Введите порядковый номер числа из последовательности Фибоначчи:"))

for i in range(n):
    fib_arr.append(fibonacci(i))

print("%d-ый член последовательности Фибоначчи - это: %d" % (n, fib_arr[n-1]))
print("Вся последовальеность до %d-го члена:" % (n))
print(fib_arr)

