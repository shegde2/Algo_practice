import math

def jump_search(arr,x,n):
    step=math.sqrt(n)
    print("sqrt of n is %d"%step)

    prev=0
    while arr[int(min(step,n)-1)]<x:
        prev=step
        print("prev %d"%prev)
        step += math.sqrt(n)
        print("Step",step)
        if prev >=n:
            return -1

    while arr[int(prev)] <x:
        prev +=1
        print("inside 2 while prev",prev)
        if prev == min(step,n):
            return -1
    if arr[int(prev)] == x:
        return prev
    return -1
    
    


arr=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
x=1
n=len(arr)
index=jump_search(arr,x,n)
print("Number",x,"is at the index of%d"%index)
