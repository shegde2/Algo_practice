#Program to implement merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i +=1
            else:
                arr[k]=R[j]
                j +=1
            k +=1
        while i < len(L):
            arr[k]=L[i]
            i +=1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        

            

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

if __name__ == '__main__':

    arr=[15,6,2,12,14,8,5]
    print("Given Array is")
    print_array(arr)
    merge_sort(arr)
    print("Sorted Array is")
    print_array(arr)
    
            
        
