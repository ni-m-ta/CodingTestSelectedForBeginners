n = int(input())
ts = [list(map(int,input().split())) for i in range(n)]

flag = True

if n == 1:
    if ts[0][0] < ts[0][1] + ts[0][2]:
        flag = False
    if ts[0][0]%2 != (ts[0][1] + ts[0][2])%2:
        flag = False
else:
    for i in range(n-1):
        if abs(ts[i+1][0] - ts[i][0]) < abs(ts[i+1][1] - ts[i][1]) + abs(ts[i+1][2] - ts[i][2]):
            flag = False
        if (ts[i+1][0] - ts[i][0])%2 != ((ts[i+1][1] - ts[i][1]) + (ts[i+1][2] - ts[i][2]))%2:
            flag = False

if flag:
    print('Yes')
else:
    print('No')