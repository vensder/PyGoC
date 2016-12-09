#include <stdio.h>
#include <string.h>

char *words[] = {"питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник"};
char *word;

int main () {

	word = words[5];

	char buf[30];
	int i = 0;
	while (i < strlen(word)) {
	memset(buf,0,sizeof(buf));
	strncpy(buf, &word[i], 2);
	printf("Извлекаем буквы по-одной, присваивая временной переменной buf: %s\n", buf);
	i++; i++;
}

	printf("Выбранное слово: %s\n", word);
	printf("Длина слова: %lu\n", strlen(word));

	printf("Берем буквы через пары указателей:\n");
	char *p1; char *p2;
	    i = 0;
	    while(i < strlen(word)) {
	        p1 = &word[i];
	        p2 = &word[i+1];
	        printf("*p1*p2 = %c%c(%d) \n", *p1,*p2, i);
	        i++; i++;
	    }

	 printf("Выводим слово через putchar: \n");  
	 int index = 0;
	 while (word[index] != '\0') {
	 	putchar(word[index]);
	 	putchar(word[index+1]);
	 	printf(" i: %d\n", index);
	 	index++; index++;
	 }

	printf("\nРазмер элемента слова: %lu\n", sizeof(&word[0]));
	printf("Первая буква в числовом представлении: %d\n", word[0]);
}