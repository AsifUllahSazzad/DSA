def Merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1

    #Compare left and right side and add element:
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    #Extra Element add left side:
    while left<=mid:
        temp.append(arr[left])
        left+=1
    #Extra Element add right side:
    while right<=high:
        temp.append(arr[right])
        right+=1

    #Copy temporary array to original array:
    for i in range(low,high+1):
        arr[i] = temp[i-low]
    return arr

def MergeSort(arr,low,high):
    #base case:
    if low==high:
        return
    #Divide into two parts:
    mid = (low+high)//2

    #left side recursive call:
    left = MergeSort(arr,low,mid)
    #right side recursive call:
    right = MergeSort(arr,mid+1,high)
    
    #Conquer and Combine (Merge) function:
    Merge(arr,low,mid,high)
    return arr

arr = [80,30,20,100,40,60,10,90,70,50]
low = 0
high = len(arr)-1
MergeSort(arr,low,high)
print("Sorted Array is:",arr)