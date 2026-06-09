# Pick-and-Place-Robot-for-surgical-tools
UR10 Robot with a vaccum gripper doing pickin and placing of surgical tools from one table to the other

Steps to run the package

1. Copy the packages into the src folder inside the workspace folder.
2. Build the workspace
3. Source it "source install/setup.bash"
4. Run the launch file by running "ros2 launch surgical_robot gazebo_launch.py"
5. Open another tab and source ros2 and repeat the step 3
6. Before running the node, please install "pip install visual-kinematics" and repeat the steps from 2-3.
7. Run the node for controlling the manipulator by running "ros2 run py_pubsub joint_cmd"

Optional

1. To visualize it in Rviz, please run "ros2 run surgical_robot display.launch.py"
