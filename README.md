# WRO2026_RCBC
# 🚀 WRO 2026 Future Engineers – RCBC

<center>
<p align="center">
  <img src="Others/Team%20Logo.png" alt="Team Logo" width="600">
</p>

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/anti.wro/)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@WRO_RCBC_EGYPT)
</center>

---

## **EGPYTIAN NATIONAL TEAM **

Welcome to the GitHub repository of Team RCBC, competing in the World Robot Olympiad™ (WRO®) Future Engineers 2025 category. Our team is made up of Egyptian students who have designed a compact, innovative, and autonomous self-driving vehicle to tackle the dynamic challenges of the WRO 2025 competition. Our team name, RCBC—which stands for Reliable Chassis, Brilliant Code—reflects our core philosophy: achieving perfect harmony between mechanical durability and highly intelligent software. This name signifies our competitive spirit, blending robust engineering with cutting-edge algorithms to push the boundaries of autonomous design.

Our mission was to engineer a highly precise and exceptionally fast autonomous vehicle for the WRO 2025 challenge, prioritizing dynamic stability, speed, and flawless execution over extreme miniaturization. Leveraging our expertise in electrical, mechanical, and software engineering, we optimized every component to dominate the 3 m x 3 m game field.
Current best times on the 3 m x 3 m field:
- **Open Challenge**: ## seconds (full score)
- **Obstacle Challenge**: ## seconds (full score)


---

## 📚 **Table of Contents**
- [📂 Complete Documentation Structure](#complete-documentation-structure)
- [👥 The Team](#the-team)
- [🎯 Challenge Overview](#challenge-overview)
- [🤖 Our Robot](#our-robot)
- [🔧 Electronic Systems](#electronic-systems)
- [⚙ Mechanical Systems](#mechanical-systems)
- [💻 Software Architecture](#software-architecture)
- [📹 Performance Videos](#performance-videos)
- [🌐 GitHub Utilization & Development](#github-utilization--development)
- [📜 License & Replication](#license--replication)

---

## 📂 **Complete Documentation Structure** <a id="complete-documentation-structure"></a>

<div align="center">

## 🔍 **DETAILED TECHNICAL DOCUMENTATION AVAILABLE**

### **Each folder contains comprehensive README documentation with specialized technical content**

| 📁 Folder | 🎯 Technical Content | 📖 Detailed Documentation |
|-----------|----------------------|---------------------------|
| **🧮 MATLAB** | **Vision System Calibration**<br>• LAB colorspace analysis<br>• Threshold optimization<br>• Lighting condition testing | [🔗 Explore MATLAB Documentation](matlab/README.md) |
| **⚙ Models** | **Mechanical Engineering**<br>• 3D CAD designs<br>• Assembly instructions<br>• Gear system calculations | [🔗 Explore 3D Models & Assembly Documentation](models/README.md) |
| **🔌 Schemes** | **Electrical Systems**<br>• Wiring diagrams<br>• Power management<br>• Component schematics & datasheets | [🔗 Explore Schematics & Wiring Documentation](schemes/README.md) |
| **💾 Source Code** | **Software Algorithms**<br>• Navigation logic<br>• Sensor fusion<br>• Control systems | [🔗 Explore Software & Algorithms Documentation](src/README.md) |
| **👥 Team Photos** | **Team Documentation**<br>• Member profiles<br>• Development journey<br>• Competition preparation | [🔗 Explore Team Photos Documentation](t-photos/README.md) |
| **🚗 Vehicle Photos** | **Vehicle Documentation**<br>• Multi-angle views<br>• Component labeling<br>• System integration | [🔗 Explore Vehicle Photos Documentation](v-photos/README.md) |
| **🎥 Videos** | **Performance Validation**<br>• Challenge demonstrations<br>• Engineering tests<br>• System validation | [🔗 Explore Performance Videos Documentation](video/README.md) |
| **📚 Other Resources** | **Technical References**<br>• Component images<br>• Development resources<br>• Additional documentation | [🔗 Explore Additional Resources Documentation](other/README.md) |

</div>

---

## 👥 **The Team** <a id="the-team"></a>

Team RCBC includes passionate students from EGYPT, guided by a coach. This is our **first year** competing in the WRO Future Engineers category, and each member brings unique skills to the project, from electronics to computer vision.

<div align="center">
<img src="t-photos/team_official.jpg" alt="Official Team Moment" width="600">
<img src="t-photos/workplace.jpg" alt="Team RCBC at Work" width="600">
</div>

### **Members**
- **Yossef Hossam** (Team Leader)  
  *Role*: Electronics, Mechanical Design, Software, Strategy Integration  
  *Background*: High School Student, Stem October High School For Boys (S28)
  *Contact*: [atakan@atakanersoy.com](mailto:atakan@atakanersoy.com), [aersoy24@ku.edu.tr](mailto:aersoy24@ku.edu.tr)  
  *Born*: 2009, Egypt

- **Mahmoud Atef**  
  *Role*: Computer Vision Research, Strategy  
  *Background*: High School Student, Stem October High School For Boys (S28)
  *Born*: 2010, Egypt

  - **Hamza Mahmoud**   
  *Role*: Electronics, Software, 
  *Background*: High School Student, Stem October High School For Boys (S28)  
  *Contact*: [atakan@atakanersoy.com](mailto:atakan@atakanersoy.com), [aersoy24@ku.edu.tr](mailto:aersoy24@ku.edu.tr)  
  *Born*: 2009, EGYPT

### **Coach**
- **Manar**  
  *Role*: Team Coach, Connector  
  *Background*: Alumni, Electrical and Electronics Engineering, Koç University (2025)  
  *Born*: 2000, EGYPT  
<br>
<div align="center">
<img src="t-photos/team_fun.jpg" alt="Team RCBC Fun Photo" width="600">
</div>


### **Team Journey Moments**
Throughout our development process from initial concept to competition readiness, we captured key moments demonstrating our collaborative spirit and technical dedication. These images showcase our brainstorming sessions, technical adjustments, and competition preparation.
---

## 🎯 **Challenge Overview** <a id="challenge-overview"></a>

<div align="center">

## 🏁 **WRO 2026 Future Engineers Challenges**

### **Two distinct autonomous navigation challenges testing vehicle intelligence and precision**

</div>

### **🚀 Open Challenge**
<div align="center">

**Objective**: Complete three autonomous laps on dynamically configured tracks

| Aspect | Challenge | Our Solution |
|--------|-----------|--------------|
| **Track Variability** | Random internal wall placements | Adaptive path planning algorithms |
| **Navigation** | Unknown track layouts each round | Robust wall-following with corner detection |
| **Performance** | Consistent lap times across variations | Optimized PID control and sensor fusion |
| **Precision** | Maintain course in narrow lanes | High-accuracy steering and speed control |

</div>

### **🚧 Obstacle Challenge**
<div align="center">

**Objective**: Navigate three laps with traffic sign compliance and precision parking

| Challenge Element | Requirement | Our Implementation |
|-------------------|-------------|-------------------|
| **Traffic Signs** | Red → Right bias<br>Green → Left bias | Real-time color detection with LAB colorspace |
| **Obstacle Avoidance** | Dynamic path adjustment | Smooth following at consistent distances |
| **Parking Maneuver** | Parallel parking after lap completion | Multi-stage parking with sensor validation |
| **Navigation** | Shortest path optimization | Efficient routing around obstacle combinations |
</div>

### **📁 Documentation Evaluation Framework**

<div align="center">

## 📊 **WRO 2026 Engineering Documentation Scoring (30 points total)**

| Scoring Area | Maximum Points | Our Documentation Coverage |
|--------------|----------------|---------------------------|
| **1. Mobility Management** | 4 points | Complete mechanical design, motor selection, steering system, assembly instructions |
| **2. Power & Sense Management** | 4 points | Power systems, sensor integration, wiring diagrams, component specifications |
| **3. Obstacle Management** | 4 points | Navigation algorithms, parking strategies, source code with detailed comments |
| **4. Pictures – Team and Vehicle** | 4 points | Multi-angle vehicle photos, team photos, component labeling |
| **5. Performance Videos** | 4 points | Complete challenge demonstrations with commentary and analysis |
| **6. GitHub Utilization** | 4 points | Version control, structured documentation, regular commits |
| **7. Engineering Factor** | 4 points | Custom design and manufacturing throughout the vehicle |
| **8. Overall Judge Impression** | 2 points | Clear communication enabling easy replication |
| **Total Documentation Score** | **Still unknown (WE Haven't Competed Yet** | **(≈25% of total competition score)** |
</div>

### **Key Evaluation Areas**
- Still Unknown ( WE will Update all These Areas After The Competion )

**Scoring Philosophy**: Documentation is evaluated based on completeness, structure, and ease of replication - not comparison between teams. Each scoring area uses a 0-4 point scale where "Exceeds Expectations" requires not only enabling exact duplication but also providing improvement suggestions.

### **🎓 Educational Objectives**
- **Advanced Computer Vision**: Real-world implementation of color space theory
- **Sensor Fusion**: Integrating multiple data sources for robust navigation
- **Control Systems**: Precision steering and speed control algorithms
- **Engineering Documentation**: Professional technical communication
- **Problem Solving**: Systematic approach to technical challenges

---

## 🤖 **Our Robot** <a id="our-robot"></a>

<div align="center">
<img src="v-photos/front_view.jpg" alt="RCBC Autonomous Vehicle" width="600">
</div>

Our platform represents a breakthrough in high-performance autonomous vehicle design, achieving exceptional speed and pinpoint precision without compromising dynamic stability. The complete system seamlessly integrates a robust custom mechanical chassis with sophisticated electronics and highly optimized software algorithms

**Core Processing Architecture**:
- **Primary Vision Processor**: Rasberry Pi 4 model B dedicated to real-time image processing
- **Secondary Sensor Processor**: Esp32 microcontroller handling multi-sensor data fusion
- **Distributed Processing**: Optimized task allocation between vision and control subsystems

**Perception System**:
- **Front-Facing Detection**: HC-SR04 Ultrasonic Sensor Detector for general obstacle awareness
- **Side-Mounted Precision Sensors**: Dual HC-SR04 Ultrasonic Sensor Detector for parking detection
- **Visual Navigation**: Rasberry Pi Camera module 2 8MP camera with optimized field of view for track following and obstacle detection

**Propulsion and Control**:
- **Drive System**: 450 RPM DC Gear Motor JGA25-370 with External encoder feedback
- **Steering Mechanism**: Custom Ackermann geometry with metalic servo actuation
- **Power Management**: Integrated LiPo Batteries with comprehensive power distribution

Complete vehicle documentation with detailed component identification available in [vehicle photos](v-photos/README.md).

<div align="center">
<img src="models/design_to_life.jpg" alt="Digital to Physical Realization" width="600">
</div>

### Potential Future Improvements (Overall Vehicle)
- Reduce size even further to ≈ 100 × 150 × 60 mm by switching to smaller LiPo (3.7 V), a coreless motor + micro gearbox and smaller mechanic differential style.
- Implement four-wheel steering or active rear-axle 4 wheel drive to control for tighter turning radius on narrow lanes.
- Add a very small extra second camera facing backwards for reverse parking or emergency obstacle detection.

---

## 🔧 **Electronic Systems** <a id="electronic-systems"></a>

Our electronic architecture emphasizes modularity, reliability, and hands-on engineering through custom manufacturing approaches.

### **Component Integration Strategy**

<div align="center">

| Component | Image | Quantity | Function | Key Specifications |
|-----------|-------|----------|----------|-------------------|
| **Raspberry Pi 4 Model B (4GB)** | <img width="150" alt="image" src="https://github.com/user-attachments/assets/3615940c-df78-42af-b8ce-07dddc0f563a" /> | 1 | Main Processing & Vision | Quad-core Cortex-A72, 4GB RAM, Peripheral & Camera Interface |
| **Raspberry Pi Camera Module 2 (8MP)** | <img width="150" alt="image" src="https://github.com/user-attachments/assets/10418180-6c80-4b07-a8bd-66003c9ab83e" /> | 1 | Visual Navigation | 8MP Sony IMX219 sensor, 1080p video, CSI interface |
| **HC-SR04 Ultrasonic Sensor** | <img src="other/hc_sr04.jpg" width="150"> | 2 | Distance & Obstacle Detection | 2cm to 400cm range, 15-degree measurement angle |
| **MG966R Servo Motor** | <img src="other/mg966r.jpg" width="150"> | 1 | Steering Actuation | High-torque metal gear servo, 180° rotation |
| **L298N Motor Driver** | <img src="other/l298n.jpg" width="150"> | 1 | Motor Control | Dual H-bridge driver, up to 2A current per channel |
| **LiPo Battery Pack** | <img src="other/lipo_battery.jpg" width="150"> | 1 | Power Source | High-capacity rechargeable lithium polymer power supply |
</div>

**Component Selection Philosophy**: We prioritize widely available, well-documented components to ensure reproducibility. All parts can be sourced through standard electronics distributors using the provided specifications and images.

### **Professional Wiring Implementation**

<div align="center">
  <a href="schemes/wiring_diagram.jpg" target="_blank"> 
    <img src="schemes/wiring_diagram.jpg" alt="Professional Wiring Diagram" height="300">
  </a>
  <img src="schemes/complete_sockets_pertinax_scheme.jpg" alt="Physical Implementation" height="300">
</div>
<p align="center">
  <em>1) Complete hand-drawn and digitally traced professional wiring schematic showing all electrical connections (<a href="schemes/wiring_diagram.jpg" target="_blank">view full resolution</a>) • 2) Physical implementation demonstrating socket-based construction of the schematic</em>
</p>

### **Individual Component Schematics**

<div align="center">

| Component Schematic | Description | Full Documentation |
|---------------------|-------------|-------------------|
| <img src="schemes/rpi_wiring_scheme.jpg" height="150"> | **Raspberry Pi 4 Connection System**<br>GPIO interface, power distribution, and camera CSI connection | [View Details](schemes/README.md#microcontroller-systems) |
| <img src="schemes/driver_scheme.jpg" height="150"> | **L298N Motor Driver Control**<br>PWM motor regulation and dual H-bridge connections | [View Details](schemes/README.md#motor-control-systems) |
| <img src="schemes/servo_scheme.jpg" height="150"> | **MG966R Servo Control**<br>Steering mechanism PWM signal mapping | [View Details](schemes/README.md#motor-control-systems) |
| <img src="schemes/ultrasonic_scheme.jpg" height="150"> | **HC-SR04 Ultrasonic Sensor Network**<br>Trigger and echo pin integration for distance measurement | [View Details](schemes/README.md#sensor-systems) |
| <img src="schemes/charger_power_management_scheme.jpg" height="150"> | **Power Management & Distribution**<br>LiPo battery charging and main power regulation | [View Details](schemes/README.md#power-management-components) |
| <img src="schemes/button_scheme.jpg" height="150"> | **User Interface & Control**<br>Start push button and tactile system interface | [View Details](schemes/README.md#-interface--control-systems) |
</div>

### **Power Management Innovation**

During system integration, we identified a critical design limitation in our chosen power management IC. The LiPo Rider Plus's switch only controlled the 5V output rail, leaving the 3.3V regulator permanently active and creating potential battery drain.

**Engineering Solution**:
* **Root Cause Analysis**: Direct battery routing to auxiliary components bypassing the main control switch, causing minor standby current draw.
* **Component Modification**: Remapped power distribution lines and integrated a reliable master power distribution path.
* **Implementation**: Rerouted the main input rails through the primary hardware switch to ensure complete circuit isolation when deactivated.
* **Validation**: Full power cut-off achieved with zero standby current draw, protecting the Raspberry Pi and motor drivers from unwanted power leakage.
<div align="center">
<img src="schemes/switch_fix.jpg" alt="Power Management Modification" width="600">
<p><em>Hardware modification enabling complete power rail control through single switch</em></p>
</div>

### **Signal Integrity Systems**

The **LM2569 Buck converter** ensures reliable communication between our 3.3V microcontrollers and 5V servo system. This implementation prevents signal degradation and ensures precise servo positioning under all operating conditions.

### **Thermal Performance Validation**

Comprehensive thermal analysis confirmed optimal operating temperatures across all critical subsystems:


### **Sensor Integration Challenges**

Our minimal vertical profile created unique challenges for Time-of-Flight sensor implementation. The proximity to ground plane caused premature ground intersection in the sensors' field of view, limiting effective detection range.

**Optical Solution**:
- **Angular Adjustment**: Upward sensor tilt to delay ground intersection
- **Optical Modification**: Custom window lenses to narrow field of view
- **Performance Improvement**: Extended usable detection range from ~150cm to ~300cm

### **Development Convenience Features**

Implementation of magnetic USB connectors for programming interfaces significantly improved development workflow efficiency, allowing rapid code iterations without physical connector wear.

<div align="center">
<img src="v-photos/front_view.jpg" alt="Development Interface Access" width="600">
<p><em>Easy-access programming interface with magnetic connection system</em></p>
</div>

### **Performance Specifications**

- **Maximum Theoretical Speed**: 1.52 m/s (calculated from motor RPM and drive train ratios)
- **Operational Speed**: 1.4 m/s (PWM controlled for stability optimization)
- **Battery Endurance**: 3-4 hours typical operation
- **Charge Duration**: ~60 minutes via USB-C fast charging
- **Power Consumption**: 0.8W minimum, 200-250mA typical operational current

### Powertrain – Potential Improvements
- Switch to higher RPM coreless motor + greater 25:1 Micro Metal Gearbox → theoretical top speed > 2.3 m/s while keeping the same design.
- Replace the 25:25 external gear with an internal planetary stage inside the JGA27-370 motor can → saves 4 mm length with direct mounting of the motor to the rear axle.
- Active cooling (micro 10 mm fan, 0.8 g) → could improve the overall airflow in the system, allowing for faster operation and even higher stability.

---

## ⚙ **Mechanical Systems** <a id="mechanical-systems"></a>

Our mechanical design philosophy centers on achieving maximum capability within minimal dimensions through innovative engineering and precision manufacturing.

### **Core Mechanical Specifications**
- **Overall Dimensions**: 250mm (L) × 180mm (W) × 70mm (H)
- **Total Mass**: Approximately 800 grams
- **Structural Material**: 3D-printed PLA+ for optimal strength-to-weight ratio
- **Drive Configuration**: Rear-wheel drive with custom differential
- **Steering System**: True Ackermann geometry with precision linkage

### **Design Integration Approach**

<div align="center">
<img src="models/CAD_fusion_isometric_view.jpg" alt="Digital Design Model" height="325">
<img src="models/IRL_isometric_view.jpg" alt="Physical Implementation" height="325">
</div>
<p align="center">
  <em>Digital design precision translated to physical implementation through advanced manufacturing techniques</em>
</p>

### **Steering Geometry Implementation**

Our custom Ackermann steering system ensures each wheel maintains optimal alignment during turns, minimizing tire scrub and maximizing maneuverability.

<div align="center">
<img src="models/3d_CAD_motion.gif" alt="Steering Mechanism Animation" height="325">
<img src="models/ackermann_calculations_turning_radius.jpg" alt="Steering Geometry Analysis" height="325">
</div>
<p align="center">
  <em>Dynamic steering simulation and geometric analysis ensuring optimal turning performance</em>
</p>

**Steering System Evolution**:
- **Initial Concept**: Integrated print-in-place mechanism for rapid prototyping
- **Performance Refinement**: Multi-component assembly for long-term precision
- **Final Implementation**: Four M2 fasteners with locking nuts for permanent alignment
- **Wheel Articulation**: -50° to +32° range optimized for competition track dimensions

### Mechanical – Potential Improvements
- True Ackermann geometry.
- Ball bearings on the two rear wheels → theoretical 7–9 % less rolling resistance in CAD tests.
- Possible uspension system using micro torsion bars could improve stability if the track includes ground obstacles in the future when crossing the 3 mm track.

### **Power Transmission System**

The custom 2-gear differential ensures smooth torque distribution during turning maneuvers, preventing wheel slip and maintaining traction.

<div align="center">
<table align="center">
<tr>
<td align="center">
<img src="models/differential_test.gif" alt="Differential Function Test" height="430">
</td>
<td align="center">
<img src="models/CAD_design_4_gear_mini_differential_1.jpg" alt="Differential Assembly View 1" height="213"><br>
<img src="models/CAD_design_4_gear_mini_differential_2.jpg" alt="Differential Assembly View 2" height="213">
</td>
</tr>
</table>
</div>
<p align="center">
  <em>Physical validation of differential operation and comprehensive CAD documentation</em>
</p>

**Gear System Architecture**:
- **Speed Reduction**: 25:25 ratio through custom spur gear design
- **Torque Distribution**: Two 25-tooth spur gears enabling independent wheel rotation transferring the torque direct from the motor.
- **Manufacturing Precision**: 100% infill for maximum durability under load
- **Efficiency Optimization**: Precisely calculated tooth profiles for minimal power loss

### **Manufacturing File Repository**

*All components provided in 3MF format for maximum compatibility across different 3D printing platforms and slicing software*

<div align="center">

| Component | File Reference | Quantity | Visual Reference | Functional Description |
|-----------|----------------|----------|------------------|------------------------|
| **Main Chassis** | [`design_base.3mf`](models/design_base.3mf) | 1 | <img src="models/CAD_design_base_1.jpg" width="80"><img src="models/CAD_design_base_2.jpg" width="80"> | Primary structural element with integrated mounting features |
| **4-Gear Differential** | [`design_4_gear_mini_differential.3mf`](models/design_4_gear_mini_differential.3mf) | 1 | <img src="models/CAD_design_4_gear_mini_differential_1.jpg" width="80"><img src="models/CAD_design_4_gear_mini_differential_2.jpg" width="80"> | Complete differential assembly with integrated gear mounting |
| **Front Rim Assembly** | [`design_front_rim_bearing.3mf`](models/design_front_rim_bearing.3mf) | 2 | <img src="models/CAD_design_front_rim_bearing_1.jpg" width="80"><img src="models/CAD_design_front_rim_bearing_2.jpg" width="80"> | Steering wheels with integrated bearing seats |
| **Steering Arm** | [`design_steering_arm.3mf`](models/design_steering_arm.3mf) | 2 | <img src="models/CAD_design_steering_arm_1.jpg" width="80"><img src="models/CAD_design_steering_arm_2.jpg" width="80"> | Ackermann steering linkage arms (left/right pair) |
| **Steering Linkage** | [`design_steering_linkage.3mf`](models/design_steering_linkage.3mf) | 1 | <img src="models/CAD_design_steering_linkage.jpg" width="80"> | Central steering connection mechanism |
| **25T Spur Gear** | [`design_spur_25_gear.3mf`](models/design_spur_25_gear.3mf) | 1 | <img src="models/CAD_design_spur_25_gear_1.jpg" width="80"><img src="models/CAD_design_spur_25_gear_2.jpg" width="80"> | 25-tooth torque transmission gear |
| **26T Spur Gear** | [`design_spur_26_gear.3mf`](models/design_spur_26_gear.3mf) | 1 | <img src="models/CAD_design_spur_26_gear_1.jpg" width="80"><img src="models/CAD_design_spur_26_gear_2.jpg" width="80"> | 26-tooth motor interface gear |
| **12T Bevel Gear** | [`design_bevel_12_gear.3mf`](models/design_bevel_12_gear.3mf) | 4 | <img src="models/CAD_design_bevel_12_gear_1.jpg" width="80"><img src="models/CAD_design_bevel_12_gear_2.jpg" width="80"> | Differential bevel gears (set of 4 required) |
| **Motor Enclosure** | [`design_motor_lid.3mf`](models/design_motor_lid.3mf) | 1 | <img src="models/CAD_design_motor_lid.jpg" width="80"> | N20 motor protective housing |
| **Long Rear Rim** | [`design_back_rim_long.3mf`](models/design_back_rim_long.3mf) | 1 | <img src="models/CAD_design_back_rim_long.jpg" width="80"> | Extended right-side drive wheel |
| **Short Rear Rim** | [`design_back_rim_short.3mf`](models/design_back_rim_short.3mf) | 1 | <img src="models/CAD_design_back_rim_short.jpg" width="80"> | Compact left-side drive wheel |
| **Front Upper Cover** | [`design_front_top_cover.3mf`](models/design_front_top_cover.3mf) | 1 | <img src="models/CAD_design_front_top_cover_1.jpg" width="80"><img src="models/CAD_design_front_top_cover_2.jpg" width="80"> | Electronics protection shield |
| **Front Lower Cover** | [`design_front_bottom_cover.3mf`](models/design_front_bottom_cover.3mf) | 1 | <img src="models/CAD_design_front_bottom_cover.jpg" width="80"> | Underbody protection panel |
| **Button Interface** | [`design_button_cap.3mf`](models/design_button_cap.3mf) | 1 | <img src="models/CAD_design_button_cap_1.jpg" width="80"><img src="models/CAD_design_button_cap_2.jpg" width="80"> | User interface button cap |

</div>

### **Performance Engineering Analysis**

**Drive Train Calculations**:
- **Motor Specification**: 450 RPM JGA 25-370 DC motor with quadrature encoder
- **Gear Reduction**: 25:25 ratio providing optimal speed-torque balance
- **Theoretical Maximum Velocity**: 1.52 m/s derived from wheel geometry and drive ratios
- **Operational Velocity**: 1.5 m/s selected for optimal control stability

**Structural Analysis**:
- **Motor Torque Capacity**: ~1.25 Nm at 12V, sufficient for 800g vehicle acceleration
- **Bearing System**: Two precision bearings minimizing rotational friction
- **Steering Load Management**: Mechanism optimized for servo torque characteristics
- **Impact Resistance**: Validated through comprehensive testing under competition conditions

### **Assembly Methodology**

<div align="center">
<img src="models/building_steps.jpg" alt="Assembly Process Documentation" width="600">
</div>
<p align="center">
  <em>Staged assembly approach ensuring proper system integration and alignment</em>
</p>

**Assembly Sequence**:
1. **Drive System Integration**: Differential assembly and motor mounting with M3 hardware
2. **Steering Mechanism Installation**: Ackermann linkage and servo integration
3. **Wheel System Assembly**: Bearing installation and wheel mounting
4. **Electronic System Integration**: Bread board installation and component connection
5. **Final System Validation**: Comprehensive functional testing and alignment verification

---

## 💻 **Software Architecture** <a id="software-architecture"></a>

Our software implementation employs a distributed processing architecture that optimizes performance through specialized task allocation between multiple processors. This documentation was last updated on **[september]**.

### **System Architecture Overview**

<table>
<tr>
<td width="60%">

**Processing Distribution**:
- **Vision & Navigation Unit**: Raspberry Pi 4 handling real-time image analysis, obstacle-color detection, lane tracking, parking-marker detection, and high-level vision-based decision making
- **Sensor & Motor Control Unit**: ESP32 running its own onboard state machine for ultrasonic wall following, obstacle avoidance, clearance handling, and corner turning, while accepting vision-based overrides from the Raspberry Pi over UART
- **Communication Bridge**: One-directional UART protocol at 115200 baud, Raspberry Pi → ESP32, carrying vision detection and navigation results as plain-text messages

**Core Software Components**:
- [`vision_navigation.py`](vision_navigation.py) - Obstacle Challenge: real-time HSV-based detection of red/green obstacle pillars, white track lane detection, magenta parking-marker detection, and proportional steering-correction calculation
- [`final.py`](final.py) - Open Challenge: area-based wall following using dual ROI strips, orange-line turn counting, and active transmission of `A` messages over UART
- [`esp32_car.ino`](esp32_car.ino) - Sensor and motor management firmware, onboard ultrasonic wall-following and corner-turning state machine, vision-message parser, and motor/servo control

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
  - `opencv-python (cv2)` - Image preprocessing, HSV color masking, and contour-based object detection, blob analysis, and feature extraction
  - `numpy` - Array operations for HSV bounds, morphological kernels, and image-processing calculations
  - `pyserial` - One-directional UART serial communication with the ESP32 microcontroller

#### **ESP32 (Sensor and Motor Microcontroller)**
- **Programming Language**: Arduino C++ for efficient sensor and motor data handling
- **Development Interface**: Standard micro USB connection to evaluation board
- **Essential Libraries**:
  - `ESP32Servo.h` - PWM-based control of the steering servo
- **Communication Protocol**: One-directional UART Serial (115200 baud), Raspberry Pi → ESP32, used to relay vision-based obstacle, lane, and parking data

#### **Development Workflow Optimization**

We implemented magnetic USB connectors for the vision microcontroller, providing significant advantages during intensive development cycles. The magnetic interface enables rapid connection changes, prevents physical port damage from repeated use, and streamlines the programming and debugging process.

#### **Code Deployment Process**

1. **Raspberry Pi 4 Model B Python Deployment**:
   - Transfer `.py` source files directly to the microcontroller filesystem using the magnetic USB connection
   - Select the appropriate vision script according to the challenge currently being run
   - Execute the selected Python source directly without a compilation stage
   - No compilation overhead — immediate interpreted execution for rapid iteration
   - Calibration code can be used to adjust the vision variables and HSV thresholds according to the current environment

2. **ESP32 Arduino Deployment**:
   - Compile source code in Arduino IDE with ESP32 board package support
   - Upload compiled binary via micro USB interface to evaluation board
   - Precompiled firmware deployment ensuring reliable sensor and motor operation

### 🎨 **Vision Processing Strategy**

We selected the **HSV color space** for its superior performance under variable lighting conditions compared to traditional RGB representation. Detection thresholds for the red and green obstacle pillars, the white track floor, and the magenta parking markers were manually calibrated and fine-tuned per venue using a dedicated debug mask window. The standalone calibration workflow is available in the `colors` folder.

**Technical Rationale**: HSV colorspace provides adequate performance for our application requirements, isolating hue independently from brightness/lighting variance, while more complex approaches (e.g. machine learning-based detection) would introduce unnecessary computational overhead without significant benefits for this specific use case.

**Detected Targets**:
- **Red / Green pillars**: Dual-range red mask + single-range green mask, filtered by area and solidity
- **White track floor (lane)**: Restricted to the bottom half of the frame, used to compute the drivable corridor's centroid when no obstacle is in view
- **Magenta parking markers**: Detected independently every frame regardless of driving state; used to calculate the parking-gap center and width once two markers are visible
- **Orange turn line**: Used by `final.py` for Open Challenge turn/lap counting

### **Vision Processing Pipeline**

1. **Image Capture**: 320×240 resolution at approximately 26 frames per second
2. **Color Transformation**: Camera image converted into HSV colorspace for color segmentation
3. **Color Masking**: HSV thresholds isolate the required target colors
4. **Morphological Processing**: Binary masks are processed using morphological operations and kernels to improve detection reliability
5. **Feature Detection**: Contour/blob analysis with size, area, and shape filtering
6. **Target Identification**: Largest valid blob or valid set of blobs selected for reliability
7. **Error Calculation**: Position deviation from the desired tracking point or frame center
8. **Navigation Output**: Calculated detection information is converted into steering and navigation data
9. **UART Transmission**: Vision results are transmitted from the Raspberry Pi to the ESP32 using the defined plain-text UART protocol

### **Calibration Debug Windows**

<table>
<tr>
<td width="50%">
<img src="1788558162827_image.png" alt="Green Mask Calibration" width="100%">
<p align="center"><em>Green mask calibration window</em></p>
</td>
<td width="50%">
<img src="1788558165154_image.png" alt="Red Mask Calibration" width="100%">
<p align="center"><em>Red mask calibration window</em></p>
</td>
</tr>
</table>

<div align="center">
<img src="hard_light_condition_tests.jpg" alt="Environmental Testing Validation" width="600">
<p><em>Comprehensive testing under challenging lighting conditions including direct sunlight exposure</em></p>
</div>

### 🧭 **Navigation Algorithm Implementation**

#### **Obstacle Challenge Navigation**

The obstacle challenge uses a distributed navigation system in which the Raspberry Pi performs visual obstacle detection while the ESP32 executes the real-time vehicle-control state machine.

**State Machine Flow**:

```text
Vision Obstacle Avoidance → Clearance → Corner Turn → Wall Following (repeat)
        ↑                       ↑            ↑              ↑
   Vision Color            Post-Obstacle  Ultrasonic     Ultrasonic
   Detection (R/G)          Stabilizing   Front Distance  Left/Right
```

**Actual firmware logic (`loop()` in `esp32_car.ino`)**:

```text
readAllSensors()          // ultrasonic front/left/right, with low-pass filtering
readVisionData()          // parse latest UART message from the Raspberry Pi

IF handleVisionObstacle():
    steer hard toward the clear side
    drive at SPEED_OBSTACLE

ELIF clearanceState():
    center steering
    drive at SPEED_CLEARANCE for 500ms after clearing an obstacle

ELIF handleCorner():
    continue an in-progress 90°-style corner turn

ELSE:
    detectCorner()        // start a corner turn if front distance < 60cm
    wallFollowing()       // ultrasonic-based wall centering,
                          // or vision-driven steering if visionMode == 'A'

IF visionTurnCount >= 12:
    stop permanently
```

**Color-Specific Behaviors**:
- **Red Object Detection**: When `0 < obstacleDistance ≤ 50cm`, steer to `STEERING_MAX_RIGHT` and drive at `SPEED_OBSTACLE`
- **Green Object Detection**: When `0 < obstacleDistance ≤ 50cm`, steer to `STEERING_MAX_LEFT` and drive at `SPEED_OBSTACLE`
- **Clearance Window**: For 500ms after leaving an obstacle state, steering is centered and speed is raised to `SPEED_CLEARANCE`
- **Position Maintenance**: Consistent pixel positioning is used for smooth obstacle tracking

<table>
<tr>
<td width="50%">
<img src="1788558167694_image.png" alt="Red Obstacle Detection Example" width="100%">
<p align="center"><em>Live red obstacle detection with bounding box</em></p>
</td>
<td width="50%">
<img src="1788558170273_image.png" alt="Green Obstacle Detection Example" width="100%">
<p align="center"><em>Live green obstacle detection during track navigation</em></p>
</td>
</tr>
</table>

<div align="center">
<img src="example_detection.jpg" alt="Single Color Detection" style="width:80%;">
<img src="example_all_detection.jpg" alt="Multi-Color Detection" style="width:80%;">
</div>

### **Open Challenge Navigation**

The Open Challenge uses `final.py` on the Raspberry Pi while keeping the same ESP32 motor-control platform.

The Open Challenge navigation system is based on:
- Area-based wall following
- Two Region-of-Interest (ROI) strips used to estimate relative wall/track position
- Vision-based steering correction
- Orange-line detection for turn counting
- UART transmission using the `A` command
- Turn/lap counting and automatic stopping after the configured limit

The `A` message contains:

```text
A,<leftArea>,<rightArea>,<error>,<steerAngle>,<turnCount>
```

The ESP32 recognizes this message and uses vision-driven steering when `visionMode == 'A'`.

If:

```text
visionTurnCount >= 12
```

the vehicle stops permanently because the configured lap/turn limit has been reached.

### **Parking Maneuver Analysis**

Our compact dimensions required innovative parking strategies to operate within the constrained parking space.

<div align="center">
<img src="parking_cube_strategy.jpg" alt="Complex Parking Scenario" height="375">
<img src="parking_cubeless_strategy.jpg" alt="Simplified Parking Approach" height="375">
</div>
<p align="center">
  <em>Parking strategy analysis for different final obstacle configurations</em>
</p>

Parking-marker detection runs independently every frame, regardless of the current driving state. Two magenta markers define the parking gap; their midpoint and separation are continuously calculated and transmitted to the ESP32.

### **Parking Marker Detection & Data Relay**

```python
magenta_mask = cv.inRange(hsv, lower_magenta, upper_magenta)
magenta_contours, _ = cv.findContours(
    magenta_mask,
    cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE
)

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

When two markers are visible:
- `gap_center` represents the horizontal center of the parking gap
- `gap_error = gap_center - frame_center_x` represents the gap's horizontal deviation from the camera center
- `gap_width` represents the pixel separation between the two marker centers

This information is transmitted as:

```text
M,<found>,<gap_error>,<gap_width>
```

The ESP32 parses and stores the values as:
- `parkingMarkersFound`
- `parkingGapError`
- `parkingGapWidth`

Detection is continuous, while the actual parking action is intended to occur after completing the required laps.

### **Parallel Parking Strategy Optimization**

**🚧 Challenge**: Our compact vehicle length required extremely precise maneuvers.

- **Critical Clearance Design**: Narrow extension width allowed wall clearance during turns
- **🔄 Maneuverability Enhancement**: Additional space enabled reliable parking execution

**Multi-Stage Parking Sequence**:
1. **Approach Phase**: Follow the magenta wall using camera guidance while continuously monitoring the parking markers
2. **Turn-in Execution**: 80-degree turn outside the parking spot
3. **Alignment Phase**: Odometry-based reverse positioning
4. **Reverse Maneuver**: Controlled backing for final alignment
5. **Straighten Phase**: Final orientation adjustment

### **Parallel Parking – Potential Improvements**

- **Pure vision-based parking using parking walls as obstacles**:
  - Eliminates ToF distance dependency
  - Works even if the parking zone is shifted elsewhere
  - Uses visible parking walls/markers as the primary geometric reference

- **Single-motion slow parking trajectory instead of the safer fast three-segment approach**:
  - Could save approximately **1.5 s**
  - The current three-segment approach remains safer and easier to control reliably

### **Obstacle Navigation Patterns**

The algorithm handles all possible obstacle combinations through systematic pattern recognition and response.

<div align="center">
<img src="obstacle_challenge_strategy_1.jpg" alt="Clockwise Navigation Patterns" height="375">
<img src="obstacle_challenge_strategy_2.jpg" alt="Counter-clockwise Navigation Patterns" height="375">
</div>
<p align="center">
  <em>Comprehensive obstacle combination analysis for both navigation directions</em>
</p>

The obstacle strategy assigns each obstacle color a predefined avoidance direction:
- **Red** → right-side avoidance
- **Green** → left-side avoidance
- **After obstacle clearance** → centered stabilization
- **Corner detection** → ultrasonic-based turning
- **Post-corner** → return to wall-following behavior

### **Sensor and Motor Fusion Implementation**

**Data Integration Pipeline**:

```text
Raspberry Pi 4 (Vision)
        │
        │ One-way UART @ 115200 baud
        │
        ▼
      ESP32
        │
        ├──────────────────────────────┐
        │                              │
        ▼                              ▼
Ultrasonic Sensors              Latest Vision Message
 Front / Left / Right            R / G / A / M / N
        │                              │
        └──────────────┬───────────────┘
                       ▼
                Onboard Fusion
                       │
                       ▼
              Navigation State Machine
                       │
                       ▼
              Motor / Servo Actuators
```

Unlike a simple "camera decides, ESP32 executes" split, the ESP32 keeps its own onboard driving logic running continuously.

The ESP32 independently processes:
- Front ultrasonic distance
- Left ultrasonic distance
- Right ultrasonic distance
- Low-pass filtered sensor values
- Corner detection
- Wall-following control
- Motor control
- Steering-servo control
- Current vision-command state

The Raspberry Pi provides additional vision information when available. Vision information takes priority when an obstacle color is actively reported or when `visionMode == 'A'` for vision-driven Open Challenge steering.

### **Control System Implementation**

**Vision-side proportional steering (`vision_navigation.py`)**:

```python
error = target_cx - frame_center_x
steering_angle = error * kp          # kp = 0.05
steering_angle = max(-0.5, min(0.5, steering_angle))
```

**Firmware-side steering output (`esp32_car.ino`)**:

```cpp
void setSteering(int angle) {
    int clampedAngle = constrain(
        angle,
        STEERING_MAX_LEFT,
        STEERING_MAX_RIGHT
    ); // 55–125

    int invertedAngle = 180 - clampedAngle;
    // servo mechanically mounted inverted

    steeringServo.write(invertedAngle);
}
```

### **Inter-Processor Communication**

**UART Protocol Specification**:

- **Baud Rate**: 115200
- **Direction**: One-way, Raspberry Pi → ESP32
- **Command Structure**: Comma-separated plain-text messages terminated by `\n`
- **Timeout Handling**: If no valid message arrives within 500ms (`VISION_TIMEOUT`), the active obstacle state automatically resets to `N`
- **Reliability Fix**: `Serial.setTimeout(10)` is set explicitly in `setup()` to prevent `readStringUntil()` from blocking the main control loop for up to 1 second if a line arrives without its `\n` terminator

### **Raspberry Pi → ESP32 Message Formats**

| Header | Format | Meaning |
|--------|--------|---------|
| `A` | `A,<leftArea>,<rightArea>,<error>,<steerAngle>,<turnCount>` | Open Challenge area-based steering + turn/lap counting — sent by `final.py` |
| `R` / `G` / `B` | `<color>,<error>,<distance>,<steerAngle>` | Vision color detection — pixel error, distance estimate, suggested steering angle |
| `C` | `C,<error>` | Reserved header handled by the firmware; currently not sent by any vision script |
| `M` | `M,<found>,<gap_error>,<gap_width>` | Parking-gap position from magenta markers — parsed and stored by the firmware |
| `N` | `N` | No obstacle currently detected — resets the active vision obstacle state |

### **Vision Timeout and Fault Recovery**

The ESP32 continuously tracks the age of the latest valid vision message.

If no valid message is received within:

```text
VISION_TIMEOUT = 500ms
```

the firmware automatically resets the active vision obstacle state to:

```text
N
```

This prevents stale obstacle information from remaining active indefinitely and allows the ESP32's local ultrasonic navigation logic to continue operating.

### 🛠️ **Engineering Notes**

### **Why the ESP32 Keeps Its Own Sensor Logic**

Running wall-following and corner-detection locally on the ESP32, rather than fully relying on the Raspberry Pi, keeps basic driving responsive even if the vision pipeline lags for a frame or two.

The ESP32 is therefore not simply a passive actuator controller. It contains an independent real-time navigation layer based on its ultrasonic sensors.

The Raspberry Pi vision system is used as an additional high-level input:
- Vision obstacle detection overrides local navigation when a valid obstacle is reported
- Vision-driven steering is used when `visionMode == 'A'`
- Parking-marker information is continuously stored for the later parking stage
- Local ultrasonic navigation remains available when no active vision override is present

The 500ms vision timeout provides an automatic fallback mechanism, allowing the ESP32 to return to its local navigation behavior instead of continuing to act on stale vision information.

### **Distance-Gated Obstacle Reaction**

The firmware only reacts to a reported obstacle color when:

```text
0 < obstacleDistance ≤ 50cm
```

inside `handleVisionObstacle()`.

This prevents the robot from reacting to detections that are visually valid but physically too far away to require immediate avoidance.

### **Sensor Filtering**

The ESP32's ultrasonic readings are processed using low-pass filtering before being used by the navigation logic.

This reduces the effect of individual noisy measurements and prevents the wall-following or corner-detection logic from responding too aggressively to a single unstable sensor reading.

The main distance inputs are:
- Front ultrasonic
- Left ultrasonic
- Right ultrasonic

These values are used for:
- Front obstacle/corner detection
- Left/right wall-following balance
- Corner-turn initiation
- Clearance evaluation
- Local fallback navigation

## **Technical Specifications**

### **System Requirements**

- **Raspberry Pi 4 Model B** running Python 3, `opencv-python`, `numpy`, and `pyserial`
- **ESP32 dev board** with `ESP32Servo.h`, programmed via Arduino IDE
- **L298N (or similar) DC motor driver**
- **Standard hobby steering servo**
- **3× ultrasonic distance sensors**: front, left, and right
- **Camera connected to Raspberry Pi 4**
- **UART connection**: 115200 baud, Raspberry Pi → ESP32

### **File Structure**

```text
software/
├── vision_navigation.py   # Raspberry Pi:
│                          # Obstacle Challenge detection,
│                          # red/green pillar detection,
│                          # white lane tracking,
│                          # magenta parking-gap calculation
│
├── final.py               # Raspberry Pi:
│                          # Open Challenge area-based steering,
│                          # dual-ROI wall following,
│                          # orange-line turn counting
│
├── esp32_car.ino          # ESP32:
│                          # motor/servo control,
│                          # ultrasonic processing,
│                          # wall-following state machine,
│                          # corner detection,
│                          # UART parser
│
└── README.md              # This documentation
```

For the standalone color-calibration workspace, see [Colors Documentation](../colors/README.md).

### **Overall Software Architecture Summary**

```text
                         ┌─────────────────────────┐
                         │       Raspberry Pi 4     │
                         │                         │
                         │  Python 3               │
                         │  OpenCV                 │
                         │  HSV Vision             │
                         │                         │
                         │  ┌───────────────────┐  │
                         │  │ vision_navigation │  │
                         │  │ Obstacle Challenge│  │
                         │  └───────────────────┘  │
                         │                         │
                         │  ┌───────────────────┐  │
                         │  │      final.py     │  │
                         │  │  Open Challenge   │  │
                         │  └───────────────────┘  │
                         │                         │
                         │  Red / Green Detection │
                         │  White Lane Detection  │
                         │  Magenta Parking       │
                         │  Orange Turn Counting  │
                         │  Steering Calculation  │
                         └────────────┬────────────┘
                                      │
                                      │ UART
                                      │ 115200 baud
                                      │ One-way
                                      ▼
                         ┌─────────────────────────┐
                         │          ESP32          │
                         │                         │
                         │  UART Parser            │
                         │  Vision State           │
                         │                         │
                         │  Front Ultrasonic       │
                         │  Left Ultrasonic        │
                         │  Right Ultrasonic       │
                         │                         │
                         │  Local Navigation       │
                         │  Wall Following         │
                         │  Corner Detection       │
                         │  Clearance State        │
                         │  Obstacle Override      │
                         │                         │
                         │  Motor + Steering       │
                         └────────────┬────────────┘
                                      │
                         ┌────────────┴────────────┐
                         ▼                         ▼
                  DC Motor Driver            Steering Servo
                         │                         │
                         └────────────┬────────────┘
                                      ▼
                              Autonomous Vehicle
```

The resulting architecture combines **camera-based perception**, **ultrasonic sensing**, **distributed processing**, **local real-time control**, **vision-based navigation**, **obstacle avoidance**, **Open Challenge wall following**, **lap/turn counting**, and **vision-assisted parking** while maintaining a lightweight and deterministic software stack suitable for real-time operation on the Raspberry Pi 4 and ESP32.


## 📹 **Performance Videos** <a id="performance-videos"></a>

Our development process included precise testing and validation to ensure competition-ready performance across both challenge scenarios.

### **Competition Performance**

- **Open Challenge**: 16-second perfect score demonstration
- **Obstacle Challenge**: 35-second perfect score with integrated parking
- **Detection Reliability**: >95% accuracy across variable lighting conditions
- **System Responsiveness**: <50ms latency from detection to actuation

### **Video Documentation**

Complete performance demonstrations showcasing our vehicle's capabilities:

- **Open Challenge**  
  [![Open Challenge Video](https://img.youtube.com/vi/tvqgwusap9M/0.jpg)](https://youtu.be/tvqgwusap9M)  
  *Demonstrates autonomous navigation and speed control on a dynamic track.*

- **Obstacle Challenge**  
  [![Obstacle Challenge Video](https://img.youtube.com/vi/fQPjyJrE8p8/0.jpg)](https://youtu.be/fQPjyJrE8p8)  
  *Shows traffic sign detection, obstacle avoidance, optimal path planning and parallel parking with smooth obstacle following at consistent distances.*

**Media Production**: All logos and visual media edits were created by our team using the ***ibisPaint X*** mobile application. Video overlay commentary and caption explanation edits were also done by our team using ***CapCut*** for professional presentation of our performance videos.

---

## 🌐 **GitHub Utilization & Development** <a id="github-utilization--development"></a>

GitHub served as the central platform for project management, version control, and public documentation. To ensure a well-organized and professional repository, we followed a milestone-based development workflow. Development and testing were conducted locally, with updates committed and documented after the completion of major engineering milestones, such as chassis finalization, sensor integration, and deployment of the core algorithms. This approach maintained a clear, structured, and easily traceable project history for both the development team and the wider community.

### **Development Workflow Strategy**

**Structured Development Approach**:
- **Local Development Environment**: Focused development work carried out on local machines using feature branches
- **Milestone-Based Committing**: Deliberate commits made at key points marking meaningful technical progress
- **Quality Assurance**: Careful testing and documentation completed before pushing updates to the public repository
- **Clean Public History**: A well-organized repository that reflects a polished and professional development journey

**File Sharing and Public Updates**: To keep our work accessible and easy for others to reproduce, all project assets — including CAD files (`models/`), electrical schematics (`schemes/`), and source code (`src/`) — are published publicly at every major milestone. Prior to each release, we carefully organize and clean up our code, data, and documentation to maintain a structured, easy-to-navigate repository. To support full transparency and proper version tracking, the exact date and time of each update is clearly noted in our README files.

### **Commit History & Project Evolution**

Our development timeline from June  to september 2026 demonstrates consistent progress and systematic engineering:

**Key Development Milestones**:
- **July 2026**: Core mechanical design and electronic system implementation
- **August 2026**: Repository initialization and project structure establishment  
- **August 2026**: national competition preparation and system optimization

**Commit Philosophy**: Each of our 20+ commits represents substantial technical progress, including:
- Complete mechanical system implementations (`design_base.3mf`, `4_gear_differential.3mf`)
- Electronic schematic and wiring documentation (`wiring_diagram.jpg`)
- Software algorithm development and optimization (`open.py`, `obstacle.py`)
- Comprehensive technical documentation updates across all 8 specialized folders
- Performance validation and testing results with competition videos

### **Repository Organization Excellence**

**Comprehensive Documentation Structure**:
- **8 Specialized Folders**: Each containing detailed technical README documentation
- **Structured File Organization**: Logical grouping of related technical assets
- **Professional Presentation**: Clean, well-organized repository layout
- **Easy Navigation**: Intuitive structure for both technical judges and future developers

### **Supporting Future Development & Replication**

<div align="center">

## 🔧 **EASY REPLICATION & FUTURE DEVELOPMENT**

### **Our documentation enables effortless duplication by other teams and developers**

</div>

**Replication-Focused Design**:
- **Complete Bill of Materials**: All components clearly specified with datasheet information
- **Step-by-Step Assembly Guides**: Detailed instructions for mechanical and electronic assembly
- **Manufacturing Files**: 3MF format for universal 3D printing compatibility
- **Source Code Availability**: Complete software implementation with detailed comments and explanations
- **Troubleshooting Guidance**: Solutions to common implementation challenges

**Supporting Others and Future Development**: We're happy to see others learn from what we've built, which is exactly why we chose the AGPL-3.0 license — it deliberately prevents our work from being folded into closed-source or private projects. Thanks to this strong copyleft protection, anything built on top of our code, hardware, or mechanical design has to stay open and available to everyone. Researchers, students, and other teams are welcome to copy, adapt, and expand on what we've done for learning, research, or competition use. Since our codebase is kept simple and clearly documented, teams without deep computer vision experience should still be able to adjust it for a new venue or challenge without much difficulty. We'd also genuinely welcome outside contributions — whether that's a better control algorithm or support for new sensors — through pull requests or issues on GitHub.
**Future Development Pathways**:
- **Modular Architecture**: Easy component upgrades and system modifications using our socket-based design
- **Comprehensive Documentation**: Every design decision and implementation detail documented
- **Open Source Philosophy**: AGPL-3.0 license ensuring continued community access
- **Educational Focus**: Detailed explanations of engineering principles and design choices

### **GitHub Best Practices Implementation**

**Professional Repository Management**:
- **Regular Updates**: Consistent documentation improvements and technical refinements
- **Quality Standards**: High-quality images, professional diagrams, and clear technical writing
- **Accessibility**: Well-structured content suitable for both technical and non-technical audiences
- **Completeness**: Every aspect of the project thoroughly documented and accessible

**Documentation Excellence Standards**:
- ✅ **Complete Information**: Comprehensive coverage of all technical aspects across 8 specialized folders
- ✅ **Structured Organization**: Logical, easy-to-navigate repository structure with clear documentation hierarchy
- ✅ **Regular Commits**: Meaningful, milestone-based version control demonstrating systematic development
- ✅ **Enhanced Engineering Understanding**: Detailed design rationale and implementation insights exceeding basic requirements

---

## 📜 **License & Replication** <a id="license--replication"></a>

### **Open Source Philosophy for Community Advancement**

**Replication-Focused Documentation**:
- **Complete Technical Transparency**: Every design decision and implementation detail documented
- **Manufacturing Accessibility**: Use of widely available components and custom manufacturing methods
- **Educational Value**: Detailed explanations enabling understanding of engineering principles
- **Future Development**: Clear pathways for system improvements and modifications

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)** to promote open collaboration, ensure continued community access to derivative works, facilitate easy replication by future developers and competition teams, and foster ongoing innovation through publicly accessible developments.

```
GNU Affero General Public License v3.0



This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```

### **Comprehensive Documentation Access**

<div align="center">

## 📚 **DETAILED TECHNICAL DOCUMENTATION**

### **Explore our specialized documentation for complete technical details**

</div>

- **For mechanical design and 3D models**: * [Models Documentation](https://github.com/wrorcbc-oss/WRO2025_RCBC/tree/main/Mechanical_Design)
- **For electrical schematics and wiring**: [Schemes Documentation](schemes/README.md)  
- **For software implementation and algorithms**: [Software Documentation](src/README.md)  
- **For competition performance videos**: [Video Documentation](video/README.md)  
- **For additional resources and photos**: [Other Documentation](other/README.md)
- **For MATLAB vision tools**: [MATLAB Documentation](matlab/README.md)
- **For team information**: [Team Photos Documentation](t-photos/README.md)
- **For vehicle documentation**: [Vehicle Photos Documentation](v-photos/README.md)

---

<div align="center">

## 🎯 **Prepared for national Competition Excellence**

**Team RCBC - *Never Stop Developing Unless We Stop Learning***

### **Comprehensive documentation enabling easy replication and future development**

[![Instagram](https://img.shields.io/badge/Follow%20our%20Journey-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/anti.wro/)
[![YouTube](https://img.shields.io/badge/Watch%20Performance%20Videos-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@solipsy.)

</div>
