def insertion_sort(arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
def bucket_sort(arr):
    n=len(arr)
    buckets=[]
    for i in range(n):
        buckets.append([])
    for i in range(n):
        index=int((n-1)*(arr[i]//max(arr)))
        buckets[index].append(arr[i])
    for bucket in buckets:
        insertion_sort(bucket)
    i=0
    for bucket in buckets:
        for num in bucket:
            arr[i]=num
            i+=1
arr=[0.42, 0.32, 0.23, 0.52, 0.25]
# arr=[2,3,4,1,6,5,8,7.2,3.5,5.67]
bucket_sort(arr)
print(arr)