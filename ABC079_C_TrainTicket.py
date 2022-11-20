s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
op = (1,-1)

for i in op:
    for j in op:
        for k in op:
            if a+b*i+c*j+d*k == 7:
                if i == 1:
                    op1 = '+'
                else:
                    op1 = '-'

                if j == 1:
                    op2 = '+'
                else:
                    op2 = '-'

                if k == 1:
                    op3 = '+'
                else:
                    op3 = '-'
                break

print(s[0]+op1+s[1]+op2+s[2]+op3+s[3]+'=7')

