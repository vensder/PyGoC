#!/usr/bin/env python3
# find #n Fibonacci number

def fibonacci(n):
    fib_arr = []
    if n == 0:
        fib_arr = [0]
    else:
        fib_arr = [0, 1]
        for i in range(n-1):
            fib_arr.append((fib_arr[i] + fib_arr[i+1]))
    return(fib_arr)

n = int(input("Введите порядковый номер числа из последовательности Фибоначчи:"))
fibonacci_array = fibonacci(n)

print("%d-ый член последовательности Фибоначчи - это: %d" % (n, fibonacci_array[n]))
print("Вся последовальеность до %d-го члена:" % (n))
print(fibonacci_array)

