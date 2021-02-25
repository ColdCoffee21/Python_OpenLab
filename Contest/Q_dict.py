n = int(input())
while(n>0):
    charFreq = {}
    maxFreq = {}
    curStr = input().strip().split(" ")
    #print(curStr)
    max = 0
    for cur in curStr:
        for i in cur.lower():
            if (charFreq.get(i) == None):
                charFreq[i] = 1
            else:
                charFreq[i] = charFreq[i] + 1
            if(charFreq[i]> max):
                max = charFreq[i]
    print("",end = "    ")
    for i in charFreq:
        if(charFreq[i]==max):
            maxFreq[i]=max
    #print(maxFreq)
    print(dict(sorted(maxFreq.items())))
    n-=1