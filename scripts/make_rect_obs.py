#!/usr/bin/env python3
import sys

# Check inputs
if( len(sys.argv) != 5 ):
    print('Usage %s rect_center_x rect_center_y width heght' % sys.argv[0])
    sys.exit(0)


xc = float(sys.argv[1])
yc = float(sys.argv[2])
w = float(sys.argv[3])
h = float(sys.argv[4])

out_str = 'rect: [%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f]' % (
    xc-w/2, yc+h/2, xc+w/2, yc+h/2, xc+w/2, yc-h/2, xc-w/2, yc-h/2 )

print(out_str)

    
    
