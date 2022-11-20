n = int(input())
a = [list(map(int,input().split())) for _ in range(2)]
count = 0
counts = []
for i in range(n):
    count = 0
    for j in range(i+1):
        count += a[0][j]
    for k in range(i,len(a[1])):
        count += a[1][k]
    counts.append(count)

print(max(counts))
    