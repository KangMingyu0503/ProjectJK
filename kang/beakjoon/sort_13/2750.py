n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr = list(set(arr))
arr.sort()
for j in range(n-1):
    print(arr[j])