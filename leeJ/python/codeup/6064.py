a, b, c = map(int, input().split())
Min = (a if a<b else b)  if ((a if a<b else b)<c) else c
print(Min)