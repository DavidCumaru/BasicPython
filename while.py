
drawn_number = 15

chosen_number = int(input('Enter a number between 1 and 20: '))

while drawn_number != chosen_number:
    print('You got the number wrong, try again...')
    chosen_number = int(input('Enter a number between 1 and 20: '))

print("Congratulations! You're right!")

# Example 2: accountant structure

accountant = 0

while accountant < 5:
    print(accountant)

    accountant = accountant + 1
