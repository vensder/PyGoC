#!/usr/bin/env python3
# Выводит n-й член ряда Фибоначчи
# и всю последовательность до n
from time import time, clock
from sys import argv

fib_arr = []


def fibonacci(n):
    if n < 2:
        return(n)
    else:
        return(fibonacci(n - 2) + fibonacci(n - 1))


if len(argv) < 2:
    n = int(input('''
        Вы можете передать порядковый
        номер числа Фибоначчи как аргумент
        при запуске этой программы.

        Вычисление чисел Фибоначчи
        рекурсивным методом более 30...40 может
        занять много времени.

        Введите порядковый номер числа
        из последовательности Фибоначчи:'''))
else:
    n = int(argv[1])

start_time = time()
start_clock = clock()
for i in range(n + 1):
    fib_arr.append(fibonacci(i))
stop_time = time()
stop_clock = clock()

print("\n%d-ый член последовательности Фибоначчи - это: %d" % (n, fib_arr[n]))
print("Вся последовальеность до %d-го члена:" % (n))
print(fib_arr)
print("Время вычисления по time: %s секунд" % (stop_time - start_time))
print("Время вычисления по clock: %s секунд" % (stop_clock - start_clock))
