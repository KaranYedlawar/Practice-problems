# Find the vowels and consonants in a word/sentence

sentence = 'I am an employee of CognitiveClouds. My company is best.'

for char in sentence:
    # if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':       - (Alternative solution)

    if char in ['a', 'e', 'i', 'o', 'u']:
        print(f'{char} is a Vowel')
    elif char in [' ', ',', '.']:
        continue
    else:
        print(f'{char} is a Consonant')

