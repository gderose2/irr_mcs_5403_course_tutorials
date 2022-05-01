#include <ros/ros.h>

int main( int argc, char **argv )
{
  // Initialize the ROS system
  ros::init(argc, argv, "hello_ros" );

  // Establish this program as a ROS node
  ros::NodeHandle nh;

  // Send out some information
  ROS_INFO_STREAM("Hello, ROS!");
}

