# cook your dish here
import math
T = int(input())
while(T>0):
    N = int(input())
    maxProf = 0
    while(N>0):
        S,P,V = input().split()
        curProf = (int(V)//(int(S)+1)) * int(P)
        if (curProf>maxProf):
            maxProf = curProf
        N-=1
    print(maxProf)
    T-=1