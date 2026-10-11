# HARDWARE.md — ROSMASTER M3 Pro (this unit)

Hardware inventory and assumptions for the cuboid collect-and-sort project.

**All facts below were captured live from the robot over SSH on 2026-08-26**
unless marked **[unverified]**. This revision supersedes the 2026-04-08 version
that lived in `Computer_vision/`; five errors from that version are corrected
here and listed in the change log at the bottom.

Rule for this file: anything not verified against the machine or the manual is
marked **[unverified]** and must not be relied on.

## Robot

- **Platform:** Yahboom ROSMASTER M3 Pro (`ROBOT_TYPE=ROSMASTER-M3Pro`)
- **Hostname:** `yahboom`
- **SSH:** `ssh jetson@<robot-ip>` (home Wi-Fi; key-based login),
  fallback `jetson@192.168.8.88` (ROSMASTER AP) **[unverified]** — the AP
  fallback has not been retested on this revision.

## Compute

- **Main controller:** NVIDIA Jetson **Orin NX** Engineering Reference
  Developer Kit Super (`/proc/device-tree/model`; `MACHINE=OrinNx`)
- **Memory:** 7.4 GiB visible → Orin NX 8 GB SKU
- **Storage:** 1 TB NVMe (`/dev/nvme0n1p1`, 915 G, 81 G used)
- **OS:** Ubuntu 22.04.5 LTS (jammy), aarch64
- **L4T:** R36.4.7 (JetPack 6.x), kernel 5.15.148-tegra
- **ROS 2 distro:** Humble Hawksbill (`/opt/ros/humble`)
- **Docker:** installed and running (`docker0`, two `br-*` bridges). All
  containers present are exited Dify / LLM images — **nothing robot-related
  runs in Docker on this unit.** Orin boards do not use the Yahboom Docker
  workflow; that is a Raspberry Pi 5 / Jetson Nano thing (course 0 §4).

## How the robot is actually driven — read this first

There is **one** serial link to the low-level board, and everything physical
goes through it:

```
/dev/ttyUSB0  ==  /dev/myserial  ==  CP210x (10c4:ea60)  ==  STM32 control board
```

The udev rule (`/etc/udev/rules.d/usb_serial.rules`) creates the `myserial`
symlink from that USB ID. `~/start_agent.sh` runs the micro-ROS agent on it at
2 000 000 baud, which brings up the ROS node `/YB_Node`.

`/YB_Node` is the STM32 firmware exposed to ROS 2. It is chassis, arm, IMU,
battery, buzzer, LED **and both LiDARs**:

| Direction | Topic | Type |
|---|---|---|
| sub | `/cmd_vel` | `geometry_msgs/msg/Twist` |
| sub | `/arm6_joints` | `arm_msgs/msg/ArmJoints` (all six servos at once) |
| sub | `/arm_joint` | `arm_msgs/msg/ArmJoint` (one servo) |
| sub | `/beep`, `/rgb` | `std_msgs/msg/…` (`/rgb` is the LED strip, **not** a camera) |
| pub | `/battery` | `std_msgs/msg/Float32` |
| pub | `/imu/data_raw` | `sensor_msgs/msg/Imu` |
| pub | `/odom_raw` | `nav_msgs/msg/Odometry` |
| pub | `/scan0`, `/scan1` | `sensor_msgs/msg/LaserScan` |

**Consequence:** only one process may hold `/dev/myserial` at a time. The
micro-ROS agent owns it whenever it is running. This is exactly why course 0
tells you to kill the agent before running `calibrate_arm.py` or
`config_robot.py` — those talk to the same port with a different protocol.

## Arm

- **DOF:** **5 DOF arm + 1 DOF parallel gripper = 6 servos total.**
  URDF has 5 revolute joints `arm1_Joint`..`arm5_Joint`, each limited to
  ±1.5708 rad (±90°), plus `rlink1_Joint` (gripper, −0.95..0) and the
  `llink*`/`rlink*` continuous linkage joints.
  `ArmJoints.msg` is `int16 joint1..joint6 + int16 time`; **`joint6` is the
  gripper.**
- **Kinematic consequence:** 5 DOF cannot reach arbitrary 6D end-effector
  poses. Grasp planning must constrain to vertical-approach grasps aligned
  with the cuboid's top face.
- **Control path:** publish `arm_msgs/msg/ArmJoints` on `/arm6_joints`
  (or `ArmJoint` on `/arm_joint` for a single servo). `/YB_Node` actuates.
- **There is no separate arm driver node.** `~/yahboomcar_ws/src/arm_driver/`
  exists in source but is **not built** (absent from `install/`), imports
  `dofbot_pro_interface`, and subscribes to `TargetAngle` — it is leftover
  code from a different Yahboom product (DOFBOT Pro). Ignore it. It has
  never run on this robot.
- **Description:** `~/yahboomcar_ws/src/yahboom_M3Pro_description/urdf/M3Pro.urdf`
  (see "Two URDFs" below)
- **Kinematics:** custom `arm_kin` package, `~/libarmkin.so`, `kin_srv`
  service node; calibration offsets in `yahboomcar_ws/src/arm_kin/param/offset_value.yaml`
- **Gripper:** 2-finger parallel jaw (URDF links `llink1/2`, `rlink1/2`,
  with `llink3`/`rlink3` as auxiliary linkages)
- **TCP / end-effector frame:** URDF link `Gripping`, fixed child of `arm5`.
  There is no literal `end_effector` frame.
- **Per-joint feedback: NONE.** `/YB_Node` publishes only `/battery`,
  `/imu/data_raw`, `/odom_raw`, `/scan0`, `/scan1` — there is no arm state
  topic at all. **Grasp confirmation cannot use servo effort or current.**
  Use vision, or commanded-vs-expected gripper closure, instead.
- **Max reach / payload / gripper opening width:** **[unverified]** — not in
  URDF or config. Pull from the Yahboom M3 Pro datasheet or measure.
  Placeholder only: ~25–30 cm reach, ~200 g payload, ~3–4 cm opening.
- **URDF quirk:** joint `arm4_Joiint` (double `i`) is a typo propagated
  through the MoveIt config. Not fixed — changing it would break the SRDF.
  Code referencing this joint by name must use the typo spelling.

## Perception

- **Primary (only) camera:** Orbbec DaBai DCW2 (RGB-D), `CAMERA_TYPE=dabai_dcw2`
  - RGB USB ID `2bc5:0561`, depth sensor USB ID `2bc5:06a0`
  - Driver: `OrbbecSDK_ROS2` (built in `yahboomcar_ws`)
  - Canonical launch: `orbbec_camera/launch/dabai_dcw2.launch.py`
  - Video devices: `/dev/video0`, `/dev/video1`
  - Resolution / FOV / depth range: **[unverified]** — pull from the Orbbec
    DaBai DCW2 datasheet before tuning detection.
- **Mounting — EYE IN HAND:** the Orbbec is mounted on `arm4` near the wrist,
  modelled by the fixed joint `DCW2_Joint` (`arm4` → `DCW2`). Camera pose is
  **not** fixed relative to `base_link`; pose estimation must use live TF
  lookups against the arm chain.
- **Second camera: NONE.** The URDF contains a stale `Camera` link (mesh
  `Camera.STL`) on `base_link` via `Camera_Joint`, limits `(0, 0)`. No
  physical camera corresponds to it. The link is kept only because the MoveIt
  SRDF references it in disable-collisions entries. Ignore in all perception
  code.
- **Note:** `ros-humble-realsense2-camera` is installed but no RealSense
  device is connected. Ignore for this project.

## LiDAR

**Status: verified live 2026-08-26.**

- **Count:** 2 units. Model string from `.bashrc`: `RADAR=Tmini-plus*2`
  (LDROBOT **Tmini Plus** ×2).
- **No driver package, and none is needed.** Both scans are published by
  `/YB_Node` — i.e. the STM32 board pushes them over micro-ROS. Neither LiDAR
  appears as a USB-serial device. (Only two USB-serial devices exist on the
  whole robot: the CP210x STM32 link, and a CH340 `1a86:7522` symlinked to
  `/dev/mic`, which is the **voice module**, not a LiDAR.)
- **Field of view: 270° each**, not 180°. Measured from live `LaserScan`:
  - `/scan0` — frame `laser0_frame`, `angle_min 0.0` → `angle_max 4.7124` rad
  - `/scan1` — frame `laser1_frame`, `angle_min −3.1416` → `angle_max 1.5708` rad
  - `angle_increment` 0.009442 rad (~0.54°), `range_min` 0.05 m,
    `range_max` **12.0 m**
  - These are 360° sensors windowed to 270°; the missing quadrant on each
    points into the chassis.
- **Placement** (from `~/M3Pro_ws/src/M3Pro/urdf/M3Pro.urdf`, ROS convention
  +x forward / +y left, both at z = 0.1253 m, rpy 0 0 0):
  - `laser0_frame` → xyz `(−0.11617, +0.09156, 0.1253)` = **rear-left**
  - `laser1_frame` → xyz `(+0.10766, −0.09078, 0.1253)` = **front-right**
  - Diagonal opposition → combined coverage 360°.
- **Merging:** `ira_laser_tools` merges `/scan0` + `/scan1` → `/scan_multi`
  in frame `base_link`; then filtered by `yahboom_laser_filter`.
  Launch `yahboom_M3Pro_laser/launch/laser_driver.launch.py` starts merge +
  filter only (the scans themselves come from `/YB_Node` regardless).
- **Merge config:** `~/M3Pro_ws/src/M3Pro_core/ira_laser_tools/config/laserscan_merge.yaml`
  — `angle_min −3.14`, `angle_max 3.14`, `angle_increment 0.017453` (1°),
  `range_min 0.05`, `range_max 4.0`.
- **The 4.0 m cap is the merge config's choice, not a sensor limit.** Native
  range is 12 m (confirmed live). Raise it in the yaml if navigation needs
  longer range.

## Human interface (added 2026-08-26)

The robot is operated as a full wireless desktop — no VNC, no X11 forwarding, no
Jupyter needed. Course 0 §2 is therefore skippable in full on this setup.

- **Display out:** DP-1 → wireless video transmitter → **DELL S2722QC** on the desk.
  `card1-DP-1: connected`, negotiated at **1920x1080** (the transmitter is the limit;
  the monitor itself is 4K). A real X session runs on `:0` with the `nvidia` driver —
  *not* the dummy/virtual desktop, so the `xserver-xorg-video-dummy` procedure in
  course 0 §1.2.1 does not apply and must not be run.
- **Input in:** **Logitech Unifying Receiver** (`046d:c52f`) on the robot's USB —
  wireless keyboard + mouse. Appears as `Logitech USB Receiver` in
  `/proc/bus/input/devices`.
- **Practical split:** anything graphical (rviz2, OpenCV windows, MoveIt, Gazebo, the
  §3 arm-offset calibration window) runs on the robot's own desktop and is watched on
  the desk monitor. Anything headless (launching nodes, editing files, `ros2 topic`)
  goes over `ssh robot`.
- **No VNC server is installed** (only client libs: `libvncclient`, `libvncserver`,
  `remmina-plugin-vnc`). Don't follow §1.2.2 expecting one to be there.
- **jupyter-lab** does autostart and listens on `:8888`, but the vendor guide itself
  advises against using it on Orin. Unused here.

## Low-level control board

- **MCU:** STM32 (H743 per Yahboom docs — **[unverified on this unit]**; no
  evidence of the variant found anywhere on the filesystem)
- **Link:** USB-serial CP210x at `/dev/myserial` → `/dev/ttyUSB0`, 2 000 000 baud
- **Protocol:** micro-ROS, agent launched by `~/start_agent.sh`
  (`~/mircoROS_agent/install`) — note the vendor's spelling `mircoROS`
- **Gamepad autostart disabled 2026-08-26** — `joy_control.desktop` moved out of
  `~/.config/autostart/` (course 0 §1.3). Backups at `~/joy_control.desktop` on the
  robot and `Robot_AI/robot_config_backups/` off it. Do **not** disable
  `agent_autostart .desktop` — that one starts `/YB_Node`.
- **Firmware parameters:** `~/config_robot.py` (domain ID, motor PID, IMU yaw
  PID, linear/angular scaling, arm mid-values). Course 0 §6. Shut down the
  agent before running it.

## Network

- **Primary interface:** `wlP1p1s0` (WiFi), DHCP address on the home network
- **Fallback:** ROSMASTER AP at `192.168.8.88` **[unverified]**
- **ROS_DOMAIN_ID:** `30` (set in `~/.bashrc` and in `start_agent.sh`)
- **DDS: default settings.** `~/fastdds_all_interfaces.xml` exists (738 B) but
  `FASTRTPS_DEFAULT_PROFILES_FILE` is **commented out** in both `~/.bashrc:124`
  and `~/start_agent.sh`. The custom profile is *not* in effect. Uncomment in
  both places if multi-interface DDS discovery is ever needed.

## Two URDFs — don't mix them up

| File | Contains | Missing |
|---|---|---|
| `~/yahboomcar_ws/src/yahboom_M3Pro_description/urdf/M3Pro.urdf` | arm chain, gripper, `DCW2` camera, stale `Camera` link, wheels | **no laser links** |
| `~/M3Pro_ws/src/M3Pro/urdf/M3Pro.urdf` | `laser0_frame`, `laser1_frame` and their joints | — |

Perception/manipulation work reads the first; navigation work needs the second.

## Existing ROS 2 workspaces on the robot

- `~/yahboomcar_ws/src` — arm stack (`arm_msgs`, `arm_kin`, `arm_interface`),
  Orbbec SDK, description, YOLOv8, laser merge/filter launch, mediapipe,
  `M3Pro_config` / `M3Pro_demo` / MoveIt configs, `yahboomcar_ctrl`
- `~/M3Pro_ws/src` — core libs (`ira_laser_tools`, `imu_tools`,
  `slam_gmapping`, `yahboom_laser_filter`), navigation, slam_mapping,
  calibration, patrol, multi-brains, large-model integration
- `~/m3pro_gazebo_ws` — Gazebo simulation workspace
- `~/mircoROS_agent` — micro-ROS agent for the STM32 link
- `~/uros_ws` — micro-ROS workspace

Reuse these where sensible instead of rewriting drivers.

## Still open

- [ ] Arm max reach, payload, gripper opening width — datasheet or measure
- [ ] Orbbec DaBai DCW2 depth range, FOV, min range — datasheet
- [ ] STM32 MCU variant (H743 assumed, no on-device evidence)
- [ ] Retest the `192.168.8.88` AP fallback
- [ ] Confirm `/scan_multi` actually appears once `laser_driver.launch.py` runs
      (merge node has never been observed running)

## Change log

**2026-08-26 — full re-verification against the live robot.** Corrections to
the 2026-04-08 version:

1. **Arm serial bus.** Old file: "`/dev/ttyUSB0` (direct serial to arm servo
   controller). **Not** the STM32 micro-ROS pipe." Wrong — `/dev/ttyUSB0` *is*
   `/dev/myserial` *is* the STM32. There is no separate arm servo controller.
2. **Arm driver.** Old file named `arm_driver.py` as the driver. That package
   is unbuilt leftover code from the DOFBOT Pro. The arm is driven by
   `/YB_Node` via `/arm6_joints`.
3. **LiDAR FOV.** Old file: 180° each. Measured: **270° each.**
4. **LiDAR driver / serial ports.** Old file listed these as unknown and
   speculated `/dev/mic` might be a LiDAR. Resolved: both scans come from the
   STM32 over micro-ROS; `/dev/mic` is the voice module.
5. **LiDAR model.** Old file: "LD-Mini Plus". Banner says `Tmini-plus*2`.

Also corrected: DDS custom profile is not active; the laser frames live in a
second URDF the old file never mentioned; `~/m3pro_gazebo_ws` was missing from
the workspace list; Docker containers are Dify images, not robot images.
Closed as verified-unavailable: arm servo effort/current feedback does not
exist on any topic.
