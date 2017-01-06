#!/usr/bin/env python3
# find #n Fibonacci number
from time import time, clock
from sys import argv


def fibonacci(n):
    if n < 2:
        return n
    else:
        fib_stack = [0, 1, ]
        for i in range(n - 1):
            fib_stack[0], fib_stack[1] = \
                fib_stack[1], fib_stack[0] + fib_stack[1]
    return(fib_stack[1])


if len(argv) < 2:
    n = int(input('''
        Вы можете передать порядковый
        номер числа Фибоначчи как аргумент
        при запуске этой программы.

        Вычисление чисел с порядковыми номерами
        более 1 000 000 может занять много времени.

        Введите порядковый номер числа
        из последовательности Фибоначчи:'''))
else:
    n = int(argv[1])

start_time = time()
start_clock = clock()
fibonacci_number = fibonacci(n)
stop_time = time()
stop_clock = clock()

print('''
    %d-ый член последовательности Фибоначчи -
    это: %d
    ''' % (n, fibonacci_number))

print("Время вычисления по time: %s секунд" % (stop_time - start_time))
print("Время вычисления по clock: %s секунд" % (stop_clock - start_clock))
