#
# Format method
#

out_str = 'Hello, {}'.format('Bob')
print(out_str)

out_str = 'The sum of {} and {} is {}'.format(1,2,3)
print(out_str)

out_str = 'The sum of {} and {} is {}'.format(1.5,2,3.5)
print(out_str)

print('Hello, {}!  The sum of {} and {} is {}'.format('Bob',4,5,9))

print('\n\n')
#
# f method
#
a = 1
b = 2
print(f'The sum {a} and {b} is {a+b}')

a = 1.5
b = 2
print(f'The sum {a} and {b} is {a+b}')

x = [1, 'two', 3]
y = 'Bob'
z = True
print(f'You can print a list {x}, a string ({y}) and a boolean ({z})')

print('\n\n')
#
# % operator method
#
print('The sum of %d and %d is %d' % (1,2, 3))

print('The sum of %.2f and %.1f is %f' % (1.5, 2.0, 3.5))

print('Hello %s!  Here is a boolean value %r.' % ('Bob', True) )
