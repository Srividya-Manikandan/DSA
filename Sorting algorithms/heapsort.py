"This program is to sort randon n numbers using quick sort and analyse the change in time according to the change in number of inputs."

import time
import random

start = time.time()#calculate starting time

# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i  # Assume the root is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

# Function to perform Heap Sort
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n//2-1,-1,-1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (largest) to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify the reduced heap
        heapify(arr, i, 0)

n=int(input("Enter the number of inputs: "))
arr=[random.randint(0,1000) for _ in range(n)]
heap_sort(arr)
end=time.time()
print("Time taken for ",n," elements is: ",end-start)