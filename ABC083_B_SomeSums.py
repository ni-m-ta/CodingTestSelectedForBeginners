n,a,b = map(int,input().split())
sum = 0
'''
for i in range(1,n+1):
    s = str(i)
    num = 0
    for t in range(len(s)):
        num += int(s[t])
    if a <= num and num <= b:
        sum += i
'''

for j in range(1,n+1):
    temp = j
    sumOfDig = 0
    while True:
        sumOfDig += temp%10
        if temp < 10:
            break
        temp //= 10
    if a <= sumOfDig and sumOfDig <= b:
        sum += j

print(sum)
