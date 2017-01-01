#!/usr/bin/env python3
# Выводит n-й член ряда Фибоначчи
# и всю последовательность до n

fib_arr = []

def fibonacci(n):
    if n < 2:
        return(n)
    else:
        return(fibonacci(n-2) + fibonacci(n-1))

n = int(input("Введите порядковый номер числа из последовательности Фибоначчи:"))

for i in range(n+1):
    fib_arr.append(fibonacci(i))

print("%d-ый член последовательности Фибоначчи - это: %d" % (n, fib_arr[n]))
print("Вся последовальеность до %d-го члена:" % (n))
print(fib_arr)

