#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ������ char�� �迭�� ��ȯ�ϱ� ���� �Լ�
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
		// i�� ���ڿ��� ġȯ �� 666�� ���ԵǾ� ������ k�� 1�� ���Ͽ� n�̶� �������� ���� �ݺ�
		if (strstr(to_string(i), "666") != NULL) {
			k++;
			result = i;
		}
	}
	printf("%d", result);
}
