# Find if the word is a palindrome

word = input('Enter the word to check palindrome: ')

def checkPalindrome(word):
    return word == word[::-1]

if checkPalindrome(word):
    print('Its a palindrome')
else:
    print('Its not a palindrome')