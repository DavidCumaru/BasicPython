# > LISTS

# Before
grade1 = 7.9
grade2 = 9.7
grade3 = 8.2

# with list
grade = [7.9, 9.7, 8.2]

# creating lists
list = []
list = list()
list= [26, 'David', 3.1352, False]
list_of_lists = [10, [1, 2, 3]]

# Indexing and slices (slicing)

list = [10, 'David', 3.1415, True]

print(list[0])
print(list[1])
print(list[2])
print(list[3])
#print(list[4])

# Slices

list = [10, 50, 30, 40, 25, 60, 5]

print(list[0:3])
print(list[3:6])
print(list[3:])
print(list[2:6:2])

# > iteration with FOR

# 1. Using the list elements themselves
for elemento in list:
    print(elemento)

# 2. Using the indices

print('list length:', len(list))

for i in range(len(list)):
    print(list[i])

# > list methods

list= [1, 3, 12, 8, 2]

# append

print('before append:', list)

list.append(3)

print('after append:', list)

# insert

list.insert(2, 10)

print('after insert:', list)

# extend

list2 = [4, 2, 3]

list.extend(list2)

print('after extend:', list)

# pop

list.pop()

print('List after pop:', list)

list.pop(0)

print('List after pop:', list)

# remove

list.remove(3)

print('after remove:', list)

# count

print('Quantity of 2 in the list:', list.count(2))

# index

print('Element index 12:', list.index(12))

# sort

list.sort()

print(list)

list.sort(reverse=True)

print(list)

# FUNCTIONS FOR LISTS

# len

print(len(list))

# sum

print(sum(list))

# max

print(max(list))

# min

print(min(list))