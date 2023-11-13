def Merge(elements,low,mid,high,key,descending):
    temp = []
    left = low
    right = mid+1
    i = 0
    if descending==True:
        while left<=mid and right<=high:
            if elements[left][key]>=elements[right][key]:
                temp.append(elements[left])
                left+=1
            else:
                temp.append(elements[right])
                right+=1
    else:
        while left<=mid and right<=high:
            if elements[left][key]<=elements[right][key]:
                temp.append(elements[left])
                left+=1
            else:
                temp.append(elements[right])
                right+=1

    while left<=mid:
        temp.append(elements[left])
        left+=1
    while right<=high:
        temp.append(elements[right])
        right+=1
    
    for i in range(low,high+1):
        elements[i] = temp[i-low]
    return elements

def MergeSort(elements,low,high,key,descending):
    if low==high:
        return
    mid = (low+high)//2
    MergeSort(elements,low,mid,key,descending)
    MergeSort(elements,mid+1,high,key,descending)
    Merge(elements,low,mid,high,key,descending)
    return elements

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5}
    ]

low = 0
high = len(elements)-1

MergeSort(elements,low,high,key='name',descending = False)

for i in elements:
    print(i)