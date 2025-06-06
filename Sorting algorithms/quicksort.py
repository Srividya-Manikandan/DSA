"This program is to sort randon n numbers using quick sort and analyse the change in time according to the change in number of inputs."

import time
import random

start = time.time()#calculate starting time

# Function to implement quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Choosing pivot as the middle element
    pivot = arr[len(arr) // 2]
    
    # Partitioning the array
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and concatenate
    return quick_sort(left) + mid + quick_sort(right)

n=int(input("Enter the number of inputs: "))
arr=[random.randint(0,10000) for _ in range(n)]
print(arr)
print(quick_sort(arr))
end=time.time()
print("Time taken for ",n," elements is: ",end-start)