h,w = map(int,input().split())
s = [list(map(str,input())) for i in range(h)]
flag = True

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if i == 0 and j == 0:
                if s[i+1][j] == '.' and s[i][j+1] == '.':
                    flag = False
            elif i == 0 and j == w-1:
                if s[i+1][j] == '.' and s[i][j-1] == '.':
                    flag = False
            elif i == h-1 and j == 0:
                if s[i-1][j] == '.' and s[i][j+1] == '.':
                    flag = False
            elif i == h-1 and j == w-1:
                if s[i-1][j] == '.' and s[i][j-1] == '.':
                    flag = False
            elif i == 0:
                if s[i][j+1] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.':
                    flag = False
            elif j == 0:
                if s[i-1][j] == '.' and s[i][j+1] == '.' and s[i+1][j] == '.':
                    flag = False
            elif j == w-1:
                if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.':
                    flag = False
            elif i == h-1:
                if s[i-1][j] == '.' and s[i][j+1] == '.' and s[i][j-1] == '.':
                    flag = False
            else:
                if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j+1] == '.' and s[i][j-1] == '.':
                    flag = False

if flag:
    print('Yes')
else:
    print('No')


