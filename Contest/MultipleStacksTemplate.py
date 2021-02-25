class TwoStack():
    def __init__(self,size):
        self.stack = []
        #@start-editable@

        self.max_stack_size = size
        self.stack = [None] * size
        self.t1 = -1
        self.t2 = size			
			
	    #@end-editable@

    # define the push operation which  pushes the value into the stack1, must throw a stack full exception
    def push1(self, value):
        #@start-editable@

        if(self.t1+1 >= self.t2):
            print("StackFullException")
            return
        self.t1+=1
        self.stack[self.t1] = value	
			
	    #@end-editable@
        
        

    def push2(self, value):
        #@start-editable@

        if(self.t1 >= self.t2-1):
            print("StackFullException")
            return
        self.t2-=1
        self.stack[self.t2] = value
			
	    #@end-editable@
        
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop1(self):
    
        #@start-editable@

        if(self.t1<0):
            return "StackEmptyException"
        retVal = self.stack[self.t1]
        self.stack[self.t1] = None
        self.t1-=1
        return retVal
			
			
	    #@end-editable@
        
        
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def pop2(self):
        #@start-editable@

        if(self.t2>=self.max_stack_size):
            return "StackEmptyException"
        retVal = self.stack[self.t2]
        self.stack[self.t2] = None
        self.t2+=1
        return retVal
			
			
	    #@end-editable@
        
        


    # returns the number of elements currently in stack2 
    def size1(self):
        #@start-editable@

        return (self.t1+1)
			
			
	    #@end-editable@

    # returns the number of elements currently in stack2 
    def size2(self):
        #@start-editable@

        return self.max_stack_size - self.t2
			
	    #@end-editable@

    def printStacks(self):
        for i in range(self.max_stack_size):
            print(self.stack[i],end=" ")
        print()
        return



def teststacks():
    stacksize=int(input())
    st1 = TwoStack(stacksize)
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S1"):
            print(st1.size1())
        elif(operation[0]=="S2"):
            print(st1.size2())
        elif(operation[0]=="P1"):
            st1.push1(int(operation[1]))
            st1.printStacks()
        elif(operation[0]=="P2"):
            st1.push2(int(operation[1]))
            st1.printStacks()
        elif(operation[0]=="O1"):
            print(st1.pop1())
            st1.printStacks()
        elif(operation[0]=="O2"):
            print(st1.pop2())
            st1.printStacks()
        inputs-=1


def main():
    teststacks()

if __name__ == '__main__':
    main()