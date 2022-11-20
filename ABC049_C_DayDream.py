words = ['dream','erase','eraser','dreamer']
flag = True

s = input()
s = s[::-1]

while len(s)>0:
    if s[0:5] == words[0][::-1]:
        s = s.replace(words[0][::-1],'',1)
    elif s[0:5] == words[1][::-1]:
        s = s.replace(words[1][::-1],'',1)
    elif s[0:6] == words[2][::-1]:
        s = s.replace(words[2][::-1],'',1)
    elif s[0:7] == words[3][::-1]:
        s = s.replace(words[3][::-1],'',1)
    else:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')