# Linear Search

arr = [5, 4, 3, 7, 8, 9]
length = len(arr)
search = 9

def Lsearch(search):    
    for i in range(0, length):
        if arr[i] == search:
            return i
    return -1
        
ans = Lsearch(search)

if ans != -1:
    print(f'Element found at index {ans}')
else:
    print('Element not found')