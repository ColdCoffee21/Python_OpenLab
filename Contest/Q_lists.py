# cook your dish here
l1 = list(map(int,(input().strip().split())))
l2 = list(map(int,(input().strip().split())))
sorted_l1 = l1.sort()
sorted_l2 = l2.sort()

def intersect():
    inter = []
    for i in l1:
        for j in l2:
            if (i==j):
                if i not in inter:
                    inter.append(i)
                break
    #print(inter)
    print(' '.join(list(map(str,inter))))
    return

def difference():
    s1 = set(l1)
    s2 = set(l2)
    l3 = sorted(s2-s1)
    print(' '.join(list(map(str,l3))))
    return

"""def difference(iList):
    for i in l1:
        while(i in iList):
            iList.remove(i)
    #print(iList)
    #print(' '.join(iList))
    print(' '.join(list(map(str,iList))))
    return"""

def knockOut(kList):
    for i in l1:
        if i in kList:
            kList.remove(i)
    #print(kList)
    #print(' '.join(kList))
    print(' '.join(list(map(str,kList))))
    return

N = int(input())
while(N>0):
    choice = str(input().strip())
    if (choice == "I"):
        print("",end = "    ")
        intersect()
    elif (choice == "B"):
        print("",end = "    ")
        knockOut(l2.copy())
    elif (choice == "D"):
        print("",end = "    ")
        difference()
    N-=1