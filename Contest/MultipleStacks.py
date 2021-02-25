# cook your dish here
class twoStackArr:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.t1 = 0
        self.t2 = size
        
    def isFull(self):
        return self.t1 == self.t2
        
    def isEmpty(self):
        return ((self.t1<0) or (self.t2>self.size))
    
    def P1(self, val):
        if(self.isFull()):
            print("StackFullException")
            return
        self.arr[self.t1] = val
        self.t1+=1
        self.printArr()

    
    def P2(self, val):
        if(self.isFull()):
            print("StackFullException")
            return
        self.arr[self.t2] = val
        self.t2-=1
        self.printArr()
    
    def O1(self):
        if(self.isEmpty()):
            print("StackEmptyException")
            return
        self.t1-=1
        self.arr[self.t1] = None
        self.printArr()
    
    def O2(self):
        if(self.isEmpty()):
            print("StackEmptyException")
            return
        self.t2-=1
        self.arr[self.t2] = None
        self.printArr()
    
    def S1(self):
        return self.t1
    
    def S2(self):
        return self.t2
    
    def T1(self):
        return self.arr[self.t1]
    
    def T2(self):
         return self.arr[self.t2]

    def printArr(self):
        print(self.arr)

n = int(input()) #size
m = int(input()) #num of ops
S = twoStackArr(n)
while(m>0):
    op = input().strip().split(" ")
    if(op[0] == "P1"):
        S.P1(op[1])
    
    elif(op[0] == "P2"):
        S.P2(op[1])
    
    elif(op[0] == "O1"):
        S.O2()
    
    elif(op[0] == "O2"):
        S.O1()
    
    elif(op[0] == "S1"):
        print(S.S1())
        
    elif(op[0] == "S2"):
        print(S.S2())
        
    elif(op[0] == "T1"):
        print(S.T1())
        
    elif(op[0] == "T2"):
        print(S.T2())
        
    m-=1
    
