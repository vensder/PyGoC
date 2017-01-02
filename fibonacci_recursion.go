package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

var t0, t1 time.Time
var fib_arr = []int{}
var fib_number string

func fibonacci(n int) int {
	if n < 2 {
		return n
	} else {
		return (fibonacci(n-2) + fibonacci(n-1))
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Print(`
        Вы можете передать порядковый
        номер числа Фибоначчи как аргумент
        при запуске этой программы.

        Вычисление чисел Фибоначчи
        рекурсивным методом более 30...40 может
        занять много времени.

        Введите порядковый номер числа
        из последовательности Фибоначчи:`)
		fmt.Scanln(&fib_number)
	} else {
		fib_number = (os.Args[1])
	}

	n, err := strconv.Atoi(fib_number)
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	} else {
		t0 = time.Now()
		for i := 0; i <= n; i++ {
			fib_arr = append(fib_arr, fibonacci(i))
		}
		t1 = time.Now()
		fmt.Printf("%v-й член последовательности Фибоначчи - это: %v\n", n, fib_arr[n])
		fmt.Printf("Вся последовательность до %v-го члена:\n", n)
		fmt.Println(fib_arr)
		fmt.Printf("Время вычисления составило %v.\n", t1.Sub(t0))
	}
}
