#!/usr/bin/env python3

# Import OpenCV and NumPy
import cv2 as cv
import numpy as np

# Define a blank, grayscale image
img = np.zeros( shape=(400,500,1), dtype='uint8')
img[:] = 127
print('Image shape = ', img.shape)

# Draw a line
pt1 = (0,100)
pt2 = (200,150)
color = 255
thickness = 2
cv.line(img, pt1, pt2, color, thickness)

# Draw a circle
pt_center = (300, 50)
radius = 25
color = 200
thickness = 2
cv.circle(img, pt_center, radius, color, thickness)

# Draw some rectangles
pt1 = (100,200)
pt2 = (150,300)
color = 50
thickness = -1
cv.rectangle(img, pt1, pt2, color, thickness)

# Rect (325,200) -> (375,300)/  img[Y-RANGE, X-RANGE]
img[200:300,325:375] = 255

print('Pixel in white rectangle = ', img[250,325])

cv.imshow('Test', img)
cv.waitKey(0)


