import cv2 as cv
import numpy as np
import sys

# Color ranges
H_low = 0
H_high = 179
S_low= 0
S_high = 255
V_low= 0
V_high = 255

# Trackbar callback fucntion to update HSV value
def callback(x):
    global H_low, H_high, S_low, S_high, V_low, V_high
    H_low = cv.getTrackbarPos('low H','controls')
    H_high = cv.getTrackbarPos('high H','controls')
    S_low = cv.getTrackbarPos('low S','controls')
    S_high = cv.getTrackbarPos('high S','controls')
    V_low = cv.getTrackbarPos('low V','controls')
    V_high = cv.getTrackbarPos('high V','controls')
    return


# Create the a controls window
cv.namedWindow('controls',2)

# Create trackbars for Low and High B, G, R
cv.createTrackbar('low H','controls',    0, 179, callback)
cv.createTrackbar('high H','controls', 179, 179, callback)
cv.createTrackbar('low S','controls',    0, 255, callback)
cv.createTrackbar('high S','controls', 255, 255, callback)
cv.createTrackbar('low V','controls',    0, 255, callback)
cv.createTrackbar('high V','controls', 255, 255, callback)

# Read the image
img_orig = cv.imread(sys.argv[1])

# Loop for edits
while(1):

    # Conver to HSV
    img_hsv = cv.cvtColor(img_orig, cv.COLOR_BGR2HSV)
    
    # Set up bounds
    hsv_low = np.array([H_low, S_low, V_low], np.uint8)
    hsv_high = np.array([H_high, S_high, V_high], np.uint8)

    # Get filter image
    mask = cv.inRange(img_hsv, hsv_low, hsv_high)
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

