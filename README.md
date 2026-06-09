# Pick-and-Place-Robot-for-surgical-tools
# UR10 Robot with Vacuum Gripper – Pick and Place System

A UR10 robot equipped with a vacuum gripper performing pick-and-place operations of surgical tools from one table to another.

---

## Steps to Run the Package

1. Copy the packages into the `src` folder inside your ROS2 workspace.

2. Build the workspace:
```bash
colcon build
```

3. Source the workspace:
```bash
source install/setup.bash
```

4.Launch the simulation:
```bash
ros2 launch surgical_robot gazebo_launch.py
```

5.Open another terminal, source ROS2 and the workspace again:
```bash
source install/setup.bash
```
6.Install required dependency:
```bash
pip install visual-kinematics
```
Then rebuild and source again:
```bash
colcon build
source install/setup.bash
```
7. Run the manipulator control node:
```bash
ros2 run py_pubsub joint_cmd
```
# Optional
To visualize in RViz:
```bash
ros2 run surgical_robot display.launch.py
```
# Additional Resources
[Report](https://drive.google.com/file/d/11qMs1MFtcZWggzyGDeeada7Y0V4CAbhn/view?usp=sharing)

[Video](https://drive.google.com/file/d/1SveHbut_GvEvQvpZNzMg7xvElcUgWDXQ/view?usp=sharing)
