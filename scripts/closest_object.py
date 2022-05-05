#!/usr/bin/env python3

import rospy
import numpy as np

from sensor_msgs.msg import LaserScan

ACTIVE_WINDOWS = []

# ClosestObject class
class ClosestObject():
    def __init__(self):
        """Use lidar sensor to detect the closest object"""

        # Define subscriber
        self.sub_lidar = rospy.Subscriber('scan', LaserScan,
                                          self.lidar_callback)

        # ROS spin
        rospy.spin()
        
        return

    
    ##################
    # Lidar callback
    ##################
    def lidar_callback(self, data):

        min_idx = None
        min_dist = data.range_max
        for idx in range(len(data.ranges)):
            if(data.ranges[idx] > data.range_min and
               data.ranges[idx] < min_dist):
                min_idx = idx
                min_dist = data.ranges[idx]


        if( min_idx is not None ):
            rospy.loginfo('Closest Obj at %.2f deg and dist = %.3f' % (
                min_idx*data.angle_increment*180/np.pi, min_dist ))

        return


#################    
# Main function
#################
if __name__ == '__main__':
    
    # Initialize the node and name it
    rospy.init_node('closest_object_node')
    print("closest object node initialized")
    
    # Start node
    try:
        ClosestObject()
    except rospy.ROSInterruptException:
        pass



    
