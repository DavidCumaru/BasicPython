# > REPEAT FOR
"""for variable in range(5):
    print(variable)"""

"""for variable in range(1, 10):
    print(variable)"""

# 1, 4, 7, 10
"""for variable in range(1, 12, 3):
    print(variable)"""

"""grade1 = float(input('inform your grade 1: '))
grade2 = float(input('inform your grade 2: '))
grade3 = float(input('inform your grade 3: '))"""
sum = 0

for i in range(1, 4):
    grade = float(input(f'inform your grade {i}: '))

    sum = sum + grade

print(sum / 3)