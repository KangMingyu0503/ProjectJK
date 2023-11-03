def cal_big_o(n):
    num_of_trials = 0
    for i in range(n):
        num_of_trials += 1
    return num_of_trials


num = int(input())

# 시행 횟수
print(cal_big_o(num))
# 최고 차항
print(num // cal_big_o(num))
