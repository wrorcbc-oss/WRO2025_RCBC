# Color Detection & Calibration Documentation

This folder contains the standalone Python/OpenCV tools Team ANTi uses to develop and calibrate the color-detection logic before it is integrated into the robot's main navigation software. This documentation was last updated on **[ضع التاريخ هنا]**.

## 🎯 Purpose of This Folder

This folder is a **development and demonstration workspace** for the color detection system — separate from the full robot software (see the `software` folder). It lets us:
- Rapidly test and visualize HSV color detection in isolation
- Calibrate HSV thresholds interactively for any venue/lighting condition
- Validate detection logic (red/green signs, white lane) before it's carried over into the main navigation code

## Problem Context & Strategy

### Challenge
Accurate detection of red/green traffic signs and the white track lane under varying lighting conditions, in real time.

### Solution
- **HSV-based color segmentation**, more resistant to lighting changes than raw RGB
- **Dual-range detection for red**, since red wraps around both ends of the Hue spectrum (0–10 and 170–180)
- **Morphological filtering** (Opening + Closing) to remove noise and fill gaps in detected masks
- **Contour-based detection** with area and solidity filtering to reject false positives
- **A dedicated interactive calibration tool**, so thresholds can be re-tuned quickly for any new environment

### Why Python + OpenCV
- **OpenCV**: Fast, well-documented image processing operations (color conversion, morphology, contour analysis) suitable for real-time use
- **NumPy**: Efficient array operations for mask handling
- **Trackbars (`cv2.createTrackbar`)**: Instant visual feedback while calibrating, no need to modify code and re-run

## Innovation and Modeling

### Technical Implementation
```python
# Dual-range HSV detection for red (wraps around Hue 0/180)
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([180, 255, 255])

red_mask1 = cv.inRange(hsv, lower_red1, upper_red1)
red_mask2 = cv.inRange(hsv, lower_red2, upper_red2)
red_mask = cv.bitwise_or(red_mask1, red_mask2)
```

### Key Features
- **Multi-Target Detection**: Separate HSV ranges and masks for red, green, and the white lane
- **Noise Reduction Pipeline**: Gaussian blur before color conversion, then Morphological Open/Close on every mask
- **Region Restriction**: The lane mask ignores the top half of the frame to focus only on the track surface near the robot
- **Shape Validation**: Solidity check (`area / bounding_box_area > 0.5`) to reject irregular/noisy blobs
- **Position Reporting**: Compares each detected object's centroid X to the frame center to report LEFT/RIGHT positioning
- **Live Calibration Tool**: Real-time HSV + minimum-area tuning via trackbars, with final values printed to console on exit

## Test and Verification

### Validation Methodology
1. **Dataset**: [3000]
2. **Comparison**: Manual fixed thresholds vs. thresholds tuned live with `calibration.py`
3. **Metrics**: Detection accuracy, false positive rate, processing time per frame

### Performance Results
| Metric | Before Calibration Tool | With Calibration Tool | Improvement |
|--------|-------------------------|-----------------------|-------------|
| Calibration Time | 5 sec | 2 sec | 60% Faster (-3 sec) |
| Detection Accuracy | 80% | 93% | +13% |
| Cross-Lighting Robustness | Medium | High | Stable during regular movement (moves with uniform speed) |



### Sample Output
```
Lower: [35, 80, 80]
Upper: [90, 255, 255]
Min Area: 1000
```

## Code Quality & Readability

### File Structure
```
colors/
├── color_detection.py           # Standalone red/green/lane detection demo
├── calibration.py                # Interactive HSV/Min-Area calibration tool
├── system_implementation.jpeg    # Photo of the calibration setup on the physical robot
├── testing_the_callibration_code(*).jpg   # Calibration test screenshots
├── testing_the_detection_code(*).jpg      # Detection test screenshots
└── README.md                      # This documentation
```

### Coding Standards
- **Modular Steps**: Clear separation between blur/color-conversion, masking, morphology, contour analysis, and drawing/reporting
- **Threshold Isolation**: All HSV bounds are defined as named variables, easy to update from the calibration tool's output
- **Visual Debugging**: Every intermediate mask (`Red Mask`, `Green Mask`, `Lane Mask`) is displayed live alongside the main detection window
- **Safety Filtering**: Minimum area + solidity checks prevent small noise blobs from being reported as valid detections

## File List

- `color_detection.py`: Standalone real-time detection of red/green signs and the track lane, with LEFT/RIGHT position reporting — used to visually validate color logic in isolation
- `calibration.py`: Interactive tool with HSV and Min-Area trackbars to find optimal detection thresholds live, printed to console on exit
- `README.md`: Complete documentation for this color detection/calibration workspace
- `system_implementation.jpeg`, `testing_the_callibration_code*.jpg`, `testing_the_detection_code*.jpg`: Reference photos/screenshots from the calibration and detection testing sessions

## Usage Instructions

### Quick Start Guide

1. **Run the Calibration Tool First**:
   ```bash
   python calibration.py
   ```
   - Adjust the `L-H/S/V` and `U-H/S/V` trackbars until only the target color appears in the "Mask" window
   - Adjust "Min Area" so only real signs are boxed in green on the "Frame" window
   - Press `q` to print the final Lower/Upper/Min Area values to the console

2. **Validate with the Detection Demo**:
   ```bash
   python color_detection.py
   ```
   - Copy the calibrated HSV values into the corresponding `lower_*`/`upper_*` arrays
   - Confirm detection is stable and LEFT/RIGHT reporting is correct before moving these values into the main robot software (see the `software` folder)

3. **Press `d`** to stop and release the camera.

### Relationship to the Main Robot Software
This folder is a **calibration sandbox**, not what runs on the competition robot. Once thresholds are validated here, they are carried over into `vision_navigation.py` in the `software` folder, which adds full navigation, obstacle avoidance, and parking logic on top of the same color-detection foundation.

## Technical Specifications

### System Requirements
- **Python 3.x**
- Required Libraries: **opencv-python (cv2)**, **numpy**, **pyserial**
- **Camera**: Any OpenCV-compatible camera (index 0 by default)

### Color Channels (HSV)
- **H (Hue)**: 0–179 range (OpenCV convention)
- **S (Saturation)**: 0–255 range
- **V (Value/Brightness)**: 0–255 range

## Lessons Learned
- **HSV over RGB**: HSV separates color (Hue) from brightness (Value), making detection far more stable under changing lighting
- **Dual-Range Necessity**: Red specifically requires two Hue ranges because it sits at both ends of the OpenCV Hue scale (0–180)
- **Calibrate on Location**: Thresholds tuned indoors often fail outdoors (and vice versa) — recalibrating on the actual competition lighting is essential

For the full robot navigation and control software, see [Software Documentation](../software/README.md).
