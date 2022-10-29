class Using_stack:
    def __init__(self):
        self.stack = []


    def push(self,value):
        self.stack.append(value)
        print("Successfully Added ")

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty !!")
            return
        value=self.stack.pop()
        return value

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty !!")
            return
        return self.stack[len(self.stack)-1]

    def reverse_a_stack(self):
        temp=self.stack[::-1]
        return temp
    
      
        

obj=Using_stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print(f"Before Reverse {obj.stack}")
print(f"After Reverse {obj.reverse_a_stack()}")
