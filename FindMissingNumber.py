# Find the missing numbers in a series

arr = [ 1, 2, 3, 4, 6, 7, 8, 9, 10 ]

length = len(arr)
sum = 0
sumTotal = int((length + 1) * (length + 2) / 2)

for i in range(length):
    sum = sum + arr[i]
    

print(f'Missing number is {sumTotal - sum}')

# temp = [0] * (length + 1)                                         (Alternate solution)

# for i in range(0, length):
#     temp[arr[i] - 1] = 1
    
# for i in range(0, length + 1):
#     if (temp[i] == 0):
#         missingNumber = i + 1
        
# print(f'{missingNumber} is missing in above array')