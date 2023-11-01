#Time Complexity:
#Worst case: (n-1)+(n-2)+(n-3)+.....+1 = (n(n-1))/2 => O(n^2)
#Space: O(1)
def BubbleSort(arr):
    size = len(arr)
    for i in range(size-1): #Step
        for j in range(size-i-1): #Iteration
            if arr[j]>arr[j+1]: #Compare
                #Swap:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [50,40,30,20,10] #Space => O(1)
BubbleSort(arr)
print(arr) #[10, 20, 30, 40, 50]


#Time Complexity:
#Best Case: O(n)
#Space Complexity: O(1)
def Bubble_Sort(arr):
    for i in range(len(arr)-1):
        stop = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                stop = True
        if stop == False:
            break

arr = [10,20,30] #Space => O(1)
Bubble_Sort(arr)
print(arr) #[10, 20, 30]