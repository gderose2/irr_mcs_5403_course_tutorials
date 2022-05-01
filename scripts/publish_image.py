#!/usr/bin/env python3
import rospy
import cv2 as cv
import numpy as np
import sys

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# PubImage class
class PubImage():
    def __init__(self, fname):
        """Publish and image provided by the user"""

        # Initialization
        self.img_rate = 5   # Hz

        # Define detection publishers
        self.pub_image = rospy.Publisher('/cam_pub/image_raw', Image,
                                         queue_size=1)
        
        # Set parameters
        br = CvBridge()

        # Define ROS rate
        self.rate = rospy.Rate(self.img_rate)

        # Read in the image
        img = cv.imread(fname)
        if( img is None ):
            rospy.logerr('Image not found: %s ' % fname)
            sys.exit(0)
            
        # Loop and publish commands to vehicle
        while not rospy.is_shutdown():

            # Publish image
            self.pub_image.publish(br.cv2_to_imgmsg(img, "bgr8"))

            # Sleep for time step
            self.rate.sleep()
            
        return
    

#################    
# Main function
#################
if __name__ == '__main__':

    # Check inputs
    if( len(sys.argv) < 2 ):
        print('ERROR: Image filename required')
        sys.exit(0)
        
    # Initialize the node and name it
    rospy.init_node('publish_image_node')
    print("Publish image initialized")

    # Start tester
    try:
        PubImage(sys.argv[1])
    except rospy.ROSInterruptException:
        pass
