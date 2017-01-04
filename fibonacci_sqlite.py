#!/usr/bin/env python3
# find #n Fibonacci number
from time import time, clock
# from sys import argv
import sqlite3

start_time = time()
start_clock = clock()

n = 100000

conn = sqlite3.connect('fibonacci_sqlite.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS fibonacci (
            number INTEGER PRIMARY KEY ON CONFLICT IGNORE,
            fibonacci TEXT
            )''')

c.execute('SELECT max(number) FROM fibonacci')
max_id = c.fetchone()[0]
print(max_id)
if n <= max_id:
    exit(0)

# Insert a first row of data (zero)
c.execute('''INSERT INTO fibonacci VALUES (0, '0')''')

# Insert a second row of data (one)
c.execute('''INSERT INTO fibonacci VALUES (1, '1')''')

fib_stack = [0, 1, ]
for i in range(2, n + 1):
    fib_stack[0], fib_stack[1] = \
        fib_stack[1], fib_stack[0] + fib_stack[1]
#    print(i, fib_stack[1])
    c.execute('''INSERT INTO fibonacci VALUES
                    (?, ?)''', (i, str(fib_stack[1])))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

stop_time = time()
stop_clock = clock()

print("Время вычисления по time: %s секунд" % (stop_time - start_time))
print("Время вычисления по clock: %s секунд" % (stop_clock - start_clock))
