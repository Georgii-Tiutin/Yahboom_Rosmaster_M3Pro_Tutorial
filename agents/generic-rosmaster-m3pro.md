# ROSMASTER M3 Pro — Development Agent

This agent provides context for developing software for the Yahboom ROSMASTER M3 Pro robot platform. Load this agent first, then use the documentation references below to find detailed tutorials and code examples.

## Platform Overview

The ROSMASTER M3 Pro is an embodied intelligent robot platform for ROS2 education, research, and AI applications.

### Hardware
- **Chassis**: Mecanum wheels with pendulum suspension (omnidirectional movement)
- **Robotic arm**: 6-DOF, servo-driven
- **Depth camera**: Binocular structured light (Dabai DCW2) for visual recognition and 3D grasping
- **LiDAR**: Dual TOF LiDAR (front-left + rear-right) for 360-degree SLAM mapping and navigation
- **Audio**: Built-in microphone + speakers for voice interaction
- **Control board**: STM32-based, communicates with main controller via micro-ROS

### Supported Main Controllers
- Raspberry Pi 5
- Jetson Nano B01
- Jetson Orin Nano Super
- Jetson Orin NX Super

### Software Stack
- **OS**: Ubuntu (version depends on controller)
- **ROS**: ROS2 Humble
- **Simulation**: MoveIt2, Gazebo
- **Navigation**: Navigation2 (Nav2) with SLAM (Gmapping, Cartographer, slam_toolbox, RTAB-Map)
- **Vision**: OpenCV, Mediapipe, YOLOv8
- **AI**: Speech recognition, NLU, multimodal interaction (text/image/voice), RAG knowledge system
- **Containerization**: Docker (especially for Jetson Nano and Raspberry Pi)

### Key ROS2 Nodes and Topics
- `/YB_Node` — Main robot control node
- `geometry_msgs/msg/Twist` — Chassis velocity commands
- `std_msgs/msg/Float32MultiArray` — Sensor data (battery voltage, IMU, etc.)
- Micro-XRCE-DDS Agent bridges STM32 control board to ROS2

## Documentation Reference

All documentation is in `ROSMASTER-M3PRO-DOCS-MD/` (symlinked into project root). Each course folder contains tutorial subfolders with a `.md` file and an `images/` directory with extracted screenshots and diagrams plus `.md` sidecar files describing each image.

**To find information**: use Grep/Glob to search through `ROSMASTER-M3PRO-DOCS-MD/`. The folder structure mirrors the course curriculum below.

### Documentation Map

#### 0. Configuration and Operation Guide
Quick start, login, robotic arm calibration, Docker entry, firmware parameters, FAQ.

#### 1. AI Large Model Preparation
Prerequisites and setup for AI large model features.

#### 2. AI Large Model Basics Course
- AI model types and principles
- RAG retrieval enhancement and training samples
- Embodied intelligent robot system architecture
- Core source code walkthrough
- Configuration guide

#### 3-4. AI Large Model (Text / Voice Version)
Progressive AI integration tutorials (both text and voice variants):
semantic understanding, multimodal visual understanding, visual + robotic arm grasping, visual + SLAM navigation, combined arm + vision + navigation, intention planning with full integration.

#### 5. Chassis Control Course
ROS control, handle/keyboard control, angular/linear velocity calibration, line patrol, automatic driving.

#### 6. LiDAR Course
LiDAR introduction, dual LiDAR fusion, obstacle avoidance, tracking, guard mode, SLAM mapping (Gmapping, Cartographer, slam_toolbox, RTAB-Map), Navigation2 (single-point, multi-point, repositioning), APP mapping, machine code handling, color block transport.

#### 7. Depth Camera Course
Camera introduction, depth pseudo-color, distance measurement, volume measurement, gesture recognition, edge detection, YOLOv8 object detection, deep learning tracking.

#### 8. Mediapipe Visual Course
Hand/posture/face detection, 3D object recognition, finger control, palm target positioning, fingertip trajectory, gesture control of robotic arm, gesture grabbing/releasing.

#### 9. Robotic Arm and 3D Space Gripping Course
Arm kinematics, chassis linkage, machine code sorting (ID, height, tracking), color block sorting, shape sorting, KCF tracking, Mediapipe gesture sorting, desktop tracking, 3D tracking, line patrol with obstacle removal.

#### 10. MoveIt2 Simulation Course
MoveIt2 configuration, simulation-reality linkage, random movement, forward/inverse kinematics, Cartesian path, trajectory planning, collision detection, scene design.

#### 11. Multi-vehicle Course
Multi-vehicle chassis control, robotic arm control, navigation, formation.

#### 12. Control Board Course
STM32 development environment setup, basic routines, micro-ROS basic routines.

#### 13. Main Control Course
Platform-specific setup guides for Jetson Nano B01, Jetson Orin Nano/NX, and Raspberry Pi.

#### 14. Linux System Course
Ubuntu basics, file system, commands, editors, SSH/VNC remote control, file transfer, drivers, static IP, hotspot, capacity expansion, system backup.

#### 15. ROS2 Basic Course
Full ROS2 curriculum: nodes, topics, services, actions, custom interfaces, parameters, DDS, TF2, URDF, Gazebo, Launch files, rviz2, rqt, recording/playback.

#### 16. Docker Course
Docker overview, image/container commands, hardware interaction, data processing, robot Docker container, development environment construction.

#### 17. Image Processing Basics Course
OpenCV fundamentals: read/write/display, pixel operations, resize, crop, translate, mirror, rotate, affine/perspective transforms, grayscale, binarization, edge detection, drawing.

#### Annex
Code downloads, 3D model files, firmware/driver files.
