#Python code for selection sort

import sys
A=[2,33,28,12,98,26]

for i in range(len(A)):
    print("I",i)
    min_index=i
    for j in range(i+1,len(A)):
        if A[min_index]>A[j]:
            print("j",j)
            min_index=j
    A[i],A[min_index]=A[min_index],A[i]

print("Sorted Array")
for i in range(len(A)):
    print("%d"%A[i])
            
