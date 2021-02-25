# cook your dish here
import math
def prec(s):
    if(s == '+' or s == '-'):
        return 1
    elif(s == '*' or s == '/'):
        return 2
    elif(s == '^'):
        return 3
    else:
        return -1
T = int(input())
while(T>0):
    N = int(input())
    exp = input().strip()
    s = []
    ps = []
    for op in exp:
        if(op.isalnum()):
            ps.append(op)
        elif (op == '('):
            s.append(op)
        elif (op == ')'):
            top = s.pop()
            while(top != '('):
                ps.append(top)
                top = s.pop()
        else:
            while((len(s) > 0) and (prec(op)<=prec(s[-1])) and (s[-1] != '(') ):
                ps.append(s.pop())
            s.append(op)
    while (len(s) > 0):
        ps.append(s.pop())
    print("".join(ps))
    T-=1