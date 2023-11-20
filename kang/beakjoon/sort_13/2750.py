# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
# for j in range(n):
#     print(arr[j])

n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()
for j in range(n):
    print(arr[j])