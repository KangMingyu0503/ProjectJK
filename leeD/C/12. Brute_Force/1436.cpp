#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 정수를 char형 배열로 변환하기 위한 함수
char* to_string(int num) {
	char* str = (char*)malloc(12);
	sprintf(str, "%d", num);
	return str;
	free(str);
}
int main() {
	int n, k = 0, i = 665;
	int result;
	scanf("%d", &n);

	while (n != k) {
		i++;
		// i를 문자열로 치환 후 666이 포함되어 있으면 k를 1씩 더하여 n이랑 같아질때 까지 반복
		if (strstr(to_string(i), "666") != NULL) {
			k++;
			result = i;
		}
	}
	printf("%d", result);
}
