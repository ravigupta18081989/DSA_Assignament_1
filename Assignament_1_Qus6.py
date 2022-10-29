"""
Infix :- a+b
Postfix :- ab+
Prefix :- +ab
"""

class stack:
    def __init__(Self):
        Self.stack=[]

    def push(self,value):
        self.stack.append(value)
        print("Successfully Added")
    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty!!")
            return
        Value=self.stack.pop()
        return Value
    def peek(self):
        if len(self.stack)==0:
            print("Stack is empty!!")
            return
        return self.stack[len(self.stack)-1]
    def postfix_to_prefix(self,exp):
        str=""
        for i in range(len(exp)):

            if i==len(exp)-1:
                while len(self.stack) !=0:
                        Value1=self.pop()
                        Value2=self.pop()
                        print("Yes")
                        str=str+exp[i]+Value2+Value1
                        return str
            
            elif exp[i].isalpha():
                self.push(exp[i])
            
            elif exp[i]=='/' or exp[i]=='+' or exp[i]=='*' or exp[i]=='-':
                if len(self.stack)!=0:
                    Value1=self.pop()
                    Value2=self.pop()
                    str=str+exp[i]+Value2+Value1
                    self.push(str)
                    str=""

obj=stack()
result=obj.postfix_to_prefix("ABC/-AK/L-*")
print("Prefix expression is =",result)
