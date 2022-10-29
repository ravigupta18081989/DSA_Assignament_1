class Stack :
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

    def check_same(self,i,j):
        if j == '{' and i == '}':
            return 1
        elif j == '[' and i == ']':
            return 1
        elif j == '(' and i == ')':
            return 1
        return 0

    def parenthesis_balanced(self,str):
        for i in str:
            if i == '{' or i == '[' or i == '(':
                self.push(i)
            elif i == '}' or i == ']' or i == ')':
                if len(self.stack) == 0:
                    return 0
                value = self.peek()

                if(self.check_same(i,value)):
                    self.pop()
                else:
                    return 0
        if len(self.stack) == 0:
            return 1
        return 0



s=Stack()
if s.parenthesis_balanced("()[({})]"):
    print("balanced")
else:
    print("not balanced ")