# > FUNCTIONS

# Functions I've used

"""
print() # - Print a message (int, float, str) to console (terminal, cmd).
input() # - Return data provided by the user (standard input) and can receive a string.
len() # - Receive a list and return the size of that list
max() # - Return the largest value from a list
"""

# Creating Functions

# initial function

def language():
    print('Python Language')

language()

# Function with parameters

def salutation(name, langua):
    print(f'Welcome, {name}!')
    print(f'language: {langua}')

salutation('David', 'Python')

# Function with default parameter

def salutation(name, langua='C++'):
    print(f'Welcome, {name}!')
    print(f'language: {langua}')

salutation('Giovana')

# Functions with return

def sum(number1, number2):
    return number1 + number2
result = sum(5,7)

print('The sum result is', result)