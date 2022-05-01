// Include ROS base
#include <ros/ros.h>

// Include ROS messsage information
#include <std_msgs/Int32.h>



/******************************************************************************
*
* PublishNode class definition
*
******************************************************************************/
class PublishNode
{
public:
  PublishNode();
  ~PublishNode();

private:
  // Node Handler
  ros::NodeHandle nh_;

  // Counter
  int counter_ = 0;

  // ROS Topic Publishers
  ros::Publisher pub_int_;

  // Supporting Function Prototypes
  void publish_int_message(void);
};
// End of class PublishNode



/******************************************************************************
*
* PublishNode constructor
*
******************************************************************************/
PublishNode::PublishNode()
{
  
  // Define publisher
  pub_int_ = nh_.advertise<std_msgs::Int32>("int_msg", 10);
  
  // Set ROS rate
  ros::Rate rate(1);
   
  // Start ROS loop
  while(ros::ok()) {
    
    // Call publisher
    publish_int_message();
    
    // Control time step
    rate.sleep();
  }
  
}
// End of PublishNode



/******************************************************************************
*
* PublishNode destructor
*
******************************************************************************/
PublishNode::~PublishNode()
{
  return;
}
// End of ~PublishNode



/******************************************************************************
*
* Support functions
*
******************************************************************************/

////////////////////////////////////////////////////////////////
// publish_int_message: Fucntion to publish an integer message
////////////////////////////////////////////////////////////////
void PublishNode::publish_int_message()
{

  // Define messages
  std_msgs::Int32 msg;
  msg.data = counter_;
    
  // Publish message up to counter of 100
  if( counter_ < 100 )
    {
      pub_int_.publish(msg);
      ROS_INFO("Published int = %d", msg.data);
    }

  // Increment integer counter
  counter_++;

}
// End of publish_int_message



/******************************************************************************
*
* Main function
*
******************************************************************************/
int main(int argc, char** argv)
{
  // Initialize the ROS system
  ros::init(argc, argv, "publisher");

  // Report out node contstruction
  ROS_INFO_STREAM("Publisher node running!");

  // Create a PublishNode object
  PublishNode pub_node_obj;
  
  return 0;
}
// End of main

