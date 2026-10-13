# **Summary Of Common Errors And Solutions**

#### **[Summary Of](#page-0-0) Common Errors And Solutions**

- [1. Multi\\_Brains\\_Pre](#page-1-0) Package
  - 1.1 Configuration File [Related Errors](#page-1-1)

<span id="page-0-0"></span>Error [1.1.1: Configuration](#page-1-2) File Not Found

Error [1.1.2: YAML](#page-1-3) Parsing Failed

1.2 ASR Speech Recognition [Related Errors](#page-2-0)

Error 1.2.1: ASR Engine [Initialization](#page-2-1) Failed

Error [1.2.2: Speech](#page-2-2) Recognition Failed

Error 1.2.3: VAD Engine [Initialization](#page-2-3) Failed

Error 1.2.4: Audio [Stream Open](#page-3-0) Failed

Error 1.2.5: No Speech [Detected](#page-3-1)

Error [1.2.6: Unsupported Language](#page-3-2)

1.3 TTS Speech Synthesis [Related Errors](#page-4-0)

Error 1.3.1: TTS Engine [Initialization](#page-4-1) Failed

Error [1.3.2: Speech](#page-4-2) Synthesis Failed

1.4 Voice [Wakeup Module](#page-5-0) Serial Communication Related Errors

Error [1.4.1: Serial](#page-5-1) Port Open Failed

Error 1.4.2: Serial Port [Reconnection](#page-5-2) Failed

Error [1.4.3: Serial](#page-5-3) Port Send Failed

1.5 ROS [Communication](#page-6-0) Related Errors

Error [1.5.1: Action](#page-6-1) Server Unavailable

Error [1.5.2: Action](#page-6-2) Goal Rejected

1.6 Large Model Service [Related Errors](#page-6-3)

Error 1.6.1: Dify [Connection](#page-6-4) Failed

Error [1.6.2: Model](#page-7-0) Request Failed

1.7 Motion Control [Related Errors](#page-7-1)

Error 1.7.1: TF [Transform Acquisition](#page-7-2) Failed

Error 1.7.2: TF [Timestamp Too](#page-8-0) Old

Error [1.7.3: Joint](#page-8-1) Values Not Initialized

1.8 Audio [Playback Related Errors](#page-8-2)

Error [1.8.1: Wakeup Audio](#page-8-3) Loading Failed

- [2. Waste\\_Classify](#page-9-0) Module
  - 2.1 Model Loading [Related Errors](#page-9-1)

Error [2.1.1: Model](#page-9-2) File Not Found

Error [2.1.2: YOLO Model](#page-9-3) Initialization Error

Error 2.1.3: Model Inference [Startup Failed](#page-9-4)

2.2 Image Detection [Related Errors](#page-10-0)

Error [2.2.1: Image](#page-10-1) Shape Not Initialized

Error [2.2.2: Image](#page-10-2) Save Failed

- 3. Pcl\_Seg Point [Cloud Segmentation](#page-10-3) Module
  - 3.1 Depth Image [Processing](#page-10-4) Errors

Error [3.1.1: Invalid ROI](#page-10-5) Region (Common)

Error [3.1.2: No](#page-11-0) Depth Image

Error 3.1.3: No [Valid Depth](#page-11-1) Points In Circular Region

Error [3.1.4: Target](#page-11-2) Point Outside Image Boundary

Error [3.1.5: Invalid Radius](#page-12-0) Value

3.2 TF [Transform Related Errors](#page-12-1)

Error 3.2.1: TF [Transform Not](#page-12-2) Available

Error 3.2.2: TF [Transform Failed](#page-13-0)

3.3 Point Cloud Processing [Related Warnings](#page-13-1)

```
Error 3.3.1: ROI Point Cloud Empty
```

Error [3.3.2: No](#page-13-3) Cluster Found

Error 3.3.3: No [Valid Center](#page-14-0) Data

#### [4. Super\\_Tracker](#page-14-1) Target Tracking Module

4.1 Tracker [Initialization](#page-14-2) Errors

Error [4.1.1: Tracker](#page-14-3) Creation Failed

Error 4.1.2: Display Window [Configuration](#page-14-4) Conflict

4.2 Image Frame [Processing](#page-15-0) Warnings

Error [4.2.1: Received Empty](#page-15-1) Or Invalid Frame

4.3 ROI [Selection](#page-15-2) Errors

Error [4.3.1: Cannot](#page-15-3) Select ROI On Empty Frame

Error [4.3.2: Invalid ROI](#page-15-4) Selected

Error 4.3.3: Set [Track ROI](#page-16-0) Failed

<span id="page-1-2"></span><span id="page-1-1"></span><span id="page-1-0"></span>Error [4.3.4: Tracking](#page-16-1) Start Failed

5. General [Troubleshooting](#page-16-2) Suggestions

5.1 Log Level [Adjustment](#page-17-0)

5.2 Common [Diagnostic Commands](#page-17-1)

# **1. Multi\_Brains\_Pre Package**

# **1.1 Configuration File Related Errors**

# **Error 1.1.1: Configuration File Not Found**

### **Error Log:**

```
multi_brains_pre_setting.yaml file not found, Please check: Whether the file
exists;: {config_file}
```

### **Cause:**

- The multi\_brains\_pre\_setting.yaml configuration file path does not exist
- The file has been deleted or moved

# **Solution:**

<span id="page-1-3"></span>1. Copy multi\_brains\_pre\_setting.yaml from the attached source code to the specified directory

# **Error 1.1.2: YAML Parsing Failed**

### **Error Log:**

```
multi_brains_pre_setting.yaml file YAML parsing failed: {exc}, Please check:
Whether the file format has been modified
```

## **Cause:**

YAML file format error (incorrect indentation, unescaped special characters, etc.)

### **Solution:**

1. Modify multi\_brains\_pre\_setting.yaml, refer to the factory file format in the attached source code

# <span id="page-2-0"></span>**1.2 ASR Speech Recognition Related Errors**

# **Error 1.2.1: ASR Engine Initialization Failed**

### **Error Log:**

```
ASR Engine: {model_name} initialized failed
```

### **Cause:**

- API Key configuration error or invalid
- Model name not supported
- Network issue (online ASR)
- Key file decryption failed (Xunfei ASR)

## **Solution:**

- 1. Check if ALIYUN\_API\_KEY is correctly configured
- 2. Confirm the model name used is in the supported list:
  - paraformer-realtime-v2/v1
  - paraformer-realtime-8k-v2/v1
  - gummy-realtime-v1/gummy-chat-v1
- 3. For Xunfei ASR, check the key file path and decryption
- <span id="page-2-2"></span>4. Test network connection

# **Error 1.2.2: Speech Recognition Failed**

## **Error Log:**

```
asr recognize failure
Online ASR recognition failed: {error_message}
```

#### **Cause:**

- API invalid
- Online speech recognition service unavailable

# **Solution:**

- 1. Check network connection stability
- <span id="page-2-3"></span>2. Check if API quota has been exhausted

# **Error 1.2.3: VAD Engine Initialization Failed**

#### **Error Log:**

```
VadEngine initialization failed
VadEngine initialization exception: {exc}
```

- VAD model file does not exist
- Model path configuration error

voice\_toolbox library not properly installed

## **Solution:**

- 1. Check if the silero\_vad.int8.onnx model file has been deleted
- <span id="page-3-0"></span>2. Download the VAD model file from the attached source code

# **Error 1.2.4: Audio Stream Open Failed**

### **Error Log:**

Audio stream open failed: {exc}

### **Cause:**

- Microphone device not connected
- Audio device occupied by another program

### **Solution:**

- 1. Check if the microphone device is properly connected
- <span id="page-3-1"></span>2. Use arecord -l to view available audio devices
- 3. Close other programs occupying the audio device

# **Error 1.2.5: No Speech Detected**

#### **Warning Log:**

No speech detected, timeout exit.

## **Cause:**

- Microphone volume too low
- Ambient noise too high

#### **Solution:**

- 1. Increase the microphone input volume
- 2. Reduce ambient noise
- <span id="page-3-2"></span>3. Speak closer to the microphone

# **Error 1.2.6: Unsupported Language**

### **Warning Log:**

Unsupported language: {language}, only 'zh' and 'en' are supported

## **Cause:**

- Configured unsupported language code
- LANGUAGE parameter set incorrectly

#### **Solution:**

1. Change the LANGUAGE parameter to 'zh' (Chinese) or 'en' (English)

# <span id="page-4-0"></span>**1.3 TTS Speech Synthesis Related Errors**

# <span id="page-4-1"></span>**Error 1.3.1: TTS Engine Initialization Failed**

#### **Error Log:**

```
Failed to initialize Piper TTS engine: {e}
Failed to initialize Baidu TTS engine: {e}
Tongyi TTS_Engine initialized failed
Baidu TTS_Engine initialized failed
Xunfei TTS_Engine initialized failed
Piper TTS_Engine initialized failed
```

### **Cause:**

- TTS model file missing
- API Key configuration error
- Configuration file read failure
- Key file decryption failed (Xunfei TTS)

### **Solution:**

## 1. **Piper TTS**:

- Check if the model file exists in the ~/MODELS/tts/ directory
- Confirm both .onnx and .onnx.json files exist

#### 2. **Online TTS (Alibaba Cloud/Baidu/Xunfei)**:

- Check if the corresponding API Key is correctly configured
- <span id="page-4-2"></span>Verify network connection
- 3. Check if the configuration file format is correct

# **Error 1.3.2: Speech Synthesis Failed**

## **Error Log:**

```
PiperTTS Failed to synthesize text: {e}
Speech synthesis failed. Check whether the TTS model is available
```

#### **Cause:**

- TTS engine not properly initialized?
- Online speech service unavailable?

- 1. Confirm the TTS engine has been properly initialized
- 2. Check the specific error message for targeted handling

# <span id="page-5-0"></span>**1.4 Voice Wakeup Module Serial Communication Related Errors**

# **Error 1.4.1: Serial Port Open Failed**

#### **Error Log:**

```
[kws_mic] Failed to open serial {port}: {e}
Cannot open serial port {port}, please check voice wakeup module connection
```

### **Cause:**

- Voice wakeup serial device does not exist
- Hardware connection issue

## **Solution:**

- 1. Check if the serial device exists: ls -l /dev/mic
- <span id="page-5-2"></span>2. Check if the hardware connection is secure

# **Error 1.4.2: Serial Port Reconnection Failed**

### **Warning Log:**

```
[kws_mic] Max reconnect attempts ({max_attempts}) reached, giving up
[kws_mic] Reconnect attempt {attempt} failed: {e}
```

## **Cause:**

Hardware device disconnected

### **Solution:**

<span id="page-5-3"></span>1. Replug the USB device

# **Error 1.4.3: Serial Port Send Failed**

## **Error Log:**

```
send fial: {e}
```

# **Cause:**

- Serial connection disconnected
- Buffer overflow
- Voice wakeup device not responding

- 1. Check serial connection status
- 2. Restart the program
- 3. Check if the hardware device is working properly

# <span id="page-6-0"></span>**1.5 ROS Communication Related Errors**

# <span id="page-6-1"></span>**Error 1.5.1: Action Server Unavailable**

### **Warning Log:**

```
play_audio action server not available, skip wakeup voice
play_audio action server not available, skip error audio
play_audio action server not available, skip voice
```

### **Cause:**

common\_service node not started

## **Solution:**

- 1. Confirm the common\_service node has started
- <span id="page-6-2"></span>2. Use ros2 action list to check available actions

# **Error 1.5.2: Action Goal Rejected**

### **Warning Log:**

```
play_audio goal rejected
TTS play goal rejected
```

### **Cause:**

Audio file path does not exist

# **Solution:**

- 1. Check if the audio file exists
- <span id="page-6-4"></span><span id="page-6-3"></span>2. Check the specific rejection reason in the logs

# **1.6 Large Model Service Related Errors**

# **Error 1.6.1: Dify Connection Failed**

## **Error Log:**

```
Dify LLM connection failed, Please check whether DIY dify has been started, API
and BASE_URL settings
Error log: {error_message}
Dify service connection failed: {status_code}
Dify service connection failed: {str(e)}
```

### **Cause:**

- Dify service not started
- BASE\_URL configuration error
- **API Key invalid** (most common issue, the Dify app API does not match DIFY\_API\_KEY in the configuration file)

- 1. Confirm the Dify service has started and is running properly
- 2. Check the DIFY\_BASE\_URL configuration (e.g., <http://localhost/v1>)
- 3. Verify the DIFY\_API\_KEY is correct
- <span id="page-7-0"></span>4. Use curl to test the connection: curl -H "Authorization: Bearer {API\_KEY}" {BASE\_URL}/meta

# **Error 1.6.2: Model Request Failed**

### **Error Log:**

The model request failed. Check whether the dify or AI model is normal. Error Log: {error\_message}

#### **Cause:**

- Dify service异常
- Model service down
- Model API has no quota
- Timeout

## **Solution:**

- 1. Check Dify service status
- 2. Check Dify service logs
- 3. Check API account
- <span id="page-7-1"></span>4. Restart the Dify service

# **1.7 Motion Control Related Errors**

# **Error 1.7.1: TF Transform Acquisition Failed**

#### **Error Log:**

<span id="page-7-2"></span>Failed to get base\_link-roi transform after {max\_attempts} attempts, check the tf\_tree is normal ?

## **Cause:**

- TF tree incomplete
- pcl\_segment node not publishing TF
- Target tracking lost the target

- 1. Use ros2 run tf2\_tools view\_frames to check the TF tree
- 2. Confirm the pcl\_segment node is running properly
- 3. Ensure the node is tracking the target

# **Error 1.7.2: TF Timestamp Too Old**

## **Warning Log:**

```
tf too old for base_link-roi: {age:.3f}s ago (attempt {attempt}/{max_attempts})
```

#### **Cause:**

- TF publish frequency too low
- System latency too high, CPU load too high
- Target tracking lost the target

### **Solution:**

- 1. Increase TF publish frequency
- 2. Optimize system performance
- 3. Increase the tf\_tolerance parameter value
- <span id="page-8-1"></span>4. Disable unnecessary nodes

# **Error 1.7.3: Joint Values Not Initialized**

### **Warning Log:**

Joint1、joint\_2、joint\_4 values not initialized, skipping gaze control.

#### **Cause:**

- Robotic arm query service call failed
- Initialization process not completed

#### **Solution:**

- 1. Check if the robotic arm service is normal
- 2. Verify if the arm\_util node has started
- <span id="page-8-3"></span><span id="page-8-2"></span>3. Check the service call logs

# **1.8 Audio Playback Related Errors**

# **Error 1.8.1: Wakeup Audio Loading Failed**

#### **Error Log:**

Failed to load the wake-up word audio file :{e}

# **Cause:**

- Audio file directory does not exist
- File format not supported

- 1. Check the system\_vioce/zh/wakeup or system\_vioce/en/wakeup directory
- 2. Confirm the WAV file exists and the format is correct
- 3. Check file read permissions
- 4. Reinstall the multi\_brains\_pre package

# <span id="page-9-0"></span>**2. Waste\_Classify Module**

# <span id="page-9-1"></span>**2.1 Model Loading Related Errors**

# **Error 2.1.1: Model File Not Found**

### **Error Log:**

```
Model file not found: {model_path}
```

#### **Cause:**

- YOLO model path configuration error
- File deleted or moved

### **Solution:**

- 1. Check the model\_path parameter configuration
- 2. Confirm the model file exists
- <span id="page-9-3"></span>3. Re-download the YOLO model file from the attached source code

# **Error 2.1.2: YOLO Model Initialization Error**

#### **Error Log:**

```
YOLO Model initialization error :{e}
```

#### **Cause:**

- Factory system Python environment corrupted
- Model file format error
- Insufficient memory

#### **Solution:**

- 1. Check if the model file is in a valid ONNX format
- 2. Try using CPU mode: set the device parameter to "cpu"
- <span id="page-9-4"></span>3. Check if system memory is sufficient

# **Error 2.1.3: Model Inference Startup Failed**

# **Error Log:**

```
Model inference failed to start: {str(e)}
```

#### **Cause:**

- Shared memory creation failed
- Multi-process startup failed
- Insufficient resources

#### **Solution:**

1. Check system shared memory limit: sysctl kernel.shmmax

# <span id="page-10-0"></span>**2.2 Image Detection Related Errors**

# **Error 2.2.1: Image Shape Not Initialized**

### **Error Log:**

<span id="page-10-1"></span>Image shape not initialized, please ensure the camera is running and publishing images

### **Cause:**

- Camera not started
- Image topic not published

### **Solution:**

- 1. Confirm the camera node has started
- 2. Check if the topic /camera/color/image\_raw has data: ros2 topic echo /camera/color/image\_raw
- <span id="page-10-2"></span>3. Restart the carbase launch file

# **Error 2.2.2: Image Save Failed**

### **Error Log:**

Failed to save image: {e}

#### **Cause:**

- Output directory does not exist
- Insufficient disk space
- Camera node not started

#### **Solution:**

<span id="page-10-4"></span><span id="page-10-3"></span>1. Check the file path configuration

# **3. Pcl\_Seg Point Cloud Segmentation Module**

# **3.1 Depth Image Processing Errors**

# **Error 3.1.1: Invalid ROI Region (Common)**

#### **Warning Log:**

<span id="page-10-5"></span>Invalid ROI Region: [umin vmin umax vmax]

- Track box coordinates exceed image boundaries
- Track box dimensions are zero or negative

No depth information in the target region

## **Solution:**

- 1. Check if the track box coordinates are reasonable
- <span id="page-11-0"></span>2. Check in rviz if the target has depth information

# **Error 3.1.2: No Depth Image**

#### **Warning Log:**

No depth image received.

#### **Cause:**

- Depth camera not started
- Topic subscription failed
- Depth image not published

#### **Solution:**

- 1. Confirm the depth camera driver has started
- 2. Check if the topic /camera/depth/image\_raw has data
- 3. Verify camera hardware connection
- <span id="page-11-1"></span>4. Restart the camera node

# **Error 3.1.3: No Valid Depth Points In Circular Region**

### **Warning Log:**

No valid depth points found in the circular region.

## **Cause:**

- Target point too far or too close, no depth information near the target point
- Depth value invalid (0 or超出阈值)

# **Solution:**

- 1. Adjust the camera viewing angle and target point position
- 2. Check if the depth camera is working properly
- 3. Check in rviz if the target has depth information
- <span id="page-11-2"></span>4. Reduce ambient lighting

# **Error 3.1.4: Target Point Outside Image Boundary**

#### **Warning Log:**

```
The target point is outside the image boundary. Image size: {width}x{height},
Requested: ({x}, {y})
```

#### **Cause:**

Requested coordinates exceed image range

- Coordinate calculation error
- Image resolution change

### **Solution:**

- 1. Verify the coordinate calculation logic
- 2. Check the image resolution configuration
- 3. Add boundary checking
- <span id="page-12-0"></span>4. Use valid coordinate values

# **Error 3.1.5: Invalid Radius Value**

### **Warning Log:**

Invalid radius value.

#### **Cause:**

- Radius parameter is negative or zero
- Parameter passing error

### **Solution:**

- 1. Ensure the radius value is positive
- 2. Check the service call parameters
- <span id="page-12-2"></span><span id="page-12-1"></span>3. Use a reasonable radius value (recommended 5-50 pixels)

# **3.2 TF Transform Related Errors**

# **Error 3.2.1: TF Transform Not Available**

#### **Warning Log:**

TF transform not available between base\_link and camera\_color\_optical\_frame.

#### **Error Log:**

Failed to lookup transform: {ex.what()}

#### **Cause:**

- Missing necessary transform in the TF tree
- Camera coordinate system not configured
- TF publish node not started

- 1. Use ros2 run tf2\_tools view\_frames to check the TF tree
- 2. Ensure the camera driver publishes the correct TF
- 3. Check if the transform from base\_link to camera is correctly defined

# **Error 3.2.2: TF Transform Failed**

### <span id="page-13-0"></span>**Error Log:**

```
Failed to transform actual_pose: {ex.what()}
Failed to transform estimate_pose: {ex.what()}
Failed to transform point: {ex.what()}
```

# **Cause:**

- Coordinate system does not exist
- Transform data异常
- Timestamp issue

## **Solution:**

- 1. Check if the coordinate system name is correct
- 2. Verify TF data validity
- 3. Check timestamp synchronization
- <span id="page-13-2"></span><span id="page-13-1"></span>4. Use ros2 run tf2\_tools echo to check TF data

# **3.3 Point Cloud Processing Related Warnings**

# **Error 3.3.1: ROI Point Cloud Empty**

## **Debug Log:**

```
ROI cloud is empty, skipping this depthframe
```

#### **Cause:**

- No valid depth values within the ROI region
- Distance threshold set too small
- Target超出 distance range

# **Solution:**

- 1. Increase the distance\_threshold parameter
- 2. Adjust the ROI region size
- 3. Ensure the target is within valid distance
- <span id="page-13-3"></span>4. Check depth image quality

# **Error 3.3.2: No Cluster Found**

#### **Debug Log:**

```
No cluster found
No suitable cluster found
```

- Insufficient point cloud density
- Clustering parameters set improperly
- Target too small or too far

### **Solution:**

- 1. Decrease the cluster\_min\_size parameter
- 2. Increase the cluster\_max\_size parameter
- 3. Adjust the ClusterTolerance parameter
- <span id="page-14-0"></span>4. Ensure the target is close enough and clear

# **Error 3.3.3: No Valid Center Data**

### **Warning Log:**

GetBoxCenter: no valid data.

### **Cause:**

- Depth image not yet processed
- Clustering failed

### **Solution:**

- 1. Ensure depth image is being processed properly
- <span id="page-14-2"></span><span id="page-14-1"></span>2. Check if point cloud segmentation was successful

# **4. Super\_Tracker Target Tracking Module**

# **4.1 Tracker Initialization Errors**

# **Error 4.1.1: Tracker Creation Failed**

### **Error Log:**

<span id="page-14-3"></span>Failed to create tracker: {e.what()}

## **Cause:**

Model file does not exist

### **Solution:**

- 1. Check the model file path: \$HOME/MODELS/tracker/mixformer\_v2\_sim.onnx
- <span id="page-14-4"></span>2. Adjust the num\_threads parameter

# **Error 4.1.2: Display Window Configuration Conflict**

## **Error Log:**

display\_windows and display\_windows\_only\_track cannot both be true. Setting both to false.

#### **Cause:**

Both display parameters set to true simultaneously

Configuration logic conflict

## **Solution:**

- 1. Enable only one of the parameters:
  - display\_windows : Always show window, supports mouse selection
  - display\_windows\_only\_track : Show window only during tracking
- <span id="page-15-1"></span><span id="page-15-0"></span>2. Modify the configuration file to ensure both are not true at the same time

# **4.2 Image Frame Processing Warnings**

# **Error 4.2.1: Received Empty Or Invalid Frame**

### **Warning Log:**

Received empty or invalid frame from camera

#### **Cause:**

Camera not publishing images properly

## **Solution:**

- 1. Check the camera node running status
- <span id="page-15-2"></span>2. Use ros2 topic hz /camera/color/image\_raw to check publish frequency

# **4.3 ROI Selection Errors**

# **Error 4.3.1: Cannot Select ROI On Empty Frame**

#### **Error Log:**

<span id="page-15-3"></span>Cannot select ROI on empty frame

#### **Cause:**

- No image frame received yet
- Image frame is empty

### **Solution:**

- 1. Wait for the camera to publish images normally before selecting ROI
- 2. Check camera connection
- <span id="page-15-4"></span>3. Confirm the image topic has data

# **Error 4.3.2: Invalid ROI Selected**

#### **Warning Log:**

Invalid ROI selected

- User cancelled ROI selection
- Selected ROI width or height is zero or negative

### **Solution:**

- 1. Re-select a valid ROI region
- 2. Ensure the ROI region has sufficient size (recommended at least 20x20 pixels)
- <span id="page-16-0"></span>3. Fully框选 the target in the image

# **Error 4.3.3: Set Track ROI Failed**

### **Error Log:**

Invalid frame when setting track ROI Failed to Set Track ROI {e.what()}

### **Cause:**

- Image frame is empty
- Tracker initialization异常
- ROI coordinates invalid

### **Solution:**

- 1. Ensure a valid image frame is passed
- 2. Check if ROI coordinates are within the image range
- 3. Verify tracker status
- <span id="page-16-1"></span>4. Re-initialize the tracker

# **Error 4.3.4: Tracking Start Failed**

### **Error Log:**

Failed to start tracking

## **Cause:**

- Current camera frame invalid
- ROI setting failed
- Tracker异常

## **Solution:**

- 1. Confirm camera image is normal
- 2. Check ROI coordinate validity
- <span id="page-16-2"></span>3. Check the specific error log

# **5. General Troubleshooting Suggestions**

# **5.1 Log Level Adjustment**

- <span id="page-17-0"></span>If you encounter issues, enable debug log mode and send the complete error output to technical support
- <span id="page-17-1"></span>ROS log level: ros2 launch xxxx --ros-args --log-level debug

# **5.2 Common Diagnostic Commands**

```
# Check topic list
ros2 topic list
# Check topic data
ros2 topic echo <topic_name>
# Check service list
ros2 service list
# Check Action list
ros2 action list
# Check TF tree
ros2 run tf2_tools view_frames
# Check node status
ros2 node list
# Check logs
ros2 launch xxxx --ros-args --log-level debug
```