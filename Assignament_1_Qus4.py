str=input("enter a string")
count=0
d={}
for i in range(len(str)):
    if str[i] in d.keys():
        continue
    for j in range(i+1,len(str),1):
        if str[i]==str[j]:
            count+=1
    d[str[i]]=count
    count=0
for i in d:
    if d[i]==0:
        print("First Non-repeated value is ",i)
        break

print(d)