# Insertion Sort
# for i:1 to length(arr)-1:
#     j = 1
#     while j > 0 & arr[j - 1] > arr[j]:
#         swap A[j] and A[j-1]
#         j = j - 1


arr = [50,20,40,60,10,30]
length = len(arr)

for i in range(length):
    key = arr[i]                         
    j = i - 1                                  
    while ((j >= 0) & (arr[j] > key)):
        arr[j+1]=arr[j]
        j -= 1
    arr[j+1] = key
print(arr)


