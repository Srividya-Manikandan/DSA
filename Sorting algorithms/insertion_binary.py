def binarySearch(arr,elem,low,high):
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid]==elem:
            return mid+1
        elif arr[mid]>elem:
            high=mid-1
        else:
            low=mid+1
    return low
def insertionSort(arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        j=i-1
        pos=binarySearch(arr,key,0,j)
        while (j>=pos):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[2,5,4,3,6,1,9,8]
insertionSort(arr)
print(arr)