package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	СЛОВА := []string{"питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник"}
    fmt.Printf("%T, %v\n", СЛОВА, СЛОВА)

	слово := СЛОВА[rand.Intn(len(СЛОВА))]
    fmt.Printf("%T, %v\n", слово, слово)
	//	верное := слово
	анаграмма := []string{}

	println(слово)
	word := []rune{}
	for _, letter := range слово {
		word = append(word, letter)
	}
	fmt.Printf("%c\n", word)

	for i, letter := range word {
		fmt.Printf("%d: %c, %c\n", i, letter, (word[i]))
		println()
	}

    fmt.Printf("Word %T\n", string(word))

    println("Len of Word: ", len(word))
/*
	for len(word) >= 0 {
		позиция := rand.Intn(len(word))
		анаграмма = append(анаграмма, word(позиция))
		word = append(word[:позиция],  word[(позиция+1):])
	}
*/
    // начало игры


	fmt.Println(`Добро пожаловать в игру "Анаграммы"!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Enter, не вводя своей версии.)
    `)
	fmt.Println("Вот анаграмма: ", анаграмма)
	//отгадка = input("\nПопробуйте отгадать исходное слово: ")
	//while отгадка != верное and отгадка != "":
	//    print("К сожалению, вы неправы.")
	//    отгадка = input("Попробуйте отгадать исходное слово еще раз: ")

	//if отгадка == верное:
	//    print("Вы отгадали!\n")

	//print("Спасибо за игру.")
	//input("\nНажмите Enter, чтобы выйти.")

}
