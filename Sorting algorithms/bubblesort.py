"This program is to sort randon n numbers using bubble sort and analyse the change in time according to the change in number of inputs."

import time
import random

start = time.time()#calculate starting time

def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1): #start the loop from end of the array to just before 1st element since it will sorted already
        swapped = False 
        for i in range (n): #from starting till n 
            if arr[i]>arr[i+1]: #check if the element is greater than next number
                arr[i],arr[i+1]=arr[i+1],arr[i] #if so swap it
                swapped=True 
        if not swapped: #even after running throughout th earray if swapping doesn't take place 
            break #then the array is sorted and the process can be stopped

n = int(input("Enter the number of inputs: "))
arr=[random.randint(0,1000)for _ in range(n)] #generating an array of n elements random numbers from 0 to 1000
bubble_sort(arr)
end=time.time() #calculate ending time
print("Time taken for ",n," elements is: ",end-start)


