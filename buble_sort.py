#Program for buble sort

def buble_sort(arr):
    length=len(arr)
    for index in range(length):
        print("index",index)
        for inside_index in range(0,length-index-1):
            print("index for",inside_index)
            if arr[inside_index]>arr[inside_index+1]:
                print("inside_index",inside_index)
                arr[inside_index],arr[inside_index+1]=arr[inside_index+1],arr[inside_index]
                
    

arr=[2,64,34,25,12,22,90]
buble_sort(arr)
print("Sortedf Array")
for i in range(len(arr)):
    print("%d"%arr[i])
