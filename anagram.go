package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	СЛОВА := []string{"питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник"}

	слово := СЛОВА[rand.Intn(len(СЛОВА))]
	верное := слово
	анаграмма := []rune{}

	word := []rune{}
	for _, letter := range слово {
		word = append(word, letter)
	}

	fmt.Printf("%d\n", len(word))
	for len(word) > 0 {
		позиция := rand.Intn(len(word))
		анаграмма = append(анаграмма[:], word[позиция:(позиция+1)]...)
		word = append(word[:позиция], word[(позиция+1):]...)
	}

	fmt.Println(`Добро пожаловать в игру "Анаграммы"!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Enter, не вводя своей версии.)
    `)

	fmt.Printf("Вот агаграмма: %c\n", анаграмма)
	fmt.Println("Попробуйте отгадать исходное слово: ")
	отгадка := ""
	fmt.Scanln(&отгадка)
	for отгадка != верное {
		if отгадка == "" {
			break
		}
		println("К сожалению, вы неправы.")
		println("Попробуйте отгадать исходное слово еще раз: ")
		fmt.Scanln(&отгадка)
	}

	if отгадка == верное {
		print("Вы отгадали!\n")
	}

	println("Спасибо за игру.")
	println("Нажмите Enter, чтобы выйти.")
	fmt.Scanln()
}
