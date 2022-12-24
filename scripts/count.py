#!/usr/bin/env python3
# This program periodically generates log messages at
# various severity levels.
# Import base ROS
import rospy

if __name__ == '__main__':
    # Initialize the node and name it
    rospy.init_node('count_and_log')

    # Set ROS rate
    rate = rospy.Rate(10)

    i = 1
    while not rospy.is_shutdown():
        rospy.logdebug('Counted to ', i )
        if( i % 2 == 0 ):
            rospy.logdebug('%d is divisible by 2.' % i)
        if( i % 3 == 0 ):
            rospy.loginfo('%d is divisible by 3.' % i)
        if( i % 5 == 0 ):
            rospy.logwarn('%d is divisible by 5.' % i)
        if( i % 10 == 0 ):
            rospy.logerr('%d is divisible by 10.' % i)
        if( i % 20 == 0 ):
            rospy.logfatal('%d is divisible by 20.' % i)

        i += 1
        rate.sleep()
