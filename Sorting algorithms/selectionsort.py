"This program is to sort randon n numbers using selection sort and analyse the change in time according to the change in number of inputs."

import time
import random

start = time.time()#calculate starting time

def selection_sort(arr):
    n=len(arr)
    for i in range(n): #iterate through the array
        min=i #set min pointer to current element's index
        for j in range(i+1,n): #iterate from next element till end
            if arr[min]>arr[j]: #if any element is less than minimum element
                min=j #change the min pointer
        arr[i],arr[min]=arr[min],arr[i] #swap current element with minimum element 

n = int(input("Enter the number of inputs: "))
arr=[random.randint(0,1000)for _ in range(n)] #generating an array of n elements random numbers from 0 to 1000
selection_sort(arr)
end=time.time() #calculate ending time
print("Time taken for ",n," elements is: ",end-start)



