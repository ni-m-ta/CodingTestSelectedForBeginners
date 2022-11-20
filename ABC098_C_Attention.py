n = int(input())
s = input()
num = s.count('E')
ans = num

for i in range(n):
    if s[i] == 'E':
        num -= 1
    if s[i] == 'W':
        num += 1
    print(num)
    if ans > num:
        ans = num

print(ans)