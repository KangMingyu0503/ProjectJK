n = int(input())
a = list(map(int, input().split()))
d = [0 for _ in range(23)]
for i in range(n):
    d[a[i]-1] += 1
for i in d:
    print(i, end=" ")
