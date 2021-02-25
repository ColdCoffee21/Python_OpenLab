class stack:
    def __init__(self):
        self.arr = []
        self.longestStr = ""
        self.balStr = ""
        self.popCount = 0
        
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, val):
        self.arr.append(val)
        self.popCount = 0

    
    def pop(self):
        self.arr.pop()
        self.popCount+=1
        if(self.popCount>1):
            self.balStr = "("+ self.balStr + ")"
        else:
            self.balStr = self.balStr + "()"
        if(self.isEmpty()):
            self.longestStr = self.longestStr + self.balStr
            self.balStr = ""
    
    def size(self):
        return len(self.arr)
    
    def getLongest(self):
        return self.longestStr if (len(self.longestStr) > len(self.balStr)) else self.balStr
    
    def printArr(self):
        print(self.arr)

n = int(input())
while(n>0):
    curStr = input().strip()
    s = stack()
    for i in curStr:
        if(i == '('):
            s.push(i)
            
        elif (i == ')') and (not s.isEmpty()):
            s.pop()
    bestBal = s.getLongest()
    print(str(len(bestBal)) + " " + bestBal)
    n-=1