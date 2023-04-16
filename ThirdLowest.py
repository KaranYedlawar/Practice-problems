# Find the 3rd lowest number in an array

arr = [10, 20, 4, 45, 99]

# arr.sort()
# print(f'Third lowest number is {arr[2]}')

length = len(arr)
temp = 0
for i in range(length):
    for j in range(i + 1, length):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(f'Third lowest number is {arr[2]}')