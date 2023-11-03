num = int(input())
num_of_trials = num ** 2
# 시행 횟수
print(num_of_trials)
# 최고 차항
if num_of_trials == 1:
    print(2)
else :
    count = 0
    while(num_of_trials != 1):
        num_of_trials //= num
        count += 1
    print(count)


