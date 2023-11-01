def Bubble_Sort(arr,key):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j][key]>arr[j+1][key]:
                temp = arr[j][key]
                arr[j][key] = arr[j+1][key]
                arr[j+1][key] = temp
elements = [
        { 'name': 'Muna',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'Daniyal', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'Riya',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'Asif',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

Bubble_Sort(elements,key='transaction_amount')

for item in elements:
    print(item)