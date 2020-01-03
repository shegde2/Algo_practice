#Program to find position of a key element using binary search iterative method

def binary_search(arr,l,r,key):
    while l <=r :
        mid=int((l+r)/2)
        if arr[mid]==key:
            return mid
        elif arr[mid] > key:
            r=mid -1
        else:
            l=mid+1
    else:
        return -1

arr=[10,34,67,89,98,100]
key=100
result=binary_search(arr,0,len(arr)-1,key)

if result != -1:
    print("Element found at index %d"%result)
else:
    print("Oops !! Search for another element..Item is not found")
