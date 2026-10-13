# **ROSMASTER-M3Pro-MCP Feature Summary**

#### **[ROSMASTER-M3Pro-MCP](#page-0-0) Feature Summary**

Feature [Overview](#page-0-1)

[Detailed Function](#page-2-0) Descriptions

- <span id="page-0-0"></span>[1. MoveWithSpeed](#page-2-1)
- [2. Move](#page-2-2)
- [3. GetCurrentArmJointAngles](#page-2-3)
- [4. GetEndEffectorPose](#page-2-4)
- [5. ControlSixArmJoint](#page-3-0)
- [6. ControlSingleArmJoint](#page-3-1)
- [7. Place](#page-3-2)

#### **Return Value**: [common\\_response](#page-3-3)

- [8. Pick](#page-3-4)
- [9. AdjustCameraView](#page-4-0)
- [10. SeeWhat](#page-4-1)
- [11. InitArmPose](#page-4-2)
- [12. GetBbox](#page-4-3)
- [13. GetPlacePoint](#page-5-0)
- [14. AdjustChassisFitArmRange](#page-5-1)
- [15. RecordMapLocation](#page-5-2)
- [16. GetMapMapping](#page-5-3)
- [17. Navigation](#page-6-0)
- [18. GetWasteRecognitionResults](#page-6-1)
- [19. GraspWaste](#page-6-2)
- [20. PlaceWaste](#page-6-3)
- [21. TTS](#page-6-4)
- [22. Rotate](#page-7-0)
- [23. TargetTrack](#page-7-1)
- [24. GetTargetDist](#page-7-2)
- [25. GraspArUcoTarget](#page-7-3)
- [26. GetAprilTagIDs](#page-7-4)
- [27. FollowLine](#page-8-0)

#### Function [Categories](#page-8-1)

Chassis [Control](#page-8-2)

[Robotic Arm Control](#page-8-3)

Grasping [Operations](#page-8-4)

Vision [Functions](#page-8-5)

Mapping [& Navigation](#page-9-0)

<span id="page-0-1"></span>Speech [Synthesis](#page-9-1)

This document summarizes all MCP tool features registered in mcp\_action.py , helping users quickly understand the function, parameters, and usage of each tool.

# **Feature Overview**

| No. | Tool Name                  | Function Description                                                            |
|-----|----------------------------|---------------------------------------------------------------------------------|
| 1   | MoveWithSpeed              | Control the robot's omnidirectional chassis speed                               |
| 2   | Move                       | Control the robot chassis to move a specified<br>distance                       |
| 3   | GetCurrentArmJointAngles   | Retrieve the robotic arm's current joint angles                                 |
| 4   | GetEndEffectorPose         | Retrieve the end-effector's pose                                                |
| 5   | ControlSixArmJoint         | Simultaneously control the arm's 6 joints                                       |
| 6   | ControlSingleArmJoint      | Control a single arm joint to a specified angle                                 |
| 7   | Place                      | Place an object at specified coordinates                                        |
| 8   | Pick                       | Grasp an object                                                                 |
| 9   | AdjustCameraView           | Adjust the camera's viewpoint                                                   |
| 10  | SeeWhat                    | Capture a camera image and return the save path                                 |
| 11  | InitArmPose                | Restore the arm to its preset initial pose                                      |
| 12  | GetBbox                    | Detect the bounding box coordinates of a target<br>object                       |
| 13  | GetPlacePoint              | Retrieve placement point coordinates and check<br>reachability                  |
| 14  | AdjustChassisFitArmRange   | Quickly adjust the chassis so the target point is<br>within the arm's workspace |
| 15  | RecordMapLocation          | Save the current location to a map mapping file                                 |
| 16  | GetMapMapping              | Retrieve the mapping relationship between location<br>names and symbols         |
| 17  | Navigation                 | Navigate to a specified location using a target<br>symbol                       |
| 18  | GetWasteRecognitionResults | Retrieve waste recognition results from the YOLO<br>model                       |
| 19  | GraspWaste                 | Grasp a waste object                                                            |
| 20  | PlaceWaste                 | Place a waste object                                                            |
| 21  | TTS                        | Robot speech synthesis                                                          |
| 22  | Rotate                     | Rotate in place by a specified angle                                            |
| 23  | TargetTrack                | Visually track a target object                                                  |
| 24  | GetTargetDist              | Calculate the distance between the target and the<br>robot chassis              |
| 25  | GraspArUcoTarget           | Grasp an AprilTag target with a specified ID                                    |

| No. | Tool Name      | Function Description                           |
|-----|----------------|------------------------------------------------|
| 26  | GetAprilTagIDs | Retrieve AprilTag IDs within the field of view |
| 27  | FollowLine     | Follow a line of a specified color             |

# <span id="page-2-0"></span>**Detailed Function Descriptions**

### **1. MoveWithSpeed**

**Function**: Controls the robot's omnidirectional chassis movement using velocity commands.

#### **Parameters**:

- <span id="page-2-1"></span>linear\_x : Linear velocity in the X direction (Range: -2.5 ~ 2.5; Default: 1.5)
- linear\_y : Linear velocity in the Y direction (Range: -2.5 ~ 2.5; Default: 1.5)
- angular\_z : Angular velocity around the Z axis (Range: -2.5 ~ 2.5; Default: 1.5)
- <span id="page-2-2"></span>duration : Duration of movement (in seconds; Default: 1.0)

**Return Value**: common\_response

### **2. Move**

**Function**: Controls the robot's chassis to move a specified distance.

#### **Parameters**:

- distance : Movement distance (in meters)
- direction : Movement direction
- 'forward' : Move forward
- 'backward' : Move backward
- 'left' : Move laterally to the left
- <span id="page-2-3"></span>'right' : Move laterally to the right

**Return Value**: common\_response

### **3. GetCurrentArmJointAngles**

**Function**: Retrieves the current joint angles of the robotic arm.

**Parameters**: None

**Return Value**: ArmJointAngles

- arm\_joint\_1 ~ arm\_joint\_5 : Angles for robotic arm joints 1 through 5.
- <span id="page-2-4"></span>gripper : Gripper angle.

### **4. GetEndEffectorPose**

**Function**: Retrieves the pose (position and orientation) of the end effector (comprising the gripper and camera).

**Parameters**: None

**Return Value**: EndEffectorPose

- x , y , z : Position coordinates.
- <span id="page-3-0"></span>roll , pitch , yaw : Orientation angles.

### **5. ControlSixArmJoint**

**Function**: Simultaneously controls all 6 joints of the robotic arm (the 6th joint controls the gripper angle).

#### **Parameters**:

- arm\_joint\_1 : Joint 1 angle (Range: 0 ~ 180).
- arm\_joint\_2 : Joint 2 angle (Range: -5 ~ 180).
- arm\_joint\_3 : Joint 3 angle (Range: -10 ~ 180).
- arm\_joint\_4 : Joint 4 angle (Range: -50 ~ 180).
- arm\_joint\_5 : Joint 5 angle (Range: 0 ~ 180).
- arm\_joint\_6 : Gripper angle (Range: 0 ~ 180; 180 = fully open, 0 = fully closed).
- <span id="page-3-1"></span>runtime : Duration of the movement (in milliseconds; Default: 1500; Range: 0 ~ 2000).

**Return Value**: common\_response

# **6. ControlSingleArmJoint**

**Function**: Sets a single robotic arm joint to a specified angle.

#### **Parameters**:

- arm\_joint\_id : Joint ID (1-6; corresponds to robotic arm joints 1-6, where Joint 6 is the gripper).
- angle : Target angle (For Joint 6... gripper\_range : Gripper range (0 ~ 180)
- <span id="page-3-2"></span>runtime : Motion duration (milliseconds; default: 1500, range: 0 ~ 2000)

**Return Value**: common\_response

### **7. Place**

**Function**: Places an object at the specified coordinates

#### **Parameters**:

- place\_x : X-coordinate (meters)
- place\_y : Y-coordinate (meters)
- <span id="page-3-4"></span><span id="page-3-3"></span>place\_z : Z-coordinate (meters)

# **Return Value:** common\_response

### **8. Pick**

**Function**: Grabs an object.

#### **Parameters**:

x1 , y1 : Coordinates of the top-left corner of the target object.

<span id="page-4-0"></span>x2 , y2 : Coordinates of the bottom-right corner of the target object.

**Return Value**: common\_response

# **9. AdjustCameraView**

**Function**: Adjusts the camera view (pitch and yaw angles).

#### **Parameters**:

- pitch : Pitch angle adjustment (degrees; positive = up, negative = down; recommended step size: 5–10 degrees; default: 0).
- yaw : Yaw angle adjustment (degrees; positive = right, negative = left; recommended step size: 5–10 degrees; default: 0).

**Return Value**: dict or common\_response

- Returns {"image": adjusted\_image} upon success.
- <span id="page-4-1"></span>Returns common\_response upon failure.

### **10. SeeWhat**

**Function**: Captures an image from the camera and returns the path where the image is saved.

**Parameters**: None.

**Return Value**: dict or common\_response

- Returns {"image": image\_save\_path} upon success.
- <span id="page-4-2"></span>Returns common\_response upon failure.

### **11. InitArmPose**

**Function**: Restores the robotic arm to its preset initial pose.

**Parameters**: None.

**Return Value**: common\_response

### **12. GetBbox**

**Function**: Detects and returns the bounding box coordinates of a target object based on a description.

#### **Parameters**:

<span id="page-4-3"></span>query : A description of the target object at its current location, including its visual features.

**Return Value**: BoxLocalization or common\_response

- Returns BoxLocalization(bbox=bounding\_box, verify\_image=verification\_image\_path) upon success.
- Returns common\_response upon failure.

# **13. GetPlacePoint**

**Function**: Retrieves the coordinates for a placement point and checks whether it lies within the robotic arm's reachable workspace.

#### **Parameters**:

<span id="page-5-0"></span>query : Query description.

**Return Value**: PlacePoint or common\_response

- Returns upon success: PlacePoint(info=info, target\_point=target\_point, place\_verify\_image=place\_verify\_image\_path)
- <span id="page-5-1"></span>Returns common\_response upon failure.

# **14. AdjustChassisFitArmRange**

**Function**: Quickly adjust the mobile chassis so that the target point falls within the robotic arm's workspace.

#### **Parameters**:

<span id="page-5-2"></span>x , y , z : Target coordinates (meters)

**Return Value**: common\_response

### **15. RecordMapLocation**

**Function**: Save the current location to the map mapping file.

#### **Parameters**:

<span id="page-5-3"></span>name : Location name symbol : Location symbol

**Return Value**: common\_response

### **16. GetMapMapping**

**Function**: Retrieve the mapping relationship between all location names and their corresponding symbols.

**Parameters**: None

**Return Value**: common\_response or str

- Returns the mapping relationship string upon success.
- Returns common\_response upon failure.

### **17. Navigation**

**Function**: Navigate to a specified location using its target point symbol.

#### **Parameters**:

<span id="page-6-1"></span><span id="page-6-0"></span>location : The symbol corresponding to the location in the map mapping file.

**Return Value**: common\_response

### **18. GetWasteRecognitionResults**

**Function**: Retrieve waste recognition results from the YOLO model.

**Parameters**: None

**Return Value**: waste\_recognition\_result or common\_response

- Returns the waste recognition results upon success.
- <span id="page-6-2"></span>Returns common\_response upon failure.

### **19. GraspWaste**

**Function**: Grasp a waste object.

#### **Parameters**:

<span id="page-6-3"></span>waste\_name : Name of the waste object (obtained from the waste recognition results).

**Return Value**: common\_response

# **20. PlaceWaste**

**Function**: Place a waste object.

**Parameters**: None

**Return Value**: common\_response

### **21. TTS**

**Function**: Robot Text-to-Speech (TTS) synthesis.

#### **Parameters**:

<span id="page-6-4"></span>text : The text content to be synthesized.

**Return Value**: common\_response

### **22. Rotate**

**Function**: Rotate in place by a specified angle.

#### **Parameters**:

<span id="page-7-1"></span><span id="page-7-0"></span>angle : Rotation angle (degrees; negative = clockwise/right, positive = counter-clockwise/left).

**Return Value**: common\_response

# **23. TargetTrack**

**Function**: Visually track a target object

#### **Parameters**:

- x1\_or\_cmd :
- String "cancel" : Stop current tracking
- Integer: Serves as the x1 coordinate of the target tracking bounding box
- y1 : y-coordinate of the target object's top-left corner (Optional)
- x2 : x-coordinate of the target object's bottom-right corner (Optional)
- <span id="page-7-2"></span>y2 : y-coordinate of the target object's bottom-right corner (Optional)

**Return Value**: common\_response

### **24. GetTargetDist**

**Function**: Calculate the distance between the target and the robot chassis based on an object description

#### **Parameters**:

<span id="page-7-3"></span>query : A description of the target object's position and visual features within the current field of view (String)

**Return Value**: common\_response

# **25. GraspArUcoTarget**

**Function**: Grasp an AprilTag target with a specified ID

#### **Parameters**:

<span id="page-7-4"></span>target\_id : The ID of the AprilTag to be grasped (Integer)

**Return Value**: common\_response

### **26. GetAprilTagIDs**

**Function**: Retrieve the IDs of AprilTags currently within the field of view

**Parameters**: None

**Return Value**: common\_response

# **27. FollowLine**

**Function**: Drive along a colored line on the ground

#### **Parameters**:

<span id="page-8-1"></span><span id="page-8-0"></span>color : The color of the line to follow; possible values: "red" , "green" , "blue" , "yellow" (String)

**Return Value**: common\_response

# **Function Categories**

# **Chassis Control**

- <span id="page-8-2"></span>MoveWithSpeed
- Move
- Rotate
- AdjustChassisFitArmRange
- <span id="page-8-3"></span>Navigation

### **Robotic Arm Control**

- GetCurrentArmJointAngles
- GetEndEffectorPose
- ControlSixArmJoint
- ControlSingleArmJoint
- <span id="page-8-4"></span>InitArmPose

### **Grasping Operations**

- Pick
- Place
- GraspWaste
- PlaceWaste

# **Vision Functions**

- <span id="page-8-5"></span>AdjustCameraView
- SeeWhat
- GetBbox
- GetPlacePoint
- TargetTrack
- GetWasteRecognitionResults
- GetTargetDist
- GetAprilTagIDs
- GraspArUcoTarget
- FollowLine

### **Mapping & Navigation**

- <span id="page-9-0"></span>RecordMapLocation
- GetMapMapping
- Navigation

### **Speech Synthesis**

<span id="page-9-1"></span>TTS