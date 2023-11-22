#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 분해합을 구하는 함수
int get_disassemble(int n) {
	int i;
	for (i = 1; i < n; i++) {
		int temp = i;
		int disassemble = i;
		while (temp > 0) {
			disassemble += temp % 10;
			temp /= 10;
		}
		if (disassemble == n) {
			break;
		}
	}
	return (n == i) ? 0 : i;
}
int main() {
	int n;
	scanf("%d", &n);
	printf("%d", get_disassemble(n));
	return 0;
}
