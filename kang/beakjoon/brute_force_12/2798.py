card_num, max_num = map(int,input().split())
card_list = list(map(int,input().split()))
total = 0
for i in range(card_num):
    for j in range(i+1,card_num):
        for k in range(j+1,card_num):
            if card_list[i]+card_list[j]+card_list[k] > max_num:
                continue
            else:
                total = max(total,card_list[i]+card_list[j]+card_list[k])
print(total)