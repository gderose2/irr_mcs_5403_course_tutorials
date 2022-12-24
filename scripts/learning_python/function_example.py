def sample_fun( x, y, z=1 ):
    value = (x**2 + y**2)**0.5
    return z*value



print('Results')

val = sample_fun(3, 4)
print(val)

val = sample_fun(3, 4, 3)
print(val)
