#!/usr/bin/env python3

import rospy
import numpy as np
import sys
from std_msgs.msg import Float32
from std_msgs.msg import String

from dynamic_reconfigure.server import Server
from course_tutorials.cfg import PublishNodeDynCfgConfig

# PublishNode class definition
class PublishNode():
    def __init__(self):
        """Publishing node to demonstrate dynamic reconfigure"""

        # Dynamic reconfigure variables
        self.dyn_config = []
        self.dyn_reconfig_bool = 'False'
        self.dyn_reconfig_int = 0
        self.dyn_reconfig_double = 0.0
        self.dyn_reconfig_string = ''
        self.dyn_reconfig_enum = 0
        
        # ROS dynamic reconfigure server
        self.srv = Server(PublishNodeDynCfgConfig, self.dyn_reconfig_callback)
        
        # ROS Topic Publisher
        self.pub_float = rospy.Publisher('float_msg', Float32, queue_size=10)
        self.pub_str = rospy.Publisher('str_msg', String, queue_size=10)

        # Define ROS rate
        self.rate = rospy.Rate(10)

        # Start ROS loop
        while not rospy.is_shutdown():
            
            #  Call publishers
            if( self.dyn_reconfig_bool ):
                self.publish_float_message()
                self.publish_str_message()

            # Control time step
            self.rate.sleep()
            
        return

    
    ################################
    # Dynamic Reconfigure callback
    ################################
    def dyn_reconfig_callback(self, config, level):
        self.dyn_reconfig_bool = config['bool_param']
        self.dyn_reconfig_int = config['int_param']
        self.dyn_reconfig_double = config['double_param']
        self.dyn_reconfig_string = config['str_param']
        self.dyn_reconfig_enum = config['fun_type']
        return config


    ###########################
    # Publish string messsage
    ###########################
    def publish_str_message(self):

        # Define message
        msg = String()
        msg.data = self.dyn_reconfig_string

        # Publish message
        self.pub_str.publish(msg)

        return

       
    ###########################
    # Publish float messsage
    ###########################
    def publish_float_message(self):

        # Get the ROS time and get function amplitude and independent variable
        t = rospy.get_time()
        f = self.dyn_reconfig_double
        x_val = 2*np.pi*f*t
        Amp = self.dyn_reconfig_int
        
        # Compute function
        if( self.dyn_reconfig_enum == 0 ):
            val = Amp*np.sin(x_val)
        elif( self.dyn_reconfig_enum == 1 ):
            val = Amp*np.cos(x_val)
        elif( self.dyn_reconfig_enum == 2 ):
            val = Amp*np.tan(x_val)
        else:
            rospy.logerr('Invalid enumerated type')
            sys.exit(0)
            
        # Define message
        msg = Float32()
        msg.data = val

        # Publish message
        self.pub_float.publish(msg)

        return


#################    
# Main function
#################
if __name__ == '__main__':
    
    # Initialize the node and name it.
    rospy.init_node('publisher_py_node')
    rospy.loginfo('publisher_py_node running!')
    
    # Start node
    try:
        PublishNode()
    except rospy.ROSInterruptException:
        pass



    
