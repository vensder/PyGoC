#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

char *words[] = {"питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник", "синхрофазатрон"};
char *word = {0}; char *right_word = {0}; char anagram[60] = {0};
char guess[30];
time_t t;
int rand_number;

int main () {

    printf("\tДобро пожаловать в игру \"Анаграммы\"!\n");
    printf("Надо переставить буквы так, чтобы получилось осмысленное слово.\n");
    printf("(Для выхода просто нажимайте Enter, не вводя своей версии.)\n");

	srand((unsigned) time(&t)); // бросаем семя seed в генератор случайных чисел (ГСЧ)
	rand_number = rand() % sizeof(words)/sizeof(words[0]); // ГСЧ от 0 до числа элементов минус один

	word = strdup(words[rand_number]); // выбираем случайное слово из списка слов
	right_word = strdup(word);

	while (strlen(word) > 0) {
		// 9 = 59 % 10
		rand_number = rand() % strlen(word); // случайное число от нуля до последнего байта -1
		if (rand_number % 2 != 0) {	// используем только четные числа,т.к. работаем с парами.
			if (rand_number == strlen(word)-1)
				rand_number--;  // 10
			else
				rand_number++;
		}
		anagram[strlen(anagram)] = word[rand_number];
		anagram[strlen(anagram)] = word[rand_number+1];
		int i;
		for (i = rand_number; i < strlen(word)-2 && word[i] != '\0'; i++) {
			word[i] = word[i + 2];
		}
		for (; i < strlen(word); i++) {
			word[i] = '\0';
		}
	
	}

	printf("У нас получилась такая анаграмма: %s\n", anagram);
	printf("Попробуйте разгадать ее и ввести правильное слово:");
	fgets(guess, 30, stdin);
	strtok(guess, "\n");
	if (strcmp(guess, "\n") != 0) {
		printf("Итак, Вы полагаете, что это %s\n", guess);
		printf("Нажмите Enter, чтобы поскорее узнать, угадали Вы или нет!");
	} else {
		printf("Если ничего не приходит на ум, то можете просто нажать Enter!\n");
	}
	getchar();
	if ((strcmp(right_word, guess)) == 0) {
		printf("Поздравляем! Вы очень проницательны! Вы угадали!");
	} else {
		printf("К сожалению, Вы не угадали. Но может повезет в другой раз!\n");
		printf("Нажмите Enter, чтобы подсмотреть правильный ответ: \n");
	    getchar();	
		printf("Правильное слово: '%s'\n", right_word);
	}

    printf("Нажмите Enter для выхода: \n");
    getchar();

}