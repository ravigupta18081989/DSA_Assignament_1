str1=input("enter a string 1")
str2=input("enter a string 2")
if len(str1)==len(str2):
    temp=str1+str1
    if str2 in temp:
        print("rotation")
    else:
        print("no rotation")
print("no rotation")