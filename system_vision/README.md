## 💻 **Software Architecture** <a id="software-architecture"></a>

Our software implementation employs a distributed processing architecture that optimizes performance through specialized task allocation between multiple processors.

### **System Architecture Overview**

<table>
<tr>
<td width="60%">

**Processing Distribution**:
- **Vision Processing Unit**: Raspberry Pi 4 handling real-time image analysis and high-level decision making
- **Sensor Fusion Unit**: esp32 managing multi-sensor data acquisition and preprocessing
- **Communication Bridge**: Bidirectional UART protocol at 115200 baud for inter-processor data exchange

**Core Software Components**:
- [`vision_source.py`](src/open.py) - Open challenge navigation algorithms and obstacle challenge with integrated parking
- [`calibration.py`](src/obstacle.py) - calibration for the different variables  
- [`esp32_car.ino`](src/uart_slave.ino) - Sensor and motor management firmware

</td>
<td width="40%">
<img src="src/1788558229643_image.png" alt="Software Development Environment" width="100%">
<p align="center"><em>Integrated development and testing setup</em></p>
</td>
</tr>
</table>

### 📄 **Development Environment & Code Deployment**

#### **Raspberry Pi 4 Model B (Camera Microcontroller)**
- **Programming Language**: Python 3 for rapid development and testing
- **Development Interface**: Direct micro USB / HDMI connection to Raspberry Pi with a live OpenCV debug window (`cv.imshow`)
- **Core Libraries**:
  - `opencv-python (cv2)` - Image preprocessing, HSV color masking, and contour-based object detection
  - `numpy` - Array operations for HSV bounds and morphological kernels
  - `pyserial` - UART serial communication with the ESP32 microcontroller

#### **esp32 (Sensor and Motor Microcontroller)**
- **Programming Language**: Arduino C++ for efficient sensor and motor data handling
- **Development Interface**: Standard micro USB connection to evaluation board
- **Essential Libraries**:
  - `ESP32Servo.h` - PWM-based control of the steering servo
- **Communication Protocol**: UART Serial (115200 baud) between the Raspberry Pi and ESP32, used to relay vision-based obstacle data (color, distance, position)

#### **Development Workflow Optimization**
We implemented magnetic USB connectors for the camera microcontroller, providing significant advantages during intensive development cycles. The magnetic interface enables rapid connection changes, prevents physical port damage from repeated use, and streamlines the programming and debugging process.

#### **Code Deployment Process**

1. **Raspberry Pi 4 Model B Python Deployment**:
   - Transfer `.py` source files directly to microcontroller filesystem using magnetic USB connection
   - Automatic execution initialization from `vision_source.py` on system startup
   - Adding the calibration code in order to adjust the variables
   - No compilation overhead - immediate interpreted execution for rapid iteration

2. **esp32 Arduino Deployment**:
   - Compile source code in Arduino IDE with ESP32 board package support
   - Upload compiled binary via micro USB interface to evaluation board
   - Precompiled firmware deployment ensuring reliable sensor and motor operation

### 🎨 **Vision Processing Strategy**
We selected the **HSV color space** for its superior performance under variable lighting conditions compared to traditional RGB representation. Detection thresholds for the red and green obstacle pillars, as well as the white track floor, were manually calibrated and fine-tuned per venue using a dedicated debug mask window.

**Technical Rationale**: HSV colorspace provides adequate performance for our application requirements, isolating hue independently from brightness/lighting variance, while more complex approaches (e.g. machine learning-based detection) would introduce unnecessary computational overhead without significant benefits for this specific use case.

**Calibration Debug Windows**:

<table>
<tr>
<td width="50%">
<img src="src/1788558162827_image.png" alt="Green Mask Calibration" width="100%">
<p align="center"><em>Green mask calibration window</em></p>
</td>
<td width="50%">
<img src="src/1788558165154_image.png" alt="Red Mask Calibration" width="100%">
<p align="center"><em>Red mask calibration window</em></p>
</td>
</tr>
</table>

<div align="center">
<img src="src/hard_light_condition_tests.jpg" alt="Environmental Testing Validation" width="600">
<p><em>Comprehensive testing under challenging lighting conditions including direct sunlight exposure</em></p>
</div>

### 🧭 **Navigation Algorithm Implementation**

#### **Obstacle Challenge Navigation**

**State Machine Flow**:

Vision Obstacle Avoidance → Clearance → Corner Turn → Wall Following (repeat)
↑ ↑ ↑ ↑
Camera Color Post-Obstacle Ultrasonic Ultrasonic
Detection (R/G) Stabilizing Front Distance Left/Right PID


**Navigation Pseudocode**:

INITIALIZE sensors, center steering, stop motor

LOOP:
READ ultrasonic distances (front, left, right)
READ vision data from camera (color, distance, x-position)

IF obstacle color == RED and distance within range:
    STEER hard RIGHT, drive at obstacle speed
    CONTINUE to next loop

IF obstacle color == GREEN and distance within range:
    STEER hard LEFT, drive at obstacle speed
    CONTINUE to next loop

IF recently cleared an obstacle (within clearance window):
    CENTER steering, drive at clearance speed
    CONTINUE to next loop

IF currently turning a corner:
    CONTINUE steering toward corner direction
    IF front distance becomes clear OR max corner time exceeded:
        END corner, center steering
    CONTINUE to next loop

IF front distance

**Color-Specific Behaviors**:
- **Red Object Detection**: Right-side bias navigation with maintained offset
- **Green Object Detection**: Left-side bias navigation with maintained offset  
- **Position Maintenance**: Consistent pixel positioning for smooth obstacle tracking

<table>
<tr>
<td width="50%">
<img src="src/1788558167694_image.png" alt="Red Obstacle Detection Example" width="100%">
<p align="center"><em>Live red obstacle detection with bounding box</em></p>
</td>
<td width="50%">
<img src="src/1788558170273_image.png" alt="Green Obstacle Detection Example" width="100%">
<p align="center"><em>Live green obstacle detection during track navigation</em></p>
</td>
</tr>
</table>

### **Sensor and motor Fusion Implementation**

**Data Integration Pipeline**:
```
esp32 Sensors ←→  UART  ←→ Raspberry Pi 4 Model B → Sensor Fusion → Control Decisions
     ↑                            ↑                   ↑               ↓
  ToF Left                      Camera           PID Controller   Motor/Servo
  ToF Right                     Vision           State Machine     Actuators
 Encoder Data                  IMU Data
                               ToF Front
```

### **Control System Implementation**

**Steering Control Algorithm**:
```python
# Proportional controller implementation for smooth navigation
def calculate_steering_correction(target_cx, frame_center_x):
    error = target_cx - frame_center_x
    steering_angle = error * KP_GAIN
    steering_angle = clamp(steering_angle, -0.5, 0.5)
    return steering_angle
```

### **Inter-Processor Communication**

**UART Protocol Specification**:
- **Baud Rate**: 115200 for reliable data throughput
- **Command Structure**: Comma-separated plain-text messages terminated by newline
- **Data Validation**: Field-count check (color, distance, x-position) before parsing
- **Error Recovery**: Timeout-based fallback - if no valid message is received within the timeout window, the obstacle state automatically resets to "none detected"

**Master (Raspberry Pi 4) → Slave (ESP32) Messages**:
- `R,<distance>,<x_position>` - Red obstacle detected: distance in cm, horizontal pixel position
- `G,<distance>,<x_position>` - Green obstacle detected: distance in cm, horizontal pixel position
- `N` - No obstacle currently detected
**Slave Response Formats**:
- **All sensors**: `left_distance,right_distance,encoder_distance\n`
- **Left ToF only**: `left_distance\n`
- **Right ToF only**: `right_distance\n`
- **Encoder only**: `encoder_distance\n`