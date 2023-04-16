# Find the odd and even numbers in the array

arr = [1,2,3,4,5,6,7,8,9,10]

for i in arr:
    if i % 2 == 0:
        print(f'The number {i} is even')
    elif i % 2 == 1:
        print(f'The number {i} is odd')
    else:
        print("Error, Invalid input")
