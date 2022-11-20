a,b,c = map(int,input().split())
flag = False
sum = 0
for i in range(1,b+1):
    if (a*i)%b == c:
        flag = True

if flag:
    print('YES')
else:
    print('NO')