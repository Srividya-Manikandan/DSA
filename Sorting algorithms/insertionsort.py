"This program is to sort randon n numbers using insertion sort and analyse the change in time according to the change in number of inputs."

import time
import random

start = time.time()#calculate starting time

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1]=key


n = int(input("Enter the number of inputs: "))
arr=[random.randint(0,1000)for _ in range(n)] #generating an array of n elements random numbers from 0 to 1000
insertion_sort(arr)
end=time.time() #calculate ending time
print("Time taken for ",n," elements is: ",end-start)