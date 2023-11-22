arr = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1
while arr[x][y] != 2:
    arr[x][y] = 9
    if arr[x][y+1] != 1:
        y += 1
    elif arr[x+1][y] != 1:
        x += 1
    else:
        break
arr[x][y] = 9

for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()