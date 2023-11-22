#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void) {
	int m, n;
	char board[50][51];
	int cntW = 0, cntB = 0, min = 100;

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		scanf("%s", &board[i]);
	}
	for (int i = 0; i < n - 7; i++) {
		for (int j = 0; j < m - 7; j++) {
			cntW = 0;
			cntB = 0;
			for (int x = i; x < i + 8; x++) {
				for (int y = j; y < j + 8; y++) {
					if (((x + y) % 2) == 0) {
						if (board[x][y] == 'W') {
							cntB++;
						}
						else {
							cntW++;
						}
					}
					else {
						if (board[x][y] == 'B') {
							cntB++;
						}
						else {
							cntW++;
						}
					}
				}
				min = ((cntB < min) ? cntB : min);
				min = ((cntW < min)? cntW : min);
			}
		}
	}
	printf("%d", min);

	return 0;
}