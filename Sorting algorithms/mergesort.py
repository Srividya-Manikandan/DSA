import time
import random

start = time.time()

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    merged=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    while i<len(left):
        merged.append(left[i])
        i+=1

    while j<len(right):
        merged.append(right[j])
        j+=1

    return merged

n=int(input("Enter the number of inputs: "))
arr=[random.randint(0,1000) for _ in range(n)]
merge_sort(arr)
end=time.time()
print("Time taken for ",n," elements is: ",end-start)