n = int(input())
a = list(map(float,input().split()))
count = 0
flag = True

while True:
    for i in range(n):
        if a[i]%2 != 0:
            flag = False
        a[i] /= 2
    if flag == False:
        break
    count += 1

print(count)