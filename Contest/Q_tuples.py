import math
def kthLast(tup, k):
    print(tup[-k])

def replaceMid(tup, k):
    l1 =[]
    for i in tup:
        temp = list(i)
        N = len(i)
        mid = (N - 1) // 2
        if(N%2==0):
            temp[mid] = k
            temp[mid+1] = k
        else:
            temp[mid] = k
        l1.append(tuple(temp))
    print(l1)

def median(tup):
    l1 =[]
    for i in tup:
        temp = list(i)
        temp.sort()
        N = len(i)
        if(N%2==0):
            mid = (N - 1) // 2
            med = (temp[mid] + temp[mid+1])/2.0
            l1.append(med)
        else:
            l1.append(temp[int(N/2)])
    print(l1)

def elementsum(tup):
    rowsLen = len(tup)
    colLen = len(tup[0])
    sumL = []
    i = 0
    while(i<colLen):
        sum = 0
        for j in range(rowsLen):
            sum+=tup[j][i]
        sumL.append(sum)
        i+=1
    print(tuple(sumL))





n = int(input())
while(n>0):
    op = input().split()
    if (op[0] == "L"):
        tup = tuple(x.strip(' \'()') for x in input().split(','))
        kthLast(tup, int(op[1]))
    elif (op[0] == "R"):
        tup =[]
        tempTup = input()[1:-1].replace(' ', '')
        for inp in tempTup.split('),('):
            inp = inp.replace(')', '').replace('(', '')
            tup.append(tuple(map(int, inp.strip(" []").split(','))))
            
        replaceMid(tup, int(op[1]))
    elif (op[0] == "M"):
        tup =[]
        tempTup = input()[1:-1].replace(' ', '')
        for inp in tempTup.split('),('):
            inp = inp.replace(')', '').replace('(', '')
            tup.append(tuple(map(int, inp.strip(" []").split(','))))
            
        median(tup)
    elif (op[0] == "S"):
        tup = []
        for i in range(int(op[1])):
            tup.append(tuple(int(x.strip(" ()")) for x in input().split(',')))

        elementsum(tup)
    n-=1