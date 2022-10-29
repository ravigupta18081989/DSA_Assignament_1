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
    
    def find_smallest_no(self):
        min_value=999999
        for i in range(len(self.stack)):
            if self.stack[i] < min_value:
                min_value=self.stack[i]
        return min_value
        
        

obj=Using_stack()
obj.push(5)
obj.push(15)
obj.push(25)
obj.push(35)
print(f"SMALLEST NUMBER IS  {obj.find_smallest_no()}")