#!/usr/bin/python3

def quadratic(a, b, c):
    # Check input for x^2 coefficient
    if( a == 0.0 ):
        return None
    
    # Compute roots
    x = -b
    y = (b*b - 4.0*a*c)**0.5
    roots = [ (x-y)/(2*a), (x+y)/(2*a)]
    return roots

if __name__ == '__main__':
    print('sample_module loaded...')

    
