n = int(input())
a = [int(input()) for _ in range(n)]
count = 0
flag = False
check = 1

for i in range(1, n+1):
    count += 1
    if a[check-1] == 2:
        flag = True
        break
    check = a[check-1]

if flag:
    print(count)
else:
    print(-1)