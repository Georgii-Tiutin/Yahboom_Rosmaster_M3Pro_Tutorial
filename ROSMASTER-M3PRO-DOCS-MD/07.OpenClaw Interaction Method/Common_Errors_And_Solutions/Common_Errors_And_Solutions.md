# **Common Errors And Solutions**

#### **Common Errors And [Solutions](#page-0-0)**

|  |  | Section 1: multi_brains_pre Package |
|--|--|-------------------------------------|
|  |  |                                     |

1.1 Configuration File [Related Errors](#page-1-1)

<span id="page-0-0"></span>Error [1.1.1: Configuration](#page-1-2) File Not Found

Error [1.1.2: YAML](#page-2-0) Parsing Failed

1.2 ASR Voice Recognition [Related Errors](#page-2-1)

Error 1.2.1: ASR Engine [Initialization](#page-2-2) Failed

Error 1.2.2: Voice [Recognition](#page-2-3) Failed

Error 1.2.3: VAD Engine [Initialization](#page-3-0) Failed

Error 1.2.4: Audio [Stream Open](#page-3-1) Failed

Error 1.2.5: No Speech [Detected](#page-3-2)

Error [1.2.6: Unsupported Language](#page-4-0)

1.3 TTS Voice Synthesis [Related Errors](#page-4-1)

Error 1.3.1: TTS Engine [Initialization](#page-4-2) Failed

Error [1.3.2: Voice](#page-5-0) Synthesis Failed

1.4 Voice [Wake-up Module](#page-5-1) Serial Communication Related Errors

Error [1.4.1: Serial](#page-5-2) Port Open Failed

1.4.2: Serial [Reconnection](#page-5-3) Failed

[1.4.3: Serial](#page-6-0) Send Failed

1.5 ROS [Communication](#page-6-1) Related Errors

Error [1.5.1: Action](#page-6-2) Server Unavailable

Error [1.5.2: Action](#page-6-3) Goal Rejected

1.6 LLM Service [Related Errors](#page-7-0)

Error 1.6.1: Dify [Connection](#page-7-1) Failed

Error [1.6.2: Model](#page-7-2) Request Failed

1.7 Motion Control [Related Errors](#page-8-0)

Error 1.7.1: TF [Transform Acquisition](#page-8-1) Failed

Error 1.7.2: TF [Timestamp Too](#page-8-2) Old

Error [1.7.3: Joint](#page-8-3) Values Not Initialized

1.8 Audio [Playback Related Errors](#page-9-0)

Error [1.8.1: Wake-up Audio](#page-9-1) Load Failed

Section [2: waste\\_classify](#page-9-2) Module

2.1 Model Loading [Related Errors](#page-9-3)

Error [2.1.1: Model](#page-9-4) File Not Found

Error [2.1.2: YOLO Model](#page-9-5) Initialization Error

Error [2.1.3: Model](#page-10-0) Inference Start Failed

2.2 Image Detection [Related Errors](#page-10-1)

Error [2.2.1: Image](#page-10-2) Shape Not Initialized

Error [2.2.2: Image](#page-10-3) Save Failed

Section 3: pcl\_seg Point [Cloud Segmentation](#page-11-0) Module

3.1 Depth Image [Processing](#page-11-1) Errors

Error [3.1.1: Invalid ROI](#page-11-2) Region (Common)

Error [3.1.2: No](#page-11-3) Depth Image

Error 3.1.3: No [Valid Depth](#page-12-0) Points in Circular Region

Error [3.1.4: Target](#page-12-1) Point Outside Image Boundary

Error [3.1.5: Invalid Radius](#page-12-2) Value

3.2 TF [Transform Related Errors](#page-13-0)

Error 3.2.1: TF [Transform Not](#page-13-1) Available

Error 3.2.2: TF [Transform Failed](#page-13-2)

3.3 Point Cloud Processing [Related Warnings](#page-13-3)

Error 3.3.1: ROI Point [Cloud Empty](#page-13-4)

Error [3.3.2: No](#page-14-0) Cluster Found

Error 3.3.3: No [Valid Center](#page-14-1) Data

Section [4: super\\_tracker](#page-14-2) Object Tracking Module

4.1 Tracker [Initialization](#page-15-0) Errors

Error [4.1.1: Tracker](#page-15-1) Creation Failed

Error 4.1.2: Display Window [Configuration](#page-15-2) Conflict

4.2 Image Frame [Processing](#page-15-3) Warnings

Error 4.2.1: Empty or [Invalid Frame](#page-15-4) Received

4.3 ROI [Selection](#page-16-0) Errors

Error [4.3.1: Selecting](#page-16-1) ROI on Empty Frame

Error [4.3.2: Invalid ROI](#page-16-2) Selected

Error [4.3.3: Setting](#page-16-3) Track ROI Failed

Error [4.3.4: Tracking](#page-17-0) Start Failed

Section 5: General [Troubleshooting](#page-17-1) Suggestions

- 5.1 Log Level [Adjustment](#page-17-2)
- 5.2 Common [Diagnostic Commands](#page-17-3)

#### Section 1: multi\_brains\_pre Module

- [1.1 Configuration File Related Errors](#page-1-1)
  - [1.2 ASR Voice Recognition Related Errors](#page-2-1)
  - [1.3 TTS Voice Synthesis Related Errors](#page-4-1)
  - 1.4 Serial Communication Related Errors
  - [1.5 ROS Communication Related Errors](#page-6-1)
  - [1.6 LLM Service Related Errors](#page-7-0)
  - [1.7 Motion Control Related Errors](#page-8-0)
  - [1.8 Audio Playback Related Errors](#page-9-0)
- [Section 2: waste\\_classify Module](#page-9-2)
  - [2.1 Model Loading Related Errors](#page-9-3)
  - [2.2 Image Detection Related Errors](#page-10-1)
- [Section 3: pcl\\_seg Point Cloud Segmentation Module](#page-11-0)
  - [3.1 Depth Image Processing Errors](#page-11-1)
  - [3.2 TF Transform Related Errors](#page-13-0)
  - [3.3 Point Cloud Processing Related Warnings](#page-13-3)
- <span id="page-1-0"></span>[Section 4: super\\_tracker Object Tracking Module](#page-14-2)
  - [4.1 Tracker Initialization Errors](#page-15-0)
  - [4.2 Image Frame Processing Warnings](#page-15-3)
  - [4.3 ROI Selection Errors](#page-16-0)

# **Section 1: multi\_brains\_pre Package**

# **1.1 Configuration File Related Errors**

# **Error 1.1.1: Configuration File Not Found**

#### **Error Log:**

```
multi_brains_pre_setting.yaml file not found, Please check: Whether the file
exists;: {config_file}
```

#### **Cause:**

The multi\_brains\_pre\_setting.yaml configuration file path does not exist

The file was deleted or moved

#### **Solution:**

<span id="page-2-0"></span>1. Copy multi\_brains\_pre\_setting.yaml from the attached source code to the specified directory

## **Error 1.1.2: YAML Parsing Failed**

#### **Error Log:**

multi\_brains\_pre\_setting.yaml file YAML parsing failed: {exc}, Please check: Whether the file format has been modified

#### **Cause:**

YAML file format error (incorrect indentation, special characters not escaped, etc.)

#### **Solution:**

<span id="page-2-2"></span><span id="page-2-1"></span>1. Modify multi\_brains\_pre\_setting.yaml, refer to the factory file format in the attached source code

# **1.2 ASR Voice Recognition Related Errors**

# **Error 1.2.1: ASR Engine Initialization Failed**

#### **Error Log:**

ASR Engine: {model\_name} initialized failed

### **Cause:**

- API Key configuration error or invalid
- Model name not supported
- Network issue (online ASR)
- Key file decryption failed (iFlytek ASR)

#### **Solution:**

- 1. Check if ALIYUN\_API\_KEY is correctly configured
- 2. Confirm the model name being used is in the supported list:
  - paraformer-realtime-v2/v1
  - paraformer-realtime-8k-v2/v1
  - gummy-realtime-v1/gummy-chat-v1
- 3. For iFlytek ASR, check if the key file path and decryption are correct
- <span id="page-2-3"></span>4. Test network connection

### **Error 1.2.2: Voice Recognition Failed**

#### **Error Log:**

asr recognize failure Online ASR recognition failed: {error\_message}

#### **Cause:**

- API invalid
- Online voice recognition service unavailable

#### **Solution:**

- 1. Check network connection stability
- <span id="page-3-0"></span>2. Check if API quota is exhausted

# **Error 1.2.3: VAD Engine Initialization Failed**

#### **Error Log:**

```
VadEngine initialization failed
VadEngine initialization exception: {exc}
```

#### **Cause:**

- VAD model file does not exist
- Model path configuration error
- voice\_toolbox library not installed correctly

#### **Solution:**

- 1. Check if the silero\_vad.int8.onnx model file was deleted
- <span id="page-3-1"></span>2. Download the VAD model file from the attached source code

# **Error 1.2.4: Audio Stream Open Failed**

#### **Error Log:**

```
Audio stream open failed: {exc}
```

#### **Cause:**

- Microphone device not connected
- Audio device occupied by other programs

#### **Solution:**

- 1. Check if the microphone device is properly connected
- 2. Use arecord -l to view available audio devices
- <span id="page-3-2"></span>3. Close other programs occupying the audio device

# **Error 1.2.5: No Speech Detected**

#### **Warning Log:**

```
No speech detected, timeout exit.
```

#### **Cause:**

- Microphone volume too low
- Environment noise too loud

#### **Solution:**

- 1. Increase microphone input volume
- 2. Reduce environment noise
- <span id="page-4-0"></span>3. Speak closer to the microphone

# **Error 1.2.6: Unsupported Language**

#### **Warning Log:**

```
Unsupported language: {language}, only 'zh' and 'en' are supported
```

### **Cause:**

- Configured unsupported language code
- LANGUAGE parameter set incorrectly

### **Solution:**

- 1. Change the LANGUAGE parameter to 'zh' (Chinese) or 'en' (English)
- 2. Check the language setting in the configuration file

<span id="page-4-2"></span><span id="page-4-1"></span>**\$HOME/M3Pro\_ws/src/m3pro\_bringup/config/multi\_brains\_pre\_setting.yaml**

# **1.3 TTS Voice Synthesis Related Errors**

## **Error 1.3.1: TTS Engine Initialization Failed**

#### **Error Log:**

```
Failed to initialize Piper TTS engine: {e}
Failed to initialize Baidu TTS engine: {e}
Tongyi TTS_Engine initialized failed
Baidu TTS_Engine initialized failed
Xunfei TTS_Engine initialized failed
Piper TTS_Engine initialized failed
```

#### **Cause:**

- TTS model file missing
- API Key configuration error
- Configuration file read failed
- Key file decryption failed (iFlytek TTS)

#### **Solution:**

#### 1. **Piper TTS**:

- Check if the model file exists in the ~/MODELS/tts/ directory
- Confirm both .onnx and .onnx.json files exist

#### 2. **Online TTS (Aliyun/Baidu/iFlytek)**:

- Check if the corresponding API Key is correctly configured
- Verify network connection
- 3. Check if the configuration file format is correct

# **Error 1.3.2: Voice Synthesis Failed**

#### **Error Log:**

```
PiperTTS Failed to synthesize text: {e}
Speech synthesis failed. Check whether the TTS model is available
```

#### **Cause:**

- TTS engine not correctly initialized?
- Online voice service unavailable?

#### **Solution:**

- 1. Confirm TTS engine is correctly initialized
- <span id="page-5-1"></span>2. View specific error messages for targeted handling

# **1.4 Voice Wake-up Module Serial Communication Related Errors**

# **Error 1.4.1: Serial Port Open Failed**

### **Error Log:**

```
[kws_mic] Failed to open serial {port}: {e}
Cannot open serial port {port}, please check voice wakeup module connection
```

#### **Cause:**

- Voice wake-up serial device does not exist
- Hardware connection issue

### **Solution:**

- 1. Check if the serial device exists: ls -l /dev/mic
- <span id="page-5-3"></span>2. Check if the hardware connection is secure

# **1.4.2: Serial Reconnection Failed**

#### **Warning Log:**

```
[kws_mic] Max reconnect attempts ({max_attempts}) reached, giving up
[kws_mic] Reconnect attempt {attempt} failed: {e}
```

#### **Cause:**

Hardware device disconnected

#### **Solution:**

1. Re-plug the USB device

# **1.4.3: Serial Send Failed**

#### **Error Log:**

```
send fial: {e}
```

#### **Cause:**

- Serial connection already disconnected
- Buffer overflow
- Voice wake-up device not responding

#### **Solution:**

- 1. Check serial connection status
- 2. Restart the program
- <span id="page-6-2"></span><span id="page-6-1"></span>3. Check if the hardware device is working normally

# **1.5 ROS Communication Related Errors**

# **Error 1.5.1: Action Server Unavailable**

### **Warning Log:**

```
play_audio action server not available, skip wakeup voice
play_audio action server not available, skip error audio
play_audio action server not available, skip voice
```

#### **Cause:**

common\_service node not started

#### **Solution:**

- 1. Confirm the common\_service node is started
- <span id="page-6-3"></span>2. Use ros2 action list to check available actions

# **Error 1.5.2: Action Goal Rejected**

#### **Warning Log:**

```
play_audio goal rejected
TTS play goal rejected
```

#### **Cause:**

Audio file path does not exist

- 1. Check if the audio file exists
- 2. View specific rejection reason logs

# <span id="page-7-0"></span>**1.6 LLM Service Related Errors**

# **Error 1.6.1: Dify Connection Failed**

#### **Error Log:**

```
Dify LLM connection failed, Please check whether DIY dify has been started, API
and BASE_URL settings
Error log: {error_message}
Dify service connection failed: {status_code}
Dify service connection failed: {str(e)}
```

#### **Cause:**

- Dify service not started
- BASE\_URL configuration error
- **API Key invalid** (highest probability, dify application's API does not match DIFY\_API\_KEY in the configuration file)

#### **Solution:**

- 1. Confirm Dify service is started and running normally
- 2. Check DIFY\_BASE\_URL configuration (e.g., [http://localhost/v1\)](http://localhost/v1)
- 3. Verify DIFY\_API\_KEY is correct
- <span id="page-7-2"></span>4. Use curl to test connection: curl -H "Authorization: Bearer {API\_KEY}" {BASE\_URL}/meta

## **Error 1.6.2: Model Request Failed**

#### **Error Log:**

```
The model request failed. Check whether the dify or AI model is normal.
Error Log: {error_message}
```

### **Cause:**

- Dify service exception
- Model service down
- Model api has no quota
- Timeout

- 1. Check Dify service status
- 2. View Dify service logs
- 3. Check api account
- 4. Restart Dify service

# <span id="page-8-0"></span>**1.7 Motion Control Related Errors**

# **Error 1.7.1: TF Transform Acquisition Failed**

#### **Error Log:**

<span id="page-8-1"></span>Failed to get base\_link-roi transform after {max\_attempts} attempts, check if tf\_tree is normal ?

#### **Cause:**

- TF tree incomplete
- pcl\_segment node not publishing TF
- Object tracking lost the target

#### **Solution:**

- 1. Use ros2 run tf2\_tools view\_frames to view TF tree
- <span id="page-8-2"></span>2. Confirm pcl\_segment node is running normally
- 3. Ensure the node is tracking the target

## **Error 1.7.2: TF Timestamp Too Old**

#### **Warning Log:**

tf too old for base\_link-roi: {age:.3f}s ago (attempt {attempt}/{max\_attempts})

#### **Cause:**

- TF publishing frequency too low
- System delay too high, CPU load too high
- Object tracking lost the target

#### **Solution:**

- 1. Increase TF publishing frequency
- 2. Optimize system performance
- 3. Increase tf\_tolerance parameter value
- <span id="page-8-3"></span>4. Close nodes that are not needed

### **Error 1.7.3: Joint Values Not Initialized**

#### **Warning Log:**

Joint1, joint\_2, joint\_4 values not initialized, skipping gaze control.

### **Cause:**

- Robotic arm query service call failed
- Initialization process not completed

- 1. Check if the robotic arm service is working normally
- 2. Verify if the arm\_util node is started

# <span id="page-9-0"></span>**1.8 Audio Playback Related Errors**

## **Error 1.8.1: Wake-up Audio Load Failed**

#### **Error Log:**

<span id="page-9-1"></span>Failed to load the wake-up word audio file :{e}

#### **Cause:**

- Audio file directory does not exist
- File format not supported

#### **Solution:**

- 1. Check system\_vioce/zh/wakeup or system\_vioce/en/wakeup directory
- 2. Confirm WAV file exists and format is correct
- 3. Check file read permissions
- <span id="page-9-3"></span><span id="page-9-2"></span>4. Reinstall the multi\_brains\_pre package

# **Section 2: waste\_classify Module**

# **2.1 Model Loading Related Errors**

# **Error 2.1.1: Model File Not Found**

#### **Error Log:**

```
Model file not found: {model_path}
```

#### **Cause:**

- YOLO model path configuration error
- File deleted or moved

#### **Solution:**

- 1. Check model\_path parameter configuration
- <span id="page-9-5"></span>2. Confirm model file exists
- 3. Re-download the YOLO model file from the attached source code

### **Error 2.1.2: YOLO Model Initialization Error**

#### **Error Log:**

```
YOLO Model initialization error :{e}
```

#### **Cause:**

- Factory system python environment corrupted
- Model file format error

Insufficient memory

#### **Solution:**

- 1. Check if the model file is a valid ONNX format
- 2. Try using CPU mode: set device parameter to "cpu"
- <span id="page-10-0"></span>3. Check if system memory is sufficient

## **Error 2.1.3: Model Inference Start Failed**

#### **Error Log:**

```
Model inference failed to start: {str(e)}
```

#### **Cause:**

- Shared memory creation failed
- Multi-process start failed
- Insufficient resources

#### **Solution:**

- 1. Check system shared memory limit: sysctl kernel.shmmax
- <span id="page-10-2"></span><span id="page-10-1"></span>2. View system logs for detailed error information

# **2.2 Image Detection Related Errors**

# **Error 2.2.1: Image Shape Not Initialized**

#### **Error Log:**

Image shape not initialized, please ensure the camera is running and publishing images

#### **Cause:**

- Camera not started
- Image topic not publishing

## **Solution:**

- 1. Confirm camera node is started
- 2. Check if topic /camera/color/image\_raw has data: ros2 topic echo /camera/color/image\_raw
- <span id="page-10-3"></span>3. Restart the carbase launch file

# **Error 2.2.2: Image Save Failed**

#### **Error Log:**

```
Failed to save image: {e}
```

#### **Cause:**

- Output directory does not exist
- Insufficient disk space
- Camera node not started

#### **Solution:**

<span id="page-11-1"></span><span id="page-11-0"></span>1. Check file path configuration

# **Section 3: pcl\_seg Point Cloud Segmentation Module**

# **3.1 Depth Image Processing Errors**

### **Error 3.1.1: Invalid ROI Region (Common)**

#### **Warning Log:**

<span id="page-11-2"></span>Invalid ROI Region: [umin vmin umax vmax]

#### **Cause:**

- Tracking box coordinates exceed image boundaries
- Tracking box size is zero or negative
- Target area has no depth information

#### **Solution:**

- 1. Check if tracking box coordinates are reasonable
- <span id="page-11-3"></span>2. Use rviz to check if the target has depth information

# **Error 3.1.2: No Depth Image**

#### **Warning Log:**

No depth image received.

#### **Cause:**

- Depth camera not started
- Topic subscription failed
- Depth image not publishing

- 1. Confirm depth camera driver is started
- 2. Check if topic /camera/depth/image\_raw has data
- 3. Verify camera hardware connection
- 4. Restart the camera node

## **Error 3.1.3: No Valid Depth Points in Circular Region**

#### **Warning Log:**

<span id="page-12-0"></span>No valid depth points found in the circular region.

#### **Cause:**

- Target point too far, too close, or no depth information near the target point
- Depth value invalid (0 or exceeding threshold)

#### **Solution:**

- 1. Adjust camera observation angle or target point position
- 2. Check if the depth camera is working normally
- 3. Use rviz to check if the target has depth information
- <span id="page-12-1"></span>4. Reduce ambient lighting

# **Error 3.1.4: Target Point Outside Image Boundary**

#### **Warning Log:**

```
The target point is outside the image boundary. Image size: {width}x{height},
Requested: ({x}, {y})
```

#### **Cause:**

- Requested coordinates exceed image range
- Coordinate calculation error
- Image resolution changed

# **Solution:**

- 1. Verify coordinate calculation logic
- 2. Check image resolution configuration
- 3. Increase boundary checking
- <span id="page-12-2"></span>4. Use valid coordinate values

# **Error 3.1.5: Invalid Radius Value**

## **Warning Log:**

Invalid radius value.

#### **Cause:**

- Radius parameter is negative or zero
- Parameter passing error

- 1. Ensure radius value is positive
- 2. Check service call parameters
- 3. Use reasonable radius values (recommended 5-50 pixels)

# <span id="page-13-0"></span>**3.2 TF Transform Related Errors**

# **Error 3.2.1: TF Transform Not Available**

#### **Warning Log:**

<span id="page-13-1"></span>TF transform not available between base\_link and camera\_color\_optical\_frame.

#### **Error Log:**

```
Failed to lookup transform: {ex.what()}
```

#### **Cause:**

- Missing necessary transforms in TF tree
- Camera coordinate system not configured
- TF publishing node not started

#### **Solution:**

- 1. Use ros2 run tf2\_tools view\_frames to check TF tree
- 2. Ensure camera driver publishes correct TF
- <span id="page-13-2"></span>3. Check if the transform from base\_link to camera is correctly defined

# **Error 3.2.2: TF Transform Failed**

#### **Error Log:**

```
Failed to transform actual_pose: {ex.what()}
Failed to transform estimate_pose: {ex.what()}
Failed to transform point: {ex.what()}
```

### **Cause:**

- Coordinate frame does not exist
- Transform data abnormal
- Timestamp issue

### **Solution:**

- 1. Check if coordinate frame names are correct
- 2. Verify TF data validity
- 3. Check timestamp synchronization
- <span id="page-13-4"></span><span id="page-13-3"></span>4. Use ros2 run tf2\_tools echo to view TF data

# **3.3 Point Cloud Processing Related Warnings**

## **Error 3.3.1: ROI Point Cloud Empty**

#### **Debug Log:**

ROI cloud is empty, skipping this depthframe

#### **Cause:**

- No valid depth values in ROI area
- Distance threshold set too small
- Target exceeds distance range

#### **Solution:**

- 1. Increase distance\_threshold parameter
- 2. Adjust ROI area size
- <span id="page-14-0"></span>3. Ensure target is within effective distance
- 4. Check depth image quality

### **Error 3.3.2: No Cluster Found**

#### **Debug Log:**

No cluster found No suitable cluster found

#### **Cause:**

- Point cloud density insufficient
- Clustering parameter settings improper
- Target too small or too far

### **Solution:**

- 1. Decrease cluster\_min\_size parameter
- 2. Increase cluster\_max\_size parameter
- 3. Adjust ClusterTolerance parameter
- <span id="page-14-1"></span>4. Ensure target is close enough and clear

## **Error 3.3.3: No Valid Center Data**

#### **Warning Log:**

GetBoxCenter: no valid data.

#### **Cause:**

- No depth image processed yet
- Clustering failed

#### **Solution:**

- <span id="page-14-2"></span>1. Ensure depth image is being processed normally
- 2. Check if point cloud segmentation succeeded

# **Section 4: super\_tracker Object Tracking Module**

# **4.1 Tracker Initialization Errors**

# **Error 4.1.1: Tracker Creation Failed**

#### **Error Log:**

<span id="page-15-1"></span><span id="page-15-0"></span>Failed to create tracker: {e.what()}

#### **Cause:**

Model file does not exist

#### **Solution:**

- 1. Check model file path: \$HOME/MODELS/tracker/mixformer\_v2\_sim.onnx
- <span id="page-15-2"></span>2. Adjust num\_threads parameter

# **Error 4.1.2: Display Window Configuration Conflict**

#### **Error Log:**

display\_windows and display\_windows\_only\_track cannot both be true. Setting both to false.

#### **Cause:**

- Both display parameters set to true simultaneously
- Configuration logic conflict

#### **Solution:**

- 1. Enable only one of the parameters:
  - display\_windows : Always display window, support mouse selection
  - display\_windows\_only\_track : Display window only during tracking
- <span id="page-15-4"></span><span id="page-15-3"></span>2. Modify the configuration file to ensure they are not both true

# **4.2 Image Frame Processing Warnings**

### **Error 4.2.1: Empty or Invalid Frame Received**

#### **Warning Log:**

Received empty or invalid frame from camera

### **Cause:**

Camera not properly publishing images

- 1. Check camera node running status
- 2. Use ros2 topic hz /camera/color/image\_raw to check publishing frequency

# **4.3 ROI Selection Errors**

# **Error 4.3.1: Selecting ROI on Empty Frame**

#### **Error Log:**

<span id="page-16-1"></span><span id="page-16-0"></span>Cannot select ROI on empty frame

#### **Cause:**

- No image frame received yet
- Image frame is empty

#### **Solution:**

- 1. Wait for the camera to properly publish images before selecting ROI
- 2. Check camera connection
- <span id="page-16-2"></span>3. Confirm image topic has data

# **Error 4.3.2: Invalid ROI Selected**

#### **Warning Log:**

Invalid ROI selected

#### **Cause:**

- User cancelled ROI selection
- Selected ROI width/height is zero or negative

#### **Solution:**

- 1. Re-select a valid ROI area
- 2. Ensure the ROI area has sufficient size (recommended at least 20x20 pixels)
- <span id="page-16-3"></span>3. Completely frame the target on the image

## **Error 4.3.3: Setting Track ROI Failed**

#### **Error Log:**

Invalid frame when setting track ROI Failed to Set Track ROI {e.what()}

#### **Cause:**

- Image frame is empty
- Tracker initialization exception
- ROI coordinates invalid

- 1. Ensure a valid image frame is passed in
- 2. Check if ROI coordinates are within the image range
- 3. Verify tracker status
- 4. Re-initialize the tracker

# **Error 4.3.4: Tracking Start Failed**

#### **Error Log:**

```
Failed to start tracking
```

#### **Cause:**

- Current camera image invalid
- ROI setting failed
- Tracker exception

#### **Solution:**

- 1. Confirm camera image is normal
- 2. Check ROI coordinate validity
- <span id="page-17-1"></span>3. View specific error logs

# **Section 5: General Troubleshooting Suggestions**

# **5.1 Log Level Adjustment**

- <span id="page-17-2"></span>If you encounter problems, enable debug log mode and send the complete error content to technical support
- <span id="page-17-3"></span>ROS log level: ros2 launch xxxx --ros-args --log-level debug

# **5.2 Common Diagnostic Commands**

```
# View topic list
ros2 topic list
# View topic data
ros2 topic echo <topic_name>
# View service list
ros2 service list
# View Action list
ros2 action list
# View TF tree
ros2 run tf2_tools view_frames
# Check node status
ros2 node list
# View logs
ros2 launch xxxx --ros-args --log-level debug
```