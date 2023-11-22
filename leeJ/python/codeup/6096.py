arr = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        arr[x-1][j] = int(not arr[x-1][j])
        arr[j][y-1] = int(not arr[j][y-1])

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
