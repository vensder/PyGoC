#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <wchar.h>
#include <locale.h>
//#include "utf8.h"

wchar_t *words[] = {L"питон", L"анаграмма", L"простая", L"сложная", L"ответ", L"подстаканник", L"синхрофазатрон", L"世界"};
wchar_t anagram[60] = {0};
wchar_t guess[30];
time_t t;
int rand_number;

int main () {

    setlocale(LC_ALL, "en_US.utf8");

    printf("\tДобро пожаловать в игру \"Анаграммы\"!\n");
    printf("Надо переставить буквы так, чтобы получилось осмысленное слово.\n");
    printf("(Для выхода просто нажимайте Enter, не вводя своей версии.)\n");

	srand((unsigned) time(&t)); // бросаем семя seed в генератор случайных чисел (ГСЧ)
	rand_number = rand() % sizeof(words)/sizeof(words[0]); // ГСЧ от 0 до числа элементов минус один
	
	printf("%ls\n", words[rand_number] ); 
	wchar_t word [wcslen(words[rand_number]) + 1]; // +1 to accommodate for the null terminator
	wcscpy(word, words[rand_number]); // выбираем случайное слово из списка слов
	wchar_t right_word [wcslen(word) + 1];  // +1 to accommodate for the null terminator
	wcscpy(right_word, word); // запоминаем верное слово
	printf("Длина слова %ls: %li\n", right_word, wcslen(right_word));

	while (wcslen(word) > 0) {
		// 9 = 59 % 10
		rand_number = rand() % wcslen(word); // случайное число от нуля до последнего байта -1
		
		anagram[wcslen(anagram)] = word[rand_number];
		//wchar_t word1[60] = {0};
		//wcsncpy(word1, word, rand_number);
		//printf("word1: %ls\n", word1);
		
		
		int i;
		for (i = rand_number; i < wcslen(word)-1 && word[i] != '\0'; i++) {
			word[i] = word[i + 1];
		}
		for (; i < wcslen(word); i++) {
			word[i] = '\0';
		}
	
	}

	printf("У нас получилась такая анаграмма: %ls\n", anagram);
	printf("Попробуйте разгадать ее и ввести правильное слово:");
	fgetws(guess, 30, stdin);
	//wcstok(guess, "\n");
	if (guess != 0) {
		printf("Итак, Вы полагаете, что это %ls\n", guess);
		printf("Нажмите Enter, чтобы поскорее узнать, угадали Вы или нет!");
	} else {
		printf("Если ничего не приходит на ум, то можете просто нажать Enter!\n");
	}
	getchar();
	if ((wcscmp(right_word, guess)) == 0) {
		printf("Поздравляем! Вы очень проницательны! Вы угадали!");
	} else {
		printf("К сожалению, Вы не угадали. Но может повезет в другой раз!\n");
		printf("Нажмите Enter, чтобы подсмотреть правильный ответ: \n");
	    getchar();	
		printf("Правильное слово: '%ls'\n", right_word);
	}

    printf("Нажмите Enter для выхода: \n");
    getchar();


}


