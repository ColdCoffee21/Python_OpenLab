class stack:
    def __init__(self):
        self.arr = []
        self.arr.append(-1)
        self.top = 0
        
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, val):
        self.top+=1
        self.arr.append(val)
        

    def pop(self):
        self.arr.pop()
        self.top-=1
    
    def size(self):
        return len(self.arr)
        
    def getTop(self):
        return self.arr[self.top]
    
    
    def printArr(self):
        print(self.arr)

n = int(input())
while(n>0):
    curStr = input().strip()
    s = stack()
    M = len(curStr)
    curLen = 0
    balLen = 0
    balStr = ""
    i=0
    while(i<M):
        if(curStr[i] == '('):
            s.push(i)
        else:
            s.pop()
            if(s.isEmpty()):
                s.push(i)
                i+=1
                continue
            curLen = i - s.getTop()
            if(balLen<curLen):
                balLen = curLen
                balStr = curStr[s.getTop()+1:i+1]
        i+=1
    print(str(balLen) +" " + balStr)
    n-=1
#https://www.techiedelight.com/find-length-longest-balanced-parenthesis-string/