# Selection Sort

arr = [5, 4, 6, 2, 8, 1, 0, 3, 5, 2, 6, 7]

for i in range(len(arr)-1):
    minIndex = i
    for j in range(i + 1, len(arr)):
        if (arr[j] < arr[minIndex]):
            minIndex = j
    
    temp = arr[i]
    arr[i] = arr[minIndex]
    arr[minIndex] = temp
    
    
    
print(f'Array sorted using selection sort : {arr}')