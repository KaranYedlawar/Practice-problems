# Split the sentence in words

sentence = 'I am an employee of CognitiveClouds. My company is best.'

newList = []
temp = ''

for char in sentence+' ':
    if char == ' ':
        newList.append(temp)
        temp = ''
    else:
        temp+=char

print(newList)