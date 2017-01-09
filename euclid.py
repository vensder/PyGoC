#!/usr/bin/env python3

from time import time, clock
from sys import argv, exit as sys_exit


def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a)


def euclid_div(a, b):
    while b:
        a %= b
        a, b = b, a
    return (a)


if len(argv) < 2:
    a = int(input('''
        Вы также можете передать два числа для нахождения НОД
        (наибольшего общего делителя) по алгоритму Евклида,
        как аргументы при запуске этой программы.

        Введите первое число:'''))
    b = int(input('''
        Введите второе число:'''))
elif len(argv) == 2:
    print("Для вычисления НОД требуется ввести два числа.")
    sys_exit(0)
else:
    a = int(argv[1])
    b = int(argv[2])

if a == 0 or b == 0:
    print("Полно-те, зачем вам для нуля рассчитывать в программе? :)")
    sys_exit(0)

start_time = time()
start_clock = clock()
nod1 = euclid(a, b)
stop_time = time()
stop_clock = clock()

print('''
        Наибольший общий делитель по Евклиду вычитанием: %d\n''' % nod1)
print("Время вычисления по time: %s секунд" % (stop_time - start_time))
print("Время вычисления по clock: %s секунд" % (stop_clock - start_clock))

start_time = time()
start_clock = clock()
nod2 = euclid_div(a, b)
stop_time = time()
stop_clock = clock()

print('''
        Наибольший общий делитель по Евклиду делением: %d\n''' % nod2)
print("Время вычисления по time: %s секунд" % (stop_time - start_time))
print("Время вычисления по clock: %s секунд" % (stop_clock - start_clock))
