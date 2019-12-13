#Program for linear search

def linear_search(arr,key,length):
    for i in range(0,length):
        if (arr[i]==key):
            
            return i
    return -1
    

arr=[10,20,40,60,55,110,89,64,2]
key=110
length=len(arr)
result=linear_search(arr,key,length)
if result==-1:
    print("Item not found")
else:
    print("Item found at location",result)
