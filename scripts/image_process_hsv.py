#!/usr/bin/env python3

# Import base ROS
import rospy

# Import OpenCV and NumPy
import cv2 as cv
import numpy as np

# Import ROS message information
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from dynamic_reconfigure.server import Server
from course_tutorials.cfg import HSVImageProcessDynCfgConfig

ACTIVE_WINDOWS = []

#####################################
# ImageProcessNode class definition
#####################################
class ImageProcessNode():
    def __init__(self):
        """Node to facilitate HSV image proessing"""

        # Initialize dynamic configure parameters
        self.h_low = 0
        self.h_high = 179
        self.s_low = 0
        self.s_high = 255
        self.v_low = 0
        self.v_high = 255

        # Define subscribers
        self.image_sub = rospy.Subscriber('/cam_pub/image_raw', Image,
                                          self.camera_callback)

        # Set up dynamic reconfigure
        self.srv = Server(HSVImageProcessDynCfgConfig,
                          self.dyn_reconfig_callback)

        # Define ROS rate
        self.rate = rospy.Rate(20)
        
        # Enter ROS loop
        rospy.spin()
        
        return

    
    ################################
    # Dynamic Reconfigure callback
    ################################
    def dyn_reconfig_callback(self, config, level):
        self.h_low = config['hue_low']
        self.h_high = config['hue_high']
        self.s_low = config['sat_low']
        self.s_high = config['sat_high']
        self.v_low = config['val_low']
        self.v_high = config['val_high']
        return config
    

    #########################
    # Camera image callback
    #########################
    def camera_callback(self, msg):

        # Get the camera image and make a copy
        img = CvBridge().imgmsg_to_cv2(msg, "bgr8" )

        # Convert to HSV color space
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        # Set up bounds
        hsv_low =  np.array([self.h_low, self.s_low, self.v_low], np.uint8)
        hsv_high = np.array([self.h_high, self.s_high, self.v_high], np.uint8)

        # Apply mask 
        mask = cv.inRange(img_hsv, hsv_low, hsv_high)
        res = cv.bitwise_and(img, img, mask=mask)

        # Show images
        self.display_image('Mask', mask, True)
        self.display_image('Result', res, True)
        return


    ####################
    # Display an image
    ####################
    def display_image(self, title_str, img, disp_flag ):

        if( disp_flag ):
            # Display the given image
            cv.namedWindow(title_str, cv.WINDOW_NORMAL)
            cv.imshow(title_str, img)
            cv.waitKey(3)

            # Add window to active window list
            if not ( title_str in ACTIVE_WINDOWS ):
                ACTIVE_WINDOWS.append(title_str)
        else:
            if( title_str in ACTIVE_WINDOWS):
                cv.destroyWindow(title_str)
                ACTIVE_WINDOWS.remove(title_str)
        return
    


#################    
# Main function
#################
if __name__ == '__main__':
    
    # Initialize the node and name it.
    rospy.init_node('image_process_node')
    print("Image Process node initialized")
    
    # Start node
    try:
        ImageProcessNode()
    except rospy.ROSInterruptException:
        pass
