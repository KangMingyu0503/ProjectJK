n = int(input())
m = int(input())
m_lst = [int(i) for i in str(m)]

for num in range(len(m_lst)):
    print(n * m_lst[-(num + 1)])

print(n * m)