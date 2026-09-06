## 💻 **Software Architecture** <a id="software-architecture"></a>

Our software implementation employs a distributed processing architecture that optimizes performance through specialized task allocation between multiple processors. This documentation was last updated on **[september]**.

### **System Architecture Overview**

<table>
<tr>
<td width="60%">

**Processing Distribution**:
- **Vision & Navigation Unit**: Raspberry Pi 4 handling real-time image analysis, obstacle-color detection, lane tracking, and parking-marker detection
- **Sensor & Motor Control Unit**: ESP32 running its own onboard state machine (obstacle avoidance → clearance → corner turn → wall following) using its own ultrasonic sensors, while accepting vision-based overrides from the Raspberry Pi over UART
- **Communication Bridge**: One-directional UART protocol at 115200 baud, Raspberry Pi → ESP32, carrying vision detection results as plain-text messages

**Core Software Components**:
- [`vision_navigation.py`](vision_navigation.py) - Obstacle Challenge: real-time HSV-based detection of red/green obstacle pillars, the white track lane, and magenta parking markers, plus proportional steering-correction calculation
- [`final.py`](final.py) - Open Challenge: area-based wall following (dual ROI strips) + orange-line turn counting, actively transmits `A` messages over UART
- [`esp32_car.ino`](esp32_car.ino) - Onboard motor/servo control, ultrasonic wall-following and corner-turning state machine, and UART parser for vision messages

Only one of the two vision scripts (`vision_navigation.py` or `final.py`) runs on the Raspberry Pi at a time, matching the challenge currently being run.

</td>
<td width="40%">
<img src="1788558229643_image.png" alt="Software Development Environment" width="100%">
<p align="center"><em>Integrated development and testing setup</em></p>
</td>
</tr>
</table>

### 📄 **Development Environment & Code Deployment**

#### **Raspberry Pi 4 Model B (Vision Microcontroller)**
- **Programming Language**: Python 3 for rapid development and testing
- **Development Interface**: Direct micro USB / HDMI connection to Raspberry Pi with a live OpenCV debug window (`cv.imshow`)
- **Core Libraries**:
  - `opencv-python (cv2)` - Image preprocessing, HSV color masking, and contour-based object detection
  - `numpy` - Array operations for HSV bounds and morphological kernels
  - `pyserial` - UART serial communication with the ESP32 microcontroller

#### **ESP32 (Sensor and Motor Microcontroller)**
- **Programming Language**: Arduino C++ for efficient sensor and motor data handling
- **Development Interface**: Standard micro USB connection to evaluation board
- **Essential Libraries**:
  - `ESP32Servo.h` - PWM-based control of the steering servo
- **Communication Protocol**: One-directional UART Serial (115200 baud), Raspberry Pi → ESP32, used to relay vision-based obstacle/lane/parking data

#### **Development Workflow Optimization**
We implemented magnetic USB connectors for the vision microcontroller, providing significant advantages during intensive development cycles. The magnetic interface enables rapid connection changes, prevents physical port damage from repeated use, and streamlines the programming and debugging process.

#### **Code Deployment Process**

1. **Raspberry Pi 4 Model B Python Deployment**:
   - Transfer `.py` source files directly to the microcontroller filesystem using the magnetic USB connection
   - No compilation overhead — immediate interpreted execution for rapid iteration

2. **ESP32 Arduino Deployment**:
   - Compile source code in Arduino IDE with ESP32 board package support
   - Upload compiled binary via micro USB interface to evaluation board
   - Precompiled firmware deployment ensuring reliable sensor and motor operation

### 🎨 **Vision Processing Strategy**
We selected the **HSV color space** for its superior performance under variable lighting conditions compared to traditional RGB representation. Detection thresholds for the red and green obstacle pillars, the white track floor, and the magenta parking markers were manually calibrated and fine-tuned per venue using a dedicated debug mask window (see the `colors` folder for the standalone calibration workflow).

**Technical Rationale**: HSV colorspace provides adequate performance for our application requirements, isolating hue independently from brightness/lighting variance, while more complex approaches (e.g. machine learning-based detection) would introduce unnecessary computational overhead without significant benefits for this specific use case.

**Detected Targets**:
- **Red / Green pillars**: Dual-range red mask + single-range green mask, filtered by area and solidity
- **White track floor (lane)**: Restricted to the bottom half of the frame, used to compute the drivable corridor's centroid when no obstacle is in view
- **Magenta parking markers**: Detected independently every frame regardless of driving state; used to calculate the parking-gap center and width once two markers are visible

**Parking Marker Detection Snippet**:
```python
magenta_mask = cv.inRange(hsv, lower_magenta, upper_magenta)
magenta_contours, _ = cv.findContours(magenta_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

marker_centers = []
for cnt in magenta_contours:
    if cv.contourArea(cnt) > 150:
        mx, my, mw, mh = cv.boundingRect(cnt)
        marker_centers.append(mx + mw // 2)
marker_centers.sort()

if len(marker_centers) >= 2:
    gap_center = (marker_centers[0] + marker_centers[-1]) // 2
    gap_error = gap_center - frame_center_x
    gap_width = marker_centers[-1] - marker_centers[0]
```

### 🧭 **Navigation Algorithm Implementation**

#### **Obstacle Challenge Navigation (ESP32-side state machine)**

**State Machine Flow** *(implemented in `esp32_car.ino`)*:
```
Vision Obstacle Avoidance → Clearance → Corner Turn → Wall Following (repeat)
        ↑                       ↑            ↑              ↑
   Vision Color            Post-Obstacle  Ultrasonic     Ultrasonic
   Detection (R/G)          Stabilizing   Front Distance  Left/Right
```

**Actual firmware logic (`loop()` in `esp32_car.ino`)**:
```
readAllSensors()          // ultrasonic front/left/right, with low-pass filtering
readVisionData()          // parse latest UART message from the Raspberry Pi

IF handleVisionObstacle(): steer hard toward the clear side, drive at SPEED_OBSTACLE
ELIF clearanceState():     center steering, drive at SPEED_CLEARANCE for 500ms after clearing an obstacle
ELIF handleCorner():       continue an in-progress 90°-style corner turn
ELSE:
    detectCorner()          // start a corner turn if front distance < 60cm
    wallFollowing()         // ultrasonic-based wall centering, or vision-driven steering if visionMode == 'A'

IF visionTurnCount >= 12: stop permanently (lap limit reached)
```

**Color-Specific Behaviors** *(from `handleVisionObstacle()`)*:
- **Red Object Detected** (and `0 < obstacleDistance ≤ 50cm`): steer to `STEERING_MAX_RIGHT`, drive at `SPEED_OBSTACLE`
- **Green Object Detected** (same distance condition): steer to `STEERING_MAX_LEFT`, drive at `SPEED_OBSTACLE`
- **Clearance window**: for 500ms after leaving an obstacle state, steering is centered and speed is raised to `SPEED_CLEARANCE`

#### **Parking Maneuver — Marker Detection & Data Relay**
Parking-marker detection runs independently every frame, regardless of the current driving state, matching the intended real robot behavior of only *acting* on it after completing 3 laps:
- Two magenta markers define the parking gap; their midpoint (`gap_center`) and separation (`gap_width`) are computed continuously
- `gap_error = gap_center - frame_center_x` gives how far the gap sits from the robot's current heading
- This data is sent to the ESP32 as `M,<found>,<gap_error>,<gap_width>`; the firmware parses and stores it into `parkingMarkersFound`, `parkingGapError`, and `parkingGapWidth`

### **Sensor and Motor Fusion Implementation**

**Data Integration Pipeline**:
```
Raspberry Pi 4 (Vision) --UART (one-way)--> ESP32
                                              │
                                    ┌─────────┴─────────┐
                                    │   Onboard fusion:   │
                                    │  Ultrasonic (F/L/R) │
                                    │  + latest vision msg│
                                    └─────────┬─────────┘
                                              ▼
                                     Motor / Servo Actuators
```
Unlike a simple "camera decides, ESP32 executes" split, the ESP32 keeps its own onboard driving logic (wall following, corner detection) running from its own ultrasonic sensors at all times, and only defers to the Raspberry Pi's vision data when an obstacle color is actively reported or when `visionMode == 'A'` (vision-driven lane steering).

### **Control System Implementation**

**Vision-side proportional steering (Raspberry Pi, `vision_navigation.py`)**:
```python
error = target_cx - frame_center_x
steering_angle = error * kp          # kp = 0.05
steering_angle = max(-0.5, min(0.5, steering_angle))
```

**Firmware-side steering output (ESP32, `esp32_car.ino`)**:
```cpp
void setSteering(int angle) {
    int clampedAngle = constrain(angle, STEERING_MAX_LEFT, STEERING_MAX_RIGHT); // 55–125
    int invertedAngle = 180 - clampedAngle;   // servo mechanically mounted inverted
    steeringServo.write(invertedAngle);
}
```

### **Inter-Processor Communication**

**UART Protocol Specification** *(verified directly against `readVisionData()` in `esp32_car.ino`)*:
- **Baud Rate**: 115200
- **Direction**: One-way, Raspberry Pi → ESP32 (the ESP32 does not send data back)
- **Command Structure**: Comma-separated plain-text messages terminated by `\n`
- **Timeout Handling**: If no valid message arrives within 500ms (`VISION_TIMEOUT`), the obstacle state automatically resets to `N`
- **Reliability Fix**: `Serial.setTimeout(10)` is set explicitly in `setup()` to prevent `readStringUntil()` from blocking the main control loop for up to 1 second if a line arrives without its `\n` terminator

**Raspberry Pi → ESP32 Message Formats (as parsed by the firmware today)**:
| Header | Format | Meaning |
|--------|--------|---------|
| `A` | `A,<leftArea>,<rightArea>,<error>,<steerAngle>,<turnCount>` | Open Challenge area-based steering + lap counting — sent by `final.py` |
| `R` / `G` / `B` | `<color>,<error>,<distance>,<steerAngle>` | Obstacle color detected — pixel error, distance estimate, suggested steering angle |
| `C` | `C,<error>` | Reserved header handled by the firmware; not currently sent by any vision script |
| `M` | `M,<found>,<gap_error>,<gap_width>` | Parking-gap position from the magenta markers — parsed and stored by the firmware |
| `N` | `N` | No obstacle detected — resets steering to center |

## 🛠️ Engineering Notes

### Why the ESP32 Keeps Its Own Sensor Logic
Running wall-following and corner-detection locally on the ESP32 (rather than fully relying on the Raspberry Pi) keeps basic driving responsive even if the vision pipeline lags for a frame or two — the vision data only takes priority when an obstacle color or explicit lane-steering message is actively being received, with the 500ms timeout falling back to the local ultrasonic behavior automatically.

### Distance-Gated Obstacle Reaction
The firmware only reacts to a reported obstacle color if `0 < obstacleDistance ≤ 50cm` (`handleVisionObstacle()`), which avoids reacting to false detections far outside the useful action range.

## Technical Specifications

### System Requirements
- **Raspberry Pi 4 Model B** running Python 3, `opencv-python`, `numpy`, `pyserial`
- **ESP32 dev board** with `ESP32Servo.h`, programmed via Arduino IDE
- **L298N (or similar) DC motor driver**, standard hobby steering servo
- **3x ultrasonic distance sensors** (front, left, right)

### File Structure
```
software/
├── vision_navigation.py   # Raspberry Pi: Obstacle Challenge detection, lane tracking, parking-gap calculation
├── final.py                # Raspberry Pi: Open Challenge area-based steering + turn counting
├── esp32_car.ino            # ESP32: motor/servo control, ultrasonic state machine, UART parser
└── README.md                # This documentation
```

For the standalone color-calibration workspace, see [Colors Documentation](../colors/README.md).
