arr = []
for i in range(5):
    arr.append(int(input()))

total = sum(arr) / len(arr)
print(int(total))

arr.sort()  # Sort the list in-place
print(arr[2])
