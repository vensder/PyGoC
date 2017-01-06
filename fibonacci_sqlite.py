#!/usr/bin/env python3
# find #n Fibonacci sequence_number
from time import time, clock
from sys import argv
import sqlite3

if len(argv) < 2:
    n = int(input('''
        Вы можете передать порядковый
        номер числа Фибоначчи как аргумент
        при запуске этой программы.

        Вычисление чисел с порядковыми номерами
        более 100 000 может занять много времени
        при первом запуске, а также требует
        более 1 Гб дискового пространства.

        Введите порядковый номер числа
        из последовательности Фибоначчи:'''))
else:
    n = int(argv[1])

start_time = time()
start_clock = clock()

conn = sqlite3.connect('fibonacci_sqlite1.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS fibonacci (
            sequence_number INTEGER PRIMARY KEY ON CONFLICT IGNORE,
            fibonacci_number TEXT
            )''')

c.execute('SELECT max(sequence_number) FROM fibonacci')
max_id = c.fetchone()[0]

if max_id is None:
    # Insert first two sequence_numbers as a start contition
    c.execute('''INSERT INTO fibonacci VALUES (0, '0')''')
    c.execute('''INSERT INTO fibonacci VALUES (1, '1')''')
    conn.commit()
    c.execute('SELECT max(sequence_number) FROM fibonacci')
    max_id = c.fetchone()[0]


if n > 1 and n > max_id:
    c.execute("SELECT fibonacci_number from fibonacci where sequence_number=?", (max_id-1,))
    first_number = int(c.fetchone()[0])
    c.execute("SELECT fibonacci_number from fibonacci where sequence_number=?", (max_id,))
    second_number = int(c.fetchone()[0])

    fib_stack = [first_number, second_number, ]

    for i in range(max_id + 1, n + 1):
        fib_stack[0], fib_stack[1] = \
            fib_stack[1], fib_stack[0] + fib_stack[1]
        # print(i, fib_stack[1])
        c.execute('''INSERT INTO fibonacci VALUES
                        (?, ?)''', (i, str(fib_stack[1])))

c.execute("SELECT fibonacci_number from fibonacci where sequence_number=?", (n,))

print('''
%d-ый член последовательности Фибоначчи - это:

%s
''' % (n, c.fetchone()[0]))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

stop_time = time()
stop_clock = clock()

print("Время вычисления по time: %s секунд" % (stop_time - start_time))
print("Время вычисления по clock: %s секунд" % (stop_clock - start_clock))
