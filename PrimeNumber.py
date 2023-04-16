# Find the prime numbers in an array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def checkPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if i * i > num:
            break
        if (num % i) == 0:
            return False
    return True

start = arr[0]
end = arr[-1]+ 1

for i in range(start, end):
    if (checkPrime(i)):
        print(i, end=' ')
