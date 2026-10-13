---
name: generic-rosmaster-m3pro
description: General-purpose development agent for the Yahboom ROSMASTER M3 Pro robot platform; provides hardware/software context and routes to the detailed ROSMASTER-M3PRO-DOCS-MD tutorials (courses 00–23)
tools: ["Read", "Bash", "Glob", "Grep"]
model: opus
---

# ROSMASTER M3 Pro — Development Agent

This agent provides context for developing software for the Yahboom ROSMASTER M3 Pro robot platform. Load this agent first, then use the documentation references below to find detailed tutorials and code examples.

## Platform Overview

The ROSMASTER M3 Pro is an embodied intelligent robot platform for ROS2 education, research, and AI applications.

### Hardware
- **Chassis**: Mecanum wheels with pendulum suspension (omnidirectional movement)
- **Robotic arm**: 6-DOF, bus-servo driven (the control board also drives PWM servos)
- **Depth camera**: Orbbec DaBai DCW2 (binocular structured light) for visual recognition, distance measurement and 3D grasping
- **LiDAR**: Dual T-MiniPlus TOF LiDARs (front-left + rear-right), fused into one 360-degree scan
- **Audio**: Built-in microphone + speakers for voice interaction
- **Control board**: STM32-based, runs micro-ROS firmware and talks to the main controller over serial (`/dev/myserial`, 2,000,000 baud)

### Supported Main Controllers
- **Jetson Orin NX Super / Orin Nano Super**: Ubuntu 22.04, code runs directly on the host (`/home/jetson`)
- **Jetson Nano B01** and **Raspberry Pi 5**: the ROS2 environment runs **inside a Docker container**. Enter the container before running any `ros2` command (see `00.Configuration and Operation Guide/4.Enter_the_Docker…` and `19.Docker Course/5.Enter_the_bot's_docker_container`).

### Software Stack
- **ROS**: ROS2 Humble
- **Workspaces**: `~/M3Pro_ws` (robot packages), `~/uros_ws` (micro-ROS agent), `~/yahboomcar_ws` (arm kinematics, e.g. `src/arm_kin/param/offset_value.yaml`), `~/yahboomcar_ros2_ws`. Inside the Docker container (Jetson Nano / Raspberry Pi 5) the home directory is `/root`.
- **Simulation**: MoveIt2, Gazebo
- **Navigation**: Navigation2 (Nav2) with SLAM (Gmapping, Cartographer, slam_toolbox, RTAB-Map), road network planning, visual relocalization
- **Vision**: OpenCV, Mediapipe, YOLOv8, Transformer-based tracking
- **AI**: Large-model voice/text interaction, multimodal visual understanding, intention estimation, RAG knowledge base, Dify apps and agent workflows (Dify reached via `DIFY_BASE_URL`, e.g. `http://localhost/v1`)
- **OpenClaw**: AI agent platform that controls the robot through an MCP service (`FastMCP` "ROS-MCP-Service", tools such as `MoveWithSpeed`, `Pick`, `Place`, `SeeWhat`, `Navigation`, `TTS`). Chat via WebChat, TUI, voice or WhatsApp; managed with `openclaw` CLI (`openclaw gateway restart`, `openclaw models status`, `openclaw tui`).

### ROS2 Basics on the Robot
- **ROS_DOMAIN_ID**: set in the control board firmware (`robot.set_ros_domain_id(...)`, factory value 30) and must match `export ROS_DOMAIN_ID=...` in `~/.bashrc`, or topics from the STM32 will not appear. Each robot on a shared LAN needs its own ID.
- **Typical startup** (one terminal each):
  ```bash
  sh start_agent.sh                                  # micro-ROS agent for the STM32 board
  ros2 launch m3pro_bringup car_base.launch.py        # odometry, TF, arm helpers, camera
  ros2 launch m3pro_bringup mcp_service.launch.py     # MCP service for OpenClaw
  ros2 run multi_brains_pre openclaw_bridge           # only if OpenClaw should reply by voice
  ```
  Navigation tutorials use `ros2 launch M3Pro_navigation base_bringup.launch.py` instead; the camera alone is `ros2 launch orbbec_camera dabai_dcw2.launch.py`.
- **Key topics**:
  - `/cmd_vel` (`geometry_msgs/msg/Twist`): chassis velocity commands
  - `/scan0`, `/scan1` (each LiDAR) and `/scan` (fused), all `sensor_msgs/msg/LaserScan`
  - `/odom`, `/odom_raw`: odometry
  - `/imu/data`, `/imu/data_raw`, `/imu/mag`: IMU
  - `/arm6_joints` (`arm_msgs/msg/ArmJoints`): set all six arm servos, e.g. `ros2 topic pub /arm6_joints arm_msgs/msg/ArmJoints "{joint1: 90, joint2: 90, ...}"`
  - `/beep`: buzzer

## Documentation Reference

All documentation is in `ROSMASTER-M3PRO-DOCS-MD/` (symlinked into project root). Each course folder contains tutorial subfolders with a `.md` file and an `images/` directory with extracted screenshots and diagrams plus `.md` sidecar files describing each image.

**To find information**: use Grep/Glob to search through `ROSMASTER-M3PRO-DOCS-MD/`. The folder structure mirrors the course curriculum below.

### Documentation Map

Course folders are numbered `00`–`23` (upstream version of 2026-08-11). Do not use `archive/` in the robotdoc repo: it holds obsolete tutorials from the previous version (old numbering `0`–`17`) and is only for history questions.

#### 00. Configuration and Operation Guide
Quick start with the handle, login and viewing the code, robotic arm calibration, DIY arm precautions, Docker entry (Jetson Nano / Raspberry Pi 5), control board firmware parameters, FAQ.

#### 01. Chassis Control Course
ROS control, handle/keyboard control, angular/linear velocity calibration, line patrol automatic driving, patrol.

#### 02. LiDAR Course
LiDAR introduction, dual LiDAR fusion, obstacle avoidance, tracking, guard mode, SLAM mapping (Gmapping, Cartographer, slam_toolbox, RTAB-Map), Navigation2 (single-point, multi-point, repositioning), RTAB-Map navigation, APP mapping, machine code handling, color block transport, navigation via pose-constrained visual relocalization.

#### 03. Depth Camera Course
Dabai DCW2 introduction, depth pseudo-color, distance measurement, wood block volume measurement, Mediapipe gesture recognition, edge detection, YOLOv8 object detection, deep learning tracking, Transformer model tracking.

#### 04. Robotic Arm and 3D Space Gripping Course
Arm kinematics, chassis linkage, machine code sorting (ID, height, tracking), color block sorting, wood block shape sorting, KCF tracking, Mediapipe gesture sorting, desktop tracking, 3D tracking, line patrol with obstacle removal.

#### 05. Road Network Planning and Navigation
Road network planning introduction, building a pose map, road network annotation, waypoint planning and navigation, road network navigation from any pose, path re-planning.

#### 06. OpenClaw Basic Course
OpenClaw introduction and core concepts, API-KEY configuration, switching models, system prompt words, common CLI commands.

#### 07. OpenClaw Interaction Method
Web chat, TUI, voice dialogue and WhatsApp interaction; common errors and solutions.

#### 08. OpenClaw Development
Connecting OpenClaw to the robot's MCP interface (with MCP function summary), robot CLI command tool (with command summary), robot control and reply bridge plugins, multimodal vision, chassis and robotic arm control, skills development, timed tasks, multi-agent, active interaction, vector memory; common errors.

#### 09. OpenClaw Embodied Intelligent Application
Target tracking, arm tracking and grasping, fixed-point placement, garbage sorting, SLAM mapping and navigation, navigation transfer, machine code clip, color line patrol, visual distance measurement; common errors.

#### 10. OpenClaw Scenario Sandbox
Map description and prop placement, building the sand table map, visual relocation markers, map mapping markers, comprehensive sandbox case.

#### 11. AI Model Basics
AI large model types and principles, RAG retrieval enhancement and training samples, embodied intelligent robot system architecture, core source code of embodied functions.

#### 12. AI Model Development
Model provider account registration, API-KEY configuration, Dify introduction and basics, chatbot development, RAG knowledge base deployment and chatbot, AI agent workflow (example `.yml` apps included), custom wake-up response, core module testing tools.

#### 13–14. AI Model (Voice / Text Version)
Semantic understanding and command following, multimodal visual understanding, visual understanding + SLAM navigation, intention estimation (with `Intent mapping.xlsx` example). The voice version also covers arm gripping + visual understanding + SLAM navigation.

#### 15. Mediapipe Visual Course
Hand/posture/overall/face detection, facial landmarks, face effects, 3D object recognition, brush, finger control, palm target positioning, fingertip trajectory, gesture control of the robotic arm, gesture grabbing/releasing, gesture action groups.

#### 16. MoveIt2 Simulation Course
MoveIt2 configuration, simulation-reality linkage, random movement, forward/inverse kinematics, Cartesian path, trajectory planning, collision detection, scene design.

#### 17. Multi-vehicle Course
Multi-vehicle chassis control, robotic arm control, navigation, formation.

#### 18. Control Board Course
STM32 development environment setup (STM32CubeIDE, SWD/serial flashing, micro-ROS driver library and agent), basic routines (LED, buttons, buzzer, serial, battery, PWM servo, motors, encoders, PID, kinematics, IMU, LiDAR, flash, OLED, RGB strip, SBUS, USB controller, CAN), micro-ROS routines (publish/subscribe topics, buzzer, bus servo, speed, IMU, radar).

#### 19. Docker Course
Docker overview, image/container commands, publishing images, hardware interaction, entering the robot's container, development environment in Docker.

#### 20. Image Processing Basics Course
OpenCV fundamentals: read/write/display, image quality, pixel operations, zoom, cut, translate, mirror, affine transform, rotation, grayscale, binarization, edge detection, drawing.

#### 21. Main Control Course
Platform-specific setup for Jetson Nano B01, Jetson Orin Nano/NX and Raspberry Pi 5: system images, backup, storage expansion, swap, network, SSH/VNC, file transfer, Jtop, and Raspberry Pi display, audio/video, cameras and temperature.

#### 22. Linux System Course
Linux introduction, Ubuntu file system, commands, editors, software management, virtual machine, SSH/VNC, file transfer, drivers, static IP and hotspot, device ID binding, capacity expansion, passwordless sudo.

#### 23. ROS2 Basic Course
Full ROS2 curriculum: install Humble, workspace, packages, nodes, topics, services, actions, custom interfaces, parameters, meta-packages, distributed communication, DDS, time API, command tools, rviz2, rqt, launch files, recording/playback, URDF, Gazebo, TF2.

#### Annex
Code downloads, 3D model files, firmware/driver files.
