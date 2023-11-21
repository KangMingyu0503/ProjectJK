h, w = map(int, input().split())
arr = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())
for _ in range(n):
    i, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(i):
            arr[x-1][y-1+j] = 1
    else:
        for j in range(i):
            arr[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()
