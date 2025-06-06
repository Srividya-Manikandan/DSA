import time
import random

start = time.time()

def merge_sort(arr):
    if len(arr)<2:
        return arr
    if len(arr)==2:
        if arr[0]>arr[1]:
            arr[0],arr[1]=arr[1],arr[0]
        return arr
    m=len(arr)//3
    left=[]
    mid=[]
    right=[]
    i=0
    for _ in range(m):
        left.append(arr[i])
        i+=1
    left=merge_sort(left)
    for _ in range(m):
        mid.append(arr[i])
        i+=1
    mid=merge_sort(mid)
    n=i
    for _ in range(n,len(arr)):
        right.append(arr[i])
        i+=1
    right=merge_sort(right)
    #print(left)
    #print(mid)
    #print(right)
    return merge(left,mid,right)

def merge(left,mid,right):
    merged=[]
    i=j=k=0

    while i<len(left) and j<len(mid) and k<len(right):
        if left[i]<=mid[j] and left[i]<=right[k]:
            merged.append(left[i])
            i+=1
        elif mid[j]<=left[i] and mid[j]<=right[k]:
            merged.append(mid[j])
            j+=1
        else:
            merged.append(right[k])
            k+=1

    while i<len(left) and j<len(mid):
        if left[i]<=mid[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(mid[j])
            j+=1
            
    while i<len(left) and k<len(right):
        if left[i]<=right[k]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[k])
            k+=1
    
    while j<len(mid) and k<len(right):
        if mid[j]<=right[k]:
            merged.append(mid[j])
            j+=1
        else:
            merged.append(right[k])
            k+=1

    while i<len(left):
        merged.append(left[i])
        i+=1

    while j<len(mid):
        merged.append(mid[j])
        j+=1

    while k<len(right):
        merged.append(right[k])
        k+=1
    #print(merged)
    return merged

n=int(input("Enter the number of inputs: "))
arr=[random.randint(0,1000) for _ in range(n)]
merge_sort(arr)
end=time.time()
print("Time taken for ",n," elements is: ",end-start)
# arr1=[0,5,1,7,2,9,4,3]
# print(merge_sort(arr1))