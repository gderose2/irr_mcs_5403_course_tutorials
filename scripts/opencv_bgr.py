import cv2 as cv
import numpy as np
import sys

# Color ranges
B_low = 0
B_high = 255
G_low= 0
G_high = 255
R_low= 0
R_high = 255

# Trackbar callback fucntion to update BGR value
def callback(x):
    global R_low, B_high, G_low, G_high, R_low, R_high
    B_low = cv.getTrackbarPos('low B','controls')
    B_high = cv.getTrackbarPos('high B','controls')
    G_low = cv.getTrackbarPos('low G','controls')
    G_high = cv.getTrackbarPos('high G','controls')
    R_low = cv.getTrackbarPos('low R','controls')
    R_high = cv.getTrackbarPos('high R','controls')
    return


# Create the a controls window
cv.namedWindow('controls',2)

# Create trackbars for Low and High B, G, R
cv.createTrackbar('low B','controls',    0, 255, callback)
cv.createTrackbar('high B','controls', 255, 255, callback)
cv.createTrackbar('low G','controls',    0, 255, callback)
cv.createTrackbar('high G','controls', 255, 255, callback)
cv.createTrackbar('low R','controls',    0, 255, callback)
cv.createTrackbar('high R','controls', 255, 255, callback)

# Read the image
img_orig = cv.imread(sys.argv[1])

# Loop for edits
while(1):
       
    # Set up bounds
    bgr_low = np.array([B_low, G_low, R_low], np.uint8)
    bgr_high = np.array([B_high, G_high, R_high], np.uint8)

    # Get filter image
    mask = cv.inRange(img_orig, bgr_low, bgr_high)
    res = cv.bitwise_and(img_orig, img_orig, mask=mask)

    # Show images
    cv.imshow('Mask',mask)
    cv.imshow('Result',res)

    # Exit on key enter
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
                
# Close all windows
cv.destroyAllWindows()

