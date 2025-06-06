def counting(arr,exp1):
    n=len(arr)
    count=[0]*10
    output=[0]*n
    for i in arr:
        count[(i//exp1)%10]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        output[count[(arr[i]//exp1)%10]-1]=arr[i]
        count[(arr[i]//exp1)%10]-=1
    for i in range(n):
        arr[i]=output[i]
def radix_sort(arr):
    max1=max(arr)
    exp1=1
    while max1//exp1>0:
        counting(arr,exp1)
        exp1*=10
arr=[12,13,4,2,15,6,8,7,10]
radix_sort(arr)
print(arr)