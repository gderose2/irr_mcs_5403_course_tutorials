#!/usr/bin/env python3

# Import OpenCV and NumPy
import cv2 as cv
import numpy as np

# Define a blank, grayscale image
img = np.zeros( shape=(400,400,1), dtype='uint8')
print('Image shape = ', img.shape)

# Draw a rectangle
pt1 = (100,200)
pt2 = (150,300)
color = 255
thickness = -1
cv.rectangle(img, pt1, pt2, color, thickness)

# Compute moments
M = cv.moments(img)
print('Rectangle pt1: ', pt1, 'to pt2 ', pt2)
print('m00  ', M['m00'])
print('m01  ', M['m01'])
print('m10  ', M['m10'])

print('m10/m00  ', M['m10']/M['m00'])
print('m01/m00  ', M['m01']/M['m00'])

cv.imshow('Test', img)
cv.waitKey(0)

# Draw a circle
img[:] = 0
pt_center = (300, 50)
radius = 25
color = 200
thickness = 2
cv.circle(img, pt_center, radius, color, thickness)

# Compute moments
M = cv.moments(img)
print(' ')
print(' ')
print('m10/m00  ', M['m10']/M['m00'])
print('m01/m00  ', M['m01']/M['m00'])

cv.imshow('Test', img)
cv.waitKey(0)






