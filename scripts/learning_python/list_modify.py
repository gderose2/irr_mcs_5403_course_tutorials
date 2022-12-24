# Define list
x = [0, 1, 2, 3]
print('1) ', x)
print('')

# Append another element
x.append(4)
print('2) ', x)
print('')

# Append another list
y = [5, 6, 7]
print('3) ', x+y)
print('')
x.extend(y)
print('4) ', x)
print('')

# Remove elements
x[0:-4] = []
print('5) ', x)
print('')

# Append an element to the beginning of the list
x[:0] = [0,1]
print('6) ', x)
print('')

# Inserting in the middle
x.insert(2,3)
x.insert(2,2)
print('7) ', x)
