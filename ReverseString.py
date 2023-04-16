# Reverse a string without using built in methods

def printReverse(str, pos):
    if pos > -1:
        print(str[pos], end='')
        printReverse(str, pos-1)

str = 'CognitiveClouds'
pos = len(str)
printReverse(str, pos-1)

print()
print(str[ : :-1])                  # Alternative solution

for char in str[ : :-1]:            # Alternative solution
    print(char, end='')
    