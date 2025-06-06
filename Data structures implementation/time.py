import time
import random
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]
def time_searching(arr, target):
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    return end_time - start_time
sizes = [1000,5000,10000]
for size in sizes:
    random_list = generate_random_list(size)
    target = random.choice(random_list)
    time_taken = time_searching(random_list, target)
    print(f"Time taken to search in list of size {size}: {time_taken:.6f} seconds")