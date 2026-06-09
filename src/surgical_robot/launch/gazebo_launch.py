from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_path = get_package_share_directory("surgical_robot")

    urdf_file = os.path.join(pkg_path, "urdf", "surgical_robot.urdf.xacro")
    controller_yaml = os.path.join(pkg_path, "config", "control.yaml")

    ld = LaunchDescription()

    ld.add_action(DeclareLaunchArgument("use_sim_time", default_value="true"))

    # Robot State Publisher
    robot_state_pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            "use_sim_time": LaunchConfiguration("use_sim_time"),
            "robot_description": Command(["xacro ", urdf_file]),
        }],
        output="screen"
    )

    # ros2_control node
    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[{
            "use_sim_time": LaunchConfiguration("use_sim_time")
        }, controller_yaml],
        output="screen"
    )

    # Spawners
    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen"
    )

    robot_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller"],  # Replace if your controller name differs
        output="screen"
    )

    ld.add_action(robot_state_pub)
    ld.add_action(control_node)
    ld.add_action(TimerAction(period=2.0, actions=[joint_state_broadcaster]))
    ld.add_action(TimerAction(period=4.0, actions=[robot_controller]))

    return ld
