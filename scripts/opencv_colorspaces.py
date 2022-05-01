#!/usr/bin/env python3

# Import OpenCV and NumPy
import cv2 as cv
import numpy as np

# Set up files
root_dir = '../img/'
base_fname = 'FWC_example'
ext = '.jpg'

# Load example image
img = cv.imread(root_dir + base_fname + ext)
print('Input shape = ', img.shape)
cv.imshow('Source Image', img)
cv.waitKey(0)

# Resize the image
scale = 1/3
rows = int(img.shape[0] * scale )
cols = int(img.shape[1] * scale )
img = cv.resize(img, (cols, rows))
print('Resized shape = ', img.shape)
cv.imshow('Resized Image', img)
cv.imwrite(root_dir + base_fname + '_resized' + ext, img)
cv.waitKey(0)

# Convert to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', img_gray)
cv.imwrite(root_dir + base_fname + '_gray' + ext, img_gray)
cv.waitKey(0)

# Blur image
img_blur = cv.blur(img,(5,5))
cv.imshow('Average Blur Image', img_blur)
cv.imwrite(root_dir + base_fname + '_blur' + ext, img_blur)
cv.waitKey(0)

img_blur = cv.medianBlur(img,5)
cv.imshow('Median Blur Image', img_blur)
cv.imwrite(root_dir + base_fname + '_med_blur' + ext, img_blur)
cv.waitKey(0)

# Threshold
tmp,img_thres = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)
print('Threshold shape = ', img_thres.shape)
cv.imshow('Threshold Image', img_thres)
cv.imwrite(root_dir + base_fname + '_thres' + ext, img_thres)
cv.waitKey(0)


# Count non-black
nnz = cv.countNonZero(img_thres)
npixels = img_thres.shape[0]*img_thres.shape[1]
print('Threshold NNZ = ', nnz)
print('NNZ Percent = %.2f%%' % (100*nnz/npixels))

