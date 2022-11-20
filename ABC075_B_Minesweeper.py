h,w = map(int,input().split())
s = [list(map(str,input())) for i in range(h)]
for i in range(h):
    for j in range(w):
        count = 0
        if s[i][j] == '#':
            print('#',end='')
        else:
            if i == 0 or j == 0:
                pass
            else:
                if s[i-1][j-1] == '#':
                    count += 1
            if i == 0:
                pass
            else:
                if s[i-1][j] == '#':
                    count += 1
            if i == 0 or j == w-1:
                pass
            else:
                if s[i-1][j+1] == '#':
                    count += 1
            if j == 0:
                pass
            else:
                if s[i][j-1] == '#':
                    count += 1
            if j == w-1:
                pass
            else:
                if s[i][j+1] == '#':
                    count += 1
            if i == h-1 or j == 0:
                pass
            else:
                if s[i+1][j-1] == '#':
                    count += 1
            if i == h-1:
                pass
            else:
                if s[i+1][j] == '#':
                    count += 1
            if i == h-1 or j == w-1:
                pass
            else:
                if s[i+1][j+1] == '#':
                    count += 1
            print(count,end='')
    print()
