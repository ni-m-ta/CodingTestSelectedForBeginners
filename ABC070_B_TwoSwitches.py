a,b,c,d = map(int,input().split())
time = 0

if a <= c and c <= b and b <= d:
    time = abs(c-b)
elif c <= a and a <= d and d <= b:
    time = abs(a-d)
elif a <= c and d <= b:
    time = abs(c-d)
elif c <= a and b <= d:
    time = abs(a-b)

print(time)