# 이 문제는 1번째 삼각수에서 n-2번째 삼각수의 합을 구하는 문제와 같다
n = int(input())

# 반복문의 조건에 따라 n이 1이나 2면 실행을 안 한다
if n == (1 or 2):
    num_of_trials = 0
else :
    n -= 2
    num_of_trials = (n * (n+1) * (n+2)) // 6

print(num_of_trials)
print(3)