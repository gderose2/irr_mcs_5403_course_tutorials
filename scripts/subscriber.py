#!/usr/bin/env python3

# Import base ROS
import rospy

# Import ROS message information
from std_msgs.msg import Int32


################################
# SubscribeNode class definition
################################
class SubscribeNode():
    def __init__(self):
        """Example subscriber node"""

        # Define publishers

        # Define subscribers
        self.sub_int = rospy.Subscriber('int_msg', Int32,
                                        self.int_message_callback,queue_size=10)

        # Enter ROS loop
        rospy.spin()
        
        return

    ################################################################
    # int_message_callback: Function to process an integer message
    ################################################################
    def int_message_callback(self, msg):

        rospy.loginfo('Received int = %d' % msg.data)


#################    
# Main function
#################
if __name__ == '__main__':
    
    # Initialize the node and name it.
    rospy.init_node('subscriber_node')
    print("Subscriber node initialized")
    
    # Start node
    try:
        SubscribeNode()
    except rospy.ROSInterruptException:
        pass
