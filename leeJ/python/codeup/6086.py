n = int(input())
count, sum = 0, 0
while True:
    count += 1
    sum += count
    if sum >= n:
        break
print(sum)