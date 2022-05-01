#!/usr/bin/env python3

import cv2 as cv
import numpy as np
import sys

# Thresholds
thres1 = 0
thres2 = 0
aperture = 0
aperture_list = [3,5,7]

# Canny trackbar callback
def callback(x):
    global thres1, thres2, aperture
    thres1 = cv.getTrackbarPos('thres1','controls')
    thres2 = cv.getTrackbarPos('thres2','controls')
    aperture = cv.getTrackbarPos('aperture_3_5_7','controls')
    return

# Create the a controls window
cv.namedWindow('controls',2)

# Create trackbars for canny thresholds
cv.createTrackbar('thres1','controls',    0, 255, callback)
cv.createTrackbar('thres2','controls',    0, 255, callback)
cv.createTrackbar('aperture_3_5_7','controls',  0, 2, callback)


# Read an image
img = cv.imread(sys.argv[1])

# Loop for edits
while(1):

    # Show the image
    cv.imshow('Source', img)

    # Convert to grayscale
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply Canny edge detector
    img_canny = cv.Canny(img, thres1, thres2,
                         apertureSize=aperture_list[aperture])

    # Show the Canny image
    cv.imshow('Canny', img_canny)

    # Exit on key enter
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
                
# Close all windows
cv.destroyAllWindows()




