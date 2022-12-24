#!/usr/bin/env python3
# This program waits for a turtlesim to start up, and
# changes its background color.
import rospy

# Import ROS message information
from std_srvs.srv import Empty

if __name__ == '__main__':
    # Initialize the node and name it
    rospy.init_node('set_bg_color')

    # Wait until the clear service is available, which
    # indicates that turtlesim has started up, and has
    # set the background color parameters.
    rospy.wait_for_service('/clear')
    
    # Set the background color for turtlesim,
    # overriding the default blue color.
    rospy.set_param('background_r', 255)
    rospy.set_param('background_g', 255)
    rospy.set_param('background_b', 0)

    # Get turtlesim to pick up the new parameter values.
    clearClient = rospy.ServiceProxy('/clear', Empty)
    clearClient.call()

