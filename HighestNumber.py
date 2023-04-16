# Find the highest number in an array

arr = [10, 20, 4, 45, 99]

# arr.sort()                                        # Alternate solution
# print("Largest element is:", arr[-1])

# print("Largest element is:", max(arr))

max = arr[0]
for num in arr:
    if num > max:
        max = num


print(f'Largest number is {max}')