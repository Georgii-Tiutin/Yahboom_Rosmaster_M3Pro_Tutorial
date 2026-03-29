# **AI Large Model Preparation**

### **1. Lidar Mapping**

Refer to the instructions in [6. LiDAR] - [6. Gmapping-SLAM Mapping] of this product tutorial to start the robot, build a map, and save it. This map will be used later for navigation in the AI large model.

## **2. Robotic Arm Calibration**

Refer to the instructions in [0. Manual and Installation Steps] - [Robotic Arm Calibration] of this product tutorial to start the robot arm calibration program, calibrate the offsets, and save them in an offset parameter file. This offset parameter file will be loaded later when the AI large model controls the robot arm gripping.

#### **3. ASR Device Reading and Adding**

This selection is not required for the Jetson Orin version; the input and output audio devices are automatically configured upon startup. However, the Jetson Nano and Raspberry Pi versions use Docker and have different purchased packages, so the number of input and output devices must be read and determined.

## **4. Configure Large Model API Keys**

All Large Model gameplay requires configuring the relevant Large Model keys. This section covers a lot of topics, divided into two categories: domestic and international. I won't go into detail here. Please refer to Tutorial 2 - AI Large Model Basics - 5 Configuring AI Large Models.