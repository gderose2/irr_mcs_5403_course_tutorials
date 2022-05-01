#!/usr/bin/env python3

# Import OpenCV and NumPy
import cv2 as cv
import numpy as np

# Define a blank, color image
img = np.zeros( shape=(400,500,3), dtype='uint8')
img[:] = (127, 127, 127)
print('Image shape = ', img.shape)

# Draw a red line
pt1 = (0,100)
pt2 = (200,150)
color = (0,0,255)
thickness = 2
cv.line(img, pt1, pt2, color, thickness)

# Draw a green circle
pt_center = (300, 50)
radius = 25
color = (0,255,0)
thickness = 2
cv.circle(img, pt_center, radius, color, thickness)

# Draw some rectangles
pt1 = (100,200)
pt2 = (150,300)
color = (255,70,34)
thickness = -1
cv.rectangle(img, pt1, pt2, color, thickness)

# Rect (325,200) -> (375,300)/  img[Y-RANGE, X-RANGE]
img[200:300,325:375] = (34,70,255)

print('Pixel in second rectangle = ', img[250,325])

cv.imshow('Test', img)
cv.waitKey(0)


