#!/usr/bin/env python3

# Import base ROS
import rospy

# Main function
if __name__ == '__main__':
    
    # Initialize the node and name it
    rospy.init_node('hello_ros_node_py')

    # Display a message
    rospy.loginfo('Hello, ROS!')

