arr=[5,6,4,7,6,3]
target_no=10
pair_array=[]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        sum = arr[i]+arr[j]
        if sum ==target_no:
            pair_array.append([arr[i],arr[j]])


print(pair_array)