#!/usr/bin/env python3
# find #n Fibonacci number
from time import time, clock

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

start_time = time()
start_clock = clock()
fibonacci_array = fibonacci(n)
stop_time = time()
stop_clock = clock()

print("%d-ый член последовательности Фибоначчи - это: %d" % (n, fibonacci_array[n]))
print("Вся последовальеность до %d-го члена:" % (n))
print(fibonacci_array)
print("Время вычисления по time: %s секунд" % (stop_time - start_time))
print("Время вычисления по clock: %s секунд" % (stop_clock - start_clock))

