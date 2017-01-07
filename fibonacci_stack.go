package main

import (
	"fmt"
	"math/big"
	"os"
	"strconv"
	"time"
)

var t0, t1 time.Time
var fib_number string

func fibonacci(n int) *big.Int {
	a := big.NewInt(0)
	b := big.NewInt(1)
	if n == 0 {
		return a
	} else if n == 1 {
		return b
	} else {
		for i := 0; i < n-1; i++ {
			a.Add(a, b)
			b, a = a, b
		}
		return b
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Print(`
        Вы можете передать порядковый
        номер числа Фибоначчи как аргумент
        при запуске этой программы.

        При вычислении чисел с порядковыми 
        номерами более 100000 возможны зависания ПК.

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
		fibonacci_number := fibonacci(n)
		t1 = time.Now()
		fmt.Printf("%v-й член последовательности Фибоначчи - это: %v\n", n, fibonacci_number)
		fmt.Printf("Время вычисления составило %v.\n", t1.Sub(t0))
	}
}
