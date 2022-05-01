#!/usr/bin/env python3

# Import base ROS
import rospy

# Import ROS message information
from std_msgs.msg import Int32

################################
# PublishNode class definition
################################
class PublishNode():
    def __init__(self):
        """Example publisher node"""

        # Variables
        self.counter = 0
               
        # Define publishers
        self.pub_int = rospy.Publisher('int_msg', Int32, queue_size=10)

        # Define subscribers

        # Set ROS rate
        self.rate = rospy.Rate(1)

        # Start ROS loop
        while not rospy.is_shutdown():

            # Call publisher
            self.publish_int_message()

            # Control time step
            self.rate.sleep()
            
        return

    ###############################################################
    # publish_int_message: Function to publish an integer message
    ###############################################################
    def publish_int_message(self):

        # Define message
        msg = Int32()
        msg.data = self.counter

        # Publish messge up to coutner of 100
        if( self.counter < 100 ):
            self.pub_int.publish(msg)
            rospy.loginfo('Published int = %d' % msg.data)

        # Increment integer counter
        self.counter += 1


#################    
# Main function
#################
if __name__ == '__main__':
    
    # Initialize the node and name it
    rospy.init_node('publisher_node')
    print("Publisher node initialized")
    
    # Start node
    try:
        PublishNode()
    except rospy.ROSInterruptException:
        pass
