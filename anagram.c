#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

char *words[] = {"питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник"};
char *word; char *right_word; char anagram[60];
time_t t;
int rand_number;

int main () {

	srand((unsigned) time(&t)); // бросаем семя seed в генератор случайных чисел 
	rand_number = rand() % 6; // генератор случайных чисел от 0 до 5 для выбора слова
	if (rand_number > 5) { // на всякий случай, чтобы успокоить параною выхода за пределы массива
		rand_number = 5;
	}
	printf("%d\n", rand_number);
	word = words[rand_number]; // выбираем случайное слово из списка слов
	right_word = word;

	rand_number = rand() % strlen(word); // пара байт на русскую буквую, работаем с парами.
	printf("rand_number: %d\n", rand_number);
	// извлекаем эту случайную букву (пару байт - четный:нечетный) из слова, 
	// помещаем в другое (anagram)

	char buf[10];
	memset(buf,0,sizeof(buf));
	strncpy(buf, &word[0], 2); // как раз два байта в буфер.
	strcat(anagram, buf); // конкатенируем случайную букву к анаграмме
	printf("anagram: %s\n", anagram);


	
	int i = 0;
	while (i < strlen(word)) {
	//memset(buf,0,sizeof(buf));
	strncpy(buf, &word[i], 2);
	printf("Temp buf: %s\n", buf);
	i++; i++;
}
	printf("Выбранное слово: %s\n", word);
	printf("Длина слова: %lu\n", strlen(word));

	 printf("Выводим слово через putchar: \n");  
	 int index = 0;
	 while (index < strlen(word)) {
	 	putchar(word[index]);
	 	putchar(word[index+1]);
	 	printf(" i: %d\n", index);
	 	index++; index++;
	 }

	printf("\nРазмер элемента слова: %lu\n", sizeof(&word[0]));
	printf("Первая буква в числовом представлении: %d\n", word[0]);
}