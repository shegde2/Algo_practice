
def binary_search(arr,l,r,key):
    if r>= l:
        mid=int((l+r)/2)
        print(mid)
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binary_search(arr,l,mid-1,key)
        else:
            return binary_search(arr,mid+1,r,key)
    else:
        return -1
    

    



arr=[3,4,9,46,67,89]
key=46
result=binary_search(arr,0,len(arr)-1,key)

if result != -1:
    print("Element found at location %d"%result)
else:
    print("No Element found")
                     
