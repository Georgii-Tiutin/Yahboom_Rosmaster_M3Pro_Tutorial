# **Common Error Summary and Solutions Documentation**

#### I. multi\_brains\_pre Module

- [1.1 Configuration File Related Errors](#page-0-0)
- 1.2 ASR Speech Recognition Related Errors
- 1.3 TTS Speech Synthesis Related Errors
- 1.4 Serial Communication Related Errors
- [1.5 ROS Communication Related Errors](#page-5-0)
- 1.6 Large Model Service Related Errors
- 1.7 Motion Control Related Errors
- [1.8 Audio Playback Related Errors](#page-8-0)
- [II. waste\\_classify Module](#page-8-1) 2.1 Model Loading Related Errors
- 2.2 Image Detection Related Errors
- [III. pcl\\_seg Point Cloud Segmentation Module](#page-10-0)
- [3.1 Depth Image Processing Errors](#page-10-1)
- [3.2 TF Transform Related Errors](#page-12-0)
- [3.3 Point Cloud Processing Related Warnings](#page-12-1)
- [IV. super\\_tracker Target Tracking Module](#page-13-0)
- [4.1 Tracker Initialization Errors](#page-14-0)
- [4.2 Image Frame Processing Warnings](#page-14-1)
- <span id="page-0-0"></span>[4.3 ROI Selection Errors](#page-15-0)

# **I. multi\_brains\_pre Package**

## **1.1 Configuration File Related Errors**

## **Error 1.1.1: Configuration file not found**

#### **Error Log:**

multi\_brains\_pre\_setting.yaml file not found, Please check: Whether the file exists: {config\_file}

## **Cause:**

- The path for the multi\_brains\_pre\_setting.yaml configuration file does not exist.
- The file has been deleted or moved.

### **Solution:**

1. Copy multi\_brains\_pre\_setting.yaml from the attached source code files to the specified directory.

## **Error 1.1.2: YAML Parsing Failed**

#### **Error Log:**

multi\_brains\_pre\_setting.yaml file YAML parsing failed: {exc}, Please check: Whether the file format has been modified

#### **Cause:**

Incorrect YAML file format (e.g., incorrect indentation, unescaped special characters).

#### **Solution:**

1. Modify multi\_brains\_pre\_setting.yaml , referencing the default file format found in the attached source code files.

## **1.2 ASR Speech Recognition Errors**

## **Error 1.2.1: ASR Engine Initialization Failed**

#### **Error Log:**

ASR Engine: {model\_name} initialized failed

#### **Cause:**

- Incorrect or invalid API Key configuration.
- Unsupported model name.
- Network issues (for online ASR services).
- Key file decryption failed (for iFlytek ASR).

#### **Solution:**

- 1. Check if ALIYUN\_API\_KEY is configured correctly.
- 2. Verify that the model name being used is included in the supported list:
- paraformer-realtime-v2/v1
- paraformer-realtime-8k-v2/v1
- gummy-realtime-v1/gummy-chat-v1
- 3. For iFlytek ASR, check if the key file path and decryption settings are correct.
- 4. Test your network connection.

## **Error 1.2.2: Speech Recognition Failed**

#### **Error Log:**

```
asr recognize failure
Online ASR recognition failed: {error_message}
```

- Invalid or expired API Key.
- The online speech recognition service is currently unavailable.

#### **Solution:**

- 1. Check the stability of your network connection.
- 2. Check if your API usage quota has been exhausted.

## **Error 1.2.3: VAD Engine Initialization Failed**

#### **Error Log:**

```
VadEngine initialization failed
VadEngine initialization exception: {exc}
```

### **Cause:**

- The VAD model file does not exist.
- The model path is configured incorrectly.
- The voice\_toolbox library was not installed correctly.

#### **Solution:**

- 1. Check if the silero\_vad.int8.onnx model file has been deleted.
- 2. Download the VAD model file from the attached source code.

## **Error 1.2.4: Audio Stream Open Failed**

#### **Error Log:**

```
Audio stream open failed: {exc}
```

#### **Cause:**

- The microphone device is not connected.
- The audio device is currently in use by another program.

#### **Solution:**

- 1. Check if the microphone device is connected correctly.
- 2. Use arecord -l to list available audio devices.
- 3. Close any other programs that are currently using the audio device.

### **Error 1.2.5: No Speech Detected**

## **Warning Log:**

```
No speech detected, timeout exit.
```

#### **Cause:**

- Microphone volume is too low.
- Ambient noise is excessive.

- 1. Increase the microphone input volume.
- 2. Reduce ambient noise.

## **Error 1.2.6: Unsupported Language**

#### **Warning Log:**

```
Unsupported language: {language}, only 'zh' and 'en' are supported
```

#### **Cause:**

- An unsupported language code was configured.
- The LANGUAGE parameter is set incorrectly.

#### **Solution:**

- 1. Change the LANGUAGE parameter to 'zh' (Chinese) or 'en' (English).
- 2. Check the language settings within the configuration file:

**\$HOME/M3Pro\_ws/src/m3pro\_bringup/config/multi\_brains\_pre\_setting.yaml**

## **1.3 TTS (Text-to-Speech) Related Errors**

### **Error 1.3.1: TTS Engine Initialization Failed**

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

- TTS model files are missing.
- API Key is configured incorrectly.
- Configuration file failed to load.
- Key file decryption failed (Xunfei TTS).

#### **Solution:**

#### 1. **Piper TTS:**

- Check if the model files exist in the ~/MODELS/tts/ directory.
- Confirm that both the .onnx and .onnx.json files are present.

#### 2. **Online TTS (Alibaba Cloud/Baidu/Xunfei):**

- Check if the corresponding API Key is configured correctly.
- Verify the network connection.
- 3. Check if the configuration file format is correct.

## **Error 1.3.2: Speech Synthesis Failed**

#### **Error Log:**

```
PiperTTS Failed to synthesize text: {e}
Speech synthesis failed. Check whether the TTS model is available.
```

#### **Cause:**

- The TTS engine was not initialized correctly?
- The online speech service is unavailable?

#### **Solution:**

- 1. Verify that the TTS engine has been initialized correctly.
- 2. Review the specific error message to take targeted corrective actions.

# **1.4 Errors Related to Serial Communication in the Voice Wakeup Module**

## **Error 1.4.1: Failed to Open Serial Port**

#### **Error Log:**

```
[kws_mic] Failed to open serial {port}: {e}
Cannot open serial port {port}, please check voice wakeup module connection
```

#### **Cause:**

- The serial device for the voice wakeup module does not exist.
- Hardware connection issues.

### **Solution:**

- 1. Check if the serial device exists: ls -l /dev/mic
- 2. Verify that the hardware connections are secure.

## **1.4.2: Serial Port Reconnection Failure**

#### **Warning Logs:**

```
[kws_mic] Max reconnect attempts ({max_attempts}) reached, giving up
[kws_mic] Reconnect attempt {attempt} failed: {e}
```

#### **Cause:**

The hardware device has disconnected.

#### **Solution:**

1. Reconnect (unplug and replug) the USB device.

## **1.4.3: Serial Port Transmission Failure**

#### **Error Logs:**

```
send fial: {e}
```

#### **Cause:**

- The serial port connection has been severed.
- Buffer overflow.
- The voice wake-up device is unresponsive.

#### **Solution:**

- 1. Check the status of the serial port connection.
- 2. Restart the program.
- <span id="page-5-0"></span>3. Verify that the hardware device is functioning correctly.

## **1.5 ROS Communication-Related Errors**

## **Error 1.5.1: Action Server Unavailable**

### **Warning Logs:**

```
play_audio action server not available, skip wakeup voice
play_audio action server not available, skip error audio
play_audio action server not available, skip voice
```

#### **Cause:**

The common\_service node has not been started.

#### **Solution:**

- 1. Confirm that the common\_service node is running.
- 2. Use ros2 action list to check for available actions.

### **Error 1.5.2: Action Goal Rejected**

#### **Warning Logs:**

```
play_audio goal rejected
TTS play goal rejected
```

## **Cause:**

The specified audio file path does not exist.

- 1. Verify the existence of the audio file.
- 2. Check the logs for the specific reason why the goal was rejected.

## **1.6 Large Language Model (LLM) Service-Related Errors**

## **Error 1.6.1: Dify Connection Failure**

#### **Error Logs:**

```
Dify LLM connection failed, Please check whether DIY dify has been started, API
and BASE_URL settings
Error log: {error_message}
Dify service connection failed: {status_code}
Dify service connection failed: {str(e)}
```

#### **Cause:**

- The Dify service has not been started.
- BASE\_URL Configuration Error
- **Invalid API Key** (Most frequent cause: The API Key used in the Dify application does not match the DIFY\_API\_KEY specified in the configuration file.)

#### **Solution:**

- 1. Confirm that the Dify service has started and is running normally.
- 2. Verify the DIFY\_BASE\_URL configuration (e.g., http://localhost/v1 ).
- 3. Verify that the DIFY\_API\_KEY is correct.
- 4. Test the connection using curl : curl -H "Authorization: Bearer {API\_KEY}" {BASE\_URL}/meta

## **Error 1.6.2: Model Request Failed**

#### **Error Log:**

```
The model request failed. Check whether the dify or AI model is normal.
Error Log: {error_message}
```

#### **Causes:**

- Dify service anomaly
- Model service outage
- Insufficient API credits for the model
- Request timeout

- 1. Check the status of the Dify service.
- 2. Review the Dify service logs.
- 3. Check the API account status.
- 4. Restart the Dify service.

## **1.7 Action Control-Related Errors**

## **Error 1.7.1: TF Transform Retrieval Failed**

#### **Error Log:**

Failed to get base\_link-roi transform after {max\_attempts} attempts; check if the TF tree is normal?

#### **Cause:**

- The TF tree is incomplete.
- The pcl\_segment node is not publishing TF data.
- The target tracking module has lost the target.

#### **Solution:**

- 1. Use ros2 run tf2\_tools view\_frames to visualize the TF tree.
- 2. Verify that the pcl\_segment node is running correctly.
- 3. Ensure that the node is actively tracking a target.

## **Error 1.7.2: TF Timestamp Too Old**

#### **Warning Log:**

tf too old for base\_link-roi: {age:.3f}s ago (attempt {attempt}/{max\_attempts})

#### **Cause:**

- The TF publishing frequency is too low.
- System latency is too high, or CPU load is excessive.
- The target tracking module has lost the target.

## **Solution:**

- 1. Increase the TF publishing frequency.
- 2. Optimize system performance.
- 3. Increase the value of the tf\_tolerance parameter.
- 4. Shut down unnecessary nodes.

## **Error 1.7.3: Joint Values Uninitialized**

#### **Warning Log:**

Joint1, joint\_2, joint\_4 values not initialized; skipping gaze control.

#### **Cause:**

- The robotic arm query service call failed.
- The initialization process was not completed.

- 1. Check if the robotic arm service is functioning correctly.
- 2. Verify that the arm\_util node has started.

## <span id="page-8-0"></span>**1.8 Audio Playback-Related Errors**

## **Error 1.8.1: Wake-up Audio Loading Failed**

#### **Error Log:**

```
Failed to load the wake-up word audio file: {e}
```

#### **Cause:**

- The audio file directory does not exist.
- The file format is not supported.

#### **Solution:**

- 1. Check the system\_voice/zh/wakeup or system\_voice/en/wakeup directory.
- 2. 3. Verify that the WAV file exists and is in the correct format.
- <span id="page-8-1"></span>3. Reinstall the multi\_brains\_pre package.

# **II.** waste\_classify **Module**

## **2.1 Model Loading Errors**

## **Error 2.1.1: Model File Not Found**

#### **Error Log:**

```
Model file not found: {model_path}
```

### **Cause:**

- Incorrect configuration of the YOLO model path.
- The file has been deleted or moved.

## **Solution:**

- 1. Check the configuration of the model\_path parameter.
- 2. Verify that the model file exists.
- 3. Re-download the YOLO model file from the attached source code.

### **Error 2.1.2: YOLO Model Initialization Error**

#### **Error Log:**

```
YOLO Model initialization error: {e}
```

- The factory-default Python environment has been corrupted.
- Incorrect model file format.
- Insufficient memory.

#### **Solution:**

- 1. Verify that the model file is in a valid ONNX format.
- 2. Attempt to use CPU mode: Set the device parameter to "cpu".
- 3. Check if the system has sufficient memory.

## **Error 2.1.3: Model Inference Startup Failure**

#### **Error Log:**

```
Model inference failed to start: {str(e)}
```

#### **Cause:**

- Shared memory creation failed.
- Multiprocessing startup failed.
- Insufficient resources.

#### **Solution:**

- 1. Check the system's shared memory limits: sysctl kernel.shmmax .
- 2. Check the system logs for detailed error information.

## **2.2 Image Detection Errors**

## **Error 2.2.1: Image Shape Not Initialized**

#### **Error Log:**

Image shape not initialized; please ensure the camera is running and publishing images.

#### **Cause:**

- The camera has not started.
- The image topic is not being published.

## **Solution:**

- 1. Verify that the camera node has started.
- 2. Check if the topic /camera/color/image\_raw contains data: ros2 topic echo /camera/color/image\_raw .
- 3. Restart the CarBase launch file

## **Error 2.2.2: Image Save Failed**

#### **Error Log:**

```
Failed to save image: {e}
```

- The output directory does not exist.
- Insufficient disk space.

The camera node has not started.

#### **Solution:**

<span id="page-10-1"></span><span id="page-10-0"></span>1. Check the file path configuration.

# **III. pcl\_seg Point Cloud Segmentation Module**

## **3.1 Depth Image Processing Errors**

## **Error 3.1.1: Invalid ROI Region (Common)**

#### **Warning Log:**

Invalid ROI Region: [umin vmin umax vmax]

#### **Cause:**

- Tracking box coordinates exceed image boundaries
- Tracking box dimensions are zero or negative
- The target region lacks depth information

#### **Solution:**

- 1. Check if the tracking box coordinates are valid/reasonable
- 2. Use RViz to verify whether depth information exists for the target

### **Error 3.1.2: No Depth Image**

#### **Warning Log:**

No depth image received.

#### **Cause:**

- The depth camera has not been started
- Topic subscription failed
- The depth image is not being published

#### **Solution:**

- 1. Confirm that the depth camera driver has been started
- 2. Check if the topic /camera/depth/image\_raw contains data
- 3. Verify the camera hardware connections
- 4. Restart the camera node

## **Error 3.1.3: No Valid Depth Points in Circular Region**

#### **Warning Log:**

No valid depth points found in the circular region.

- The target point is too far or too close; there is no depth information in the vicinity of the target point
- Depth values are invalid (0 or exceed the defined threshold)

#### **Solution:**

- 1. Adjust the camera's viewing angle or the position of the target point
- 2. Check if the depth camera is functioning correctly
- 3. Use RViz to verify whether depth information exists for the target
- 4. Reduce ambient lighting

## **Error 3.1.4: Target Point Outside Image Boundaries**

### **Warning Log:**

```
The target point is outside the image boundary. Image size: {width}x{height},
Requested: ({x}, {y})
```

#### **Cause:**

- The requested coordinates fall outside the image range
- Coordinate calculation error
- Image resolution has changed

#### **Solution:**

- 1. Verify the coordinate calculation logic
- 2. Check the image resolution configuration
- 3. Implement boundary checks
- 4. Use valid coordinate values

## **Error 3.1.5: Invalid Radius Value**

#### **Warning Log:**

Invalid radius value.

### **Cause:**

- The radius parameter is negative or zero.
- Parameter passing error.

- 1. Ensure the radius value is a positive number.
- 2. Check the service call parameters.
- 3. Use a reasonable radius value (5–50 pixels recommended).

## <span id="page-12-0"></span>**3.2 TF Transform-Related Errors**

## **Error 3.2.1: TF Transform Unavailable**

#### **Warning Log:**

TF transform not available between base\_link and camera\_color\_optical\_frame.

#### **Error Log:**

```
Failed to lookup transform: {ex.what()}
```

#### **Cause:**

- Necessary transforms are missing from the TF tree.
- The camera coordinate frame has not been configured.
- The TF publishing node has not been started.

#### **Solution:**

- 1. Use ros2 run tf2\_tools view\_frames to inspect the TF tree.
- 2. Ensure that the camera driver is publishing the correct TF transforms.
- 3. Verify that the transform from base\_link to the camera is correctly defined.

## **Error 3.2.2: TF Transform Failed**

#### **Error Log:**

```
Failed to transform actual_pose: {ex.what()}
Failed to transform estimate_pose: {ex.what()}
Failed to transform point: {ex.what()}
```

## **Cause:**

- The specified coordinate frame does not exist.
- The transform data is invalid or corrupted.
- Timestamp synchronization issues.

## **Solution:**

- 1. Verify that the coordinate frame names are correct.
- 2. Validate the integrity of the TF data.
- 3. Check for timestamp synchronization issues.
- <span id="page-12-1"></span>4. Use ros2 run tf2\_tools echo to inspect the TF data.

## **3.3 Point Cloud Processing-Related Warnings**

## **Error 3.3.1: ROI Point Cloud is Empty**

#### **Debug Log:**

ROI cloud is empty, skipping this depthframe

#### **Cause:**

- There are no valid depth values within the specified ROI region.
- The distance threshold parameter is set too low.
- The target object is outside the valid distance range.

#### **Solution:**

- 1. Increase the distance\_threshold parameter.
- 2. Adjust the size of the ROI region.
- 3. Ensure that the target object is within the valid distance range.
- 4. Check the quality of the depth image data.

### **Error 3.3.2: No Cluster Found**

#### **Debug Log:**

```
No cluster found
No suitable cluster found
```

#### **Cause:**

- The point cloud density is insufficient.
- Clustering parameters have been configured incorrectly.
- Target is too small or too distant

#### **Solution:**

- 1. Decrease the cluster\_min\_size parameter.
- 2. Increase the cluster\_max\_size parameter.
- 3. Adjust the ClusterTolerance parameter.
- 4. Ensure the target is sufficiently close and clearly visible.

## **Error 3.3.3: No Valid Center Data**

#### **Warning Log:**

GetBoxCenter: no valid data.

#### **Cause:**

- Depth images have not yet been processed.
- Clustering failed.

## **Solution:**

- 1. Ensure that depth images are being processed correctly.
- <span id="page-13-0"></span>2. Check if point cloud segmentation was successful.

# **IV. super\_tracker Target Tracking Module**

## <span id="page-14-0"></span>**4.1 Tracker Initialization Errors**

## **Error 4.1.1: Tracker Creation Failed**

#### **Error Log:**

Failed to create tracker: {e.what()}

#### **Cause:**

The model file does not exist.

#### **Solution:**

- 1. Check the model file path: \$HOME/MODELS/tracker/mixformer\_v2\_sim.onnx
- 2. Adjust the num\_threads parameter.

### **Error 4.1.2: Display Window Configuration Conflict**

#### **Error Log:**

display\_windows and display\_windows\_only\_track cannot both be true. Setting both to false.

#### **Cause:**

- Both display parameters were set to true simultaneously.
- Configuration logic conflict.

### **Solution:**

- 1. Enable only one of the parameters:
- display\_windows : Always display the window; supports mouse selection.
- display\_windows\_only\_track : Display the window only when tracking.
- <span id="page-14-1"></span>2. Modify the configuration file to ensure that both are not set to true at the same time.

## **4.2 Image Frame Processing Warnings**

## **Error 4.2.1: Received Empty or Invalid Frame**

#### **Warning Log:**

Received empty or invalid frame from camera

#### **Cause:**

The camera is not publishing images correctly.

- 1. Check the running status of the camera node.
- 2. Use ros2 topic hz Check the publishing frequency of /camera/color/image\_raw

## <span id="page-15-0"></span>**4.3 ROI Selection Errors**

## **Error 4.3.1: Selecting ROI on an Empty Frame**

#### **Error Log:**

Cannot select ROI on empty frame

#### **Cause:**

- No image frames have been received yet.
- The image frame is empty.

#### **Solution:**

- 1. Wait for the camera to publish images normally before selecting the ROI.
- 2. Check the camera connection.
- 3. Verify that the image topic contains data.

### **Error 4.3.2: Invalid ROI Selection**

#### **Warning Log:**

Invalid ROI selected

#### **Cause:**

- The user cancelled the ROI selection.
- The selected ROI has zero or negative width/height dimensions.

## **Solution:**

- 1. Re-select a valid ROI area.
- 2. Ensure the ROI area has sufficient dimensions (a minimum of 20x20 pixels is recommended).
- 3. Enclose the target completely within the bounding box on the image.

## **Error 4.3.3: Failed to Set Tracking ROI**

#### **Error Log:**

Invalid frame when setting track ROI Failed to Set Track ROI {e.what()}

### **Cause:**

- The image frame is empty.
- The tracker initialization failed or encountered an exception.
- The ROI coordinates are invalid.

- 1. Ensure that a valid image frame is provided.
- 2. Check if the ROI coordinates fall within the image boundaries.
- 3. Verify the status of the tracker.

## **Error 4.3.4: Tracking Startup Failed**

#### **Error Log:**

```
Failed to start tracking
```

#### **Cause:**

- The current camera frame is invalid.
- The ROI setting failed.
- The tracker encountered an exception.

#### **Solution:**

- 1. Confirm that the camera image is normal.
- 2. Check the validity of the ROI coordinates.
- 3. Review the specific error logs for details.

# **V. General Troubleshooting Suggestions**

## **5.1 Adjusting Log Levels**

- If you encounter an issue, enable debug logging mode and send the complete error output to technical support.
- ROS Log Level: ros2 launch xxxx --ros-args --log-level debug

## **5.2 Common Diagnostic Commands**

```
# View list of topics
ros2 topic list
# View topic data
ros2 topic echo <topic_name>
# View list of services
ros2 service list
# View list of Actions
ros2 action list
# View TF tree
ros2 run tf2_tools view_frames
# Check node status
ros2 node list
# View logs
ros2 launch xxxx --ros-args --log-level debug
```