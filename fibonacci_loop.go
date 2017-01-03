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

func fibonacci(n int) []*big.Int {
	var fib_arr []*big.Int
	if n == 0 {
		fib_arr = append(fib_arr, big.NewInt(0))
	} else {
		fib_arr = append(fib_arr, big.NewInt(0), big.NewInt(1))
		sum := big.NewInt(0)
		for i := 0; i < n-1; i++ {
			sum.Add(fib_arr[i], fib_arr[i+1])
			fib_arr = append(fib_arr, sum)
			sum = big.NewInt(0)
		}
	}
	return (fib_arr)
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
		fibonacci_array := fibonacci(n)
		t1 = time.Now()
		fmt.Printf("%v-й член последовательности Фибоначчи - это: %v\n", n, fibonacci_array[n])
		if n <= 100 { // не печатаем всю последовательность, если она длиннее 100
			fmt.Printf("Вся последовательность до %v-го члена:\n", n)
			fmt.Println(fibonacci_array)
		}
		fmt.Printf("Время вычисления составило %v.\n", t1.Sub(t0))
	}
}
