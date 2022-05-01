cmake_minimum_required(VERSION 3.0.2)
project(course_tutorials)
add_compile_options(-std=c++11)

# Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  dynamic_reconfigure
)

# Declare ROS dynamic reconfigure parameters
generate_dynamic_reconfigure_options(
  cfg/PublishNodeDynCfg.cfg
  cfg/HSVImageProcessDynCfg.cfg
)

# Define the catkin_package
catkin_package()

# Specify additional locations of header files
include_directories( include  ${catkin_INCLUDE_DIRS} )

##
## For each node define an executable and link to libraries
##
add_executable(hello src/hello.cpp)
target_link_libraries(hello ${catkin_LIBRARIES})

add_executable(publisher src/publisher.cpp)
target_link_libraries(publisher ${catkin_LIBRARIES})

add_executable(subscriber src/subscriber.cpp)
target_link_libraries(subscriber ${catkin_LIBRARIES})

add_executable(count src/count.cpp)
target_link_libraries(count ${catkin_LIBRARIES})

add_executable(set_bg_color src/set_bg_color.cpp)
target_link_libraries(set_bg_color ${catkin_LIBRARIES})


