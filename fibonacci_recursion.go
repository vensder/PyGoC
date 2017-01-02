package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

var t0, t1 time.Time
var fib_arr = []int{}

func fibonacci(n int) int {
	if n < 2 {
		return n
	} else {
		return (fibonacci(n-2) + fibonacci(n-1))
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println(`
			Введите порядковый номер числа
			из последовательности Фибоначчи
			как аргумент запуска приложения.
			`)
	} else {
		n, err := strconv.Atoi(os.Args[1])
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
		t0 = time.Now()
		for i := 0; i <= n; i++ {
			fib_arr = append(fib_arr, fibonacci(i))
		}
		t1 = time.Now()
		fmt.Printf("%v-й член последовательности Фибоначчи - это: %v\n", n, fib_arr[n])
		fmt.Printf("Вся последовальеность до %v-го члена:\n", n)
		fmt.Println(fib_arr)
		fmt.Printf("Время вычисления составило %v.\n", t1.Sub(t0))
	}

}
