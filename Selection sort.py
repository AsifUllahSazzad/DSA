# #Time Complexity -> Worst case: (n-1)+(n-2)+(n-3)+...+1=(n(n-1))/2 => O(n^2)
# #                -> Best case: O(n^2)
# #Space Complexity -> O(n)


#Minimum:
def Selection_Sort_Min(arr):
    for i in range(len(arr)-1):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minimum]:
                temp = arr[minimum]
                arr[minimum] = arr[j]
                arr[j] = temp
    return arr



#Maximum:
def Selection_Sort_Max(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            maximum = j
            if arr[i]>arr[maximum]:
                temp = arr[i]
                arr[i] = arr[maximum]
                arr[maximum] = temp
    return arr

arr = [[89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
]

for i in arr:
    print("Minimum Sorted:",Selection_Sort_Min(i))
print("-----------------------------------------")
for i in arr:
    print("Maximum Sorted:",Selection_Sort_Max(i))