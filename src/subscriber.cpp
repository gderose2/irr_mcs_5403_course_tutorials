// Include ROS base
#include <ros/ros.h>

// Include ROS messsage information
#include <std_msgs/Int32.h>



/******************************************************************************
*
* SubscribeNode class definition
*
******************************************************************************/
class SubscribeNode
{
public:
  SubscribeNode();
  ~SubscribeNode();

private:
  // Node Handler
  ros::NodeHandle nh_;

  // ROS Topic Subscribers
  ros::Subscriber sub_int_;

  // Supporting Function Prototypes
  void int_message_callback(const std_msgs::Int32::ConstPtr &msg);
};
// End of class SubscribeNode



/******************************************************************************
*
* SubscribeNode constructor
*
******************************************************************************/
SubscribeNode::SubscribeNode()
{
  
  // Define subscriber
  sub_int_ = nh_.subscribe("int_msg", 10,
			   &SubscribeNode::int_message_callback, this);
  
}
// End of SubscribeNode



/******************************************************************************
*
* SubscribeNode destructor
*
******************************************************************************/
SubscribeNode::~SubscribeNode()
{
  return;
}
// End of ~SubscribeNode



/******************************************************************************
*
* Support functions
*
******************************************************************************/

///////////////////////////////////////////////////////////////////////
// int_message_callback: Function to display integer message received
///////////////////////////////////////////////////////////////////////
void SubscribeNode::int_message_callback(const std_msgs::Int32::ConstPtr &msg)
{
  ROS_INFO("Received int = %d", msg->data);
  //sleep(3);
  return;
}
// End of int_message_callback



/******************************************************************************
*
* Main function
*
******************************************************************************/
int main(int argc, char** argv)
{
  // Initialize the ROS system
  ros::init(argc, argv, "subscriber");

  // Report out node contstruction
  ROS_INFO_STREAM("Subscriber node running!");

  // Create a SubscribeNode object
  SubscribeNode sub_node_obj;
  
  // Enter ROS loop
  ros::spin();
  return 0;
}
// End of main

