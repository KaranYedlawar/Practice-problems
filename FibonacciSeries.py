# Generate Fibonacci series [1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Enter the number, How many terms?  '))

num1 = 0
num2 = 1

count = 0

print(f'Fibonacci series till {num} terms are :')

while count < num:
    print(num1, end=' ')
    nthNumber = num1 + num2
    num1 = num2
    num2 = nthNumber
    
    count += 1
    