from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    rviz_config_path = '/home/ros/robotic_arm/src/arm_description/rviz2_config/urdf.rviz'
    return LaunchDescription([
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui"
        ),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[{'use_sim_time':False}],
            arguments=['/home/ros/robotic_arm/src/arm_description/urdf/arm_description.urdf.xacro']
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            arguments=['-d', rviz_config_path],
            output = "screen"
        )
    ])
