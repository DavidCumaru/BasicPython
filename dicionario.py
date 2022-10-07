# > DICTIONARIES

# creating dictionaries

from operator import truediv

dictionary = {}
dictionary = dict()

dictionary = {'name': 'David', 'age': 23, 'height': 1.68}

print(dictionary)
print(dictionary['age'])

# Adicionando elementos em um dicionario

dictionary['developer'] = True

print(dictionary)

dictionary['height'] = 2

print(dictionary)

# Iterating through a dictionary

for key in dictionary:
    print(key, dictionary[key])

# Testing for the existence of a key

print('weight' in dictionary)
print('height' in dictionary)