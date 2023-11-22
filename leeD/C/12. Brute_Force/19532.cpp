#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int arr[6];

	for (int i = 0; i < 6; i++) {
		scanf("%d", &arr[i]);
	}
	// 2차원 배열을 이용하면 더 쉽게 구현 가능하지만 브루트 포스에 맞게끔 코드를 구현
	for (int i = -999; i < 1000; i++) {
		for (int j = -999; j < 1000; j++) {
			if ((arr[0] * i) + (arr[1] * j) == arr[2] && (arr[3] * i) + (arr[4] * j) == arr[5]) {
				printf("%d %d", i, j);
				break;
			}
		}
	}
}