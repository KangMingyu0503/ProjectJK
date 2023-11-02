fa1 , fa0 = input().split()
fa1,fa0 = int(fa1),int(fa0)
c = int(input())
n0 = int(input())

if (fa1*n0 + fa0) <= (c*n0) and (fa1<=c):
    print(1)
else:
    print(0)