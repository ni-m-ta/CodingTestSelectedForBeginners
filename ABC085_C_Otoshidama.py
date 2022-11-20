n,Y = map(int,input().split())
flag = False
for x in range(0,n+1):
    for y in range(0,n+1):
        if n-x-y >= 0 and 10000*x + 5000*y + 1000*(n-x-y) == Y:
            flag = True
            a = x
            b = y
            c = (n-x-y)
            break

if flag:
    print(str(a)+' '+str(b)+' '+str(c))
else:
    print('-1 -1 -1')