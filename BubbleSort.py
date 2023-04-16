# Bubble Sort

num = [5, 4, 6, 2, 8, 1, 0, 3, 5, 2, 6, 7]
length = len(num)
temp = 0

for i in range(length):
    for j in range(0, length-1):
        if num[i] < num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
        
print(f'Ascending : {num}')

for i in range(length):
    for j in range(0, length-1):
        if num[i] > num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
            
print(f'Descending : {num}')
