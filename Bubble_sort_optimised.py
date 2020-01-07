#Bubble sort optimsed

arr=[10,65,2,90,1]

def buble_sort(arr):
    length=len(arr)
    
    for i in range(length):
        swap=False
        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
            
        if swap==False:
            break

buble_sort(arr)
print("Sorted Array")
for i in range(len(arr)):
    print("%d"%arr[i])
    
        
