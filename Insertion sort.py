#Worst case Time Complexity: (n-1)+(n-2)+(n-3)+......+1 = (n(n-1))/2 => O(n^2)
#Best case Time Complexity: O(n)
#Space Complexity: O(1)
def Insert_Sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
    return arr

arr = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
for element in arr:
    print(Insert_Sort(element))