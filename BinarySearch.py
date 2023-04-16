arr = [1, 3, 5, 7, 9, 11, 13]

search = 5

def binarySearch(arr, low, high, search):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == search:
            return mid
        elif arr[mid] > search:
            return binarySearch(arr, low, mid - 1, search)
        else:
            return binarySearch(arr, mid + 1, high, search)
    
result = binarySearch(arr, arr[0], len(arr) - 1, search)

if result != -1:
    print(f'element found at index {result}')
else:
    print(f'element not found')