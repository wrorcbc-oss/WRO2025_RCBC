import math
import time
import cv2 as cv
import numpy as np
import serial
from picamera2 import Picamera2

# ============================================================
# CONFIGURATION & TUNING
# ============================================================
SHOW_DEBUG = True  # Set False during race runs for max FPS

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

# Proportional Gain for Steering (Adjust to match car turn rate)
KP = 0.05
BASE_STEER = 90  # Center servo angle (0-180 deg)

# Turn Trigger Area Threshold
ORANGE_AREA_THRESHOLD = 100

# ============================================================
# REGIONS OF INTEREST (ROI) DEFINITIONS: (y1, y2, x1, x2)
# ============================================================
# 1. Dual Horizontal Strip ROIs (Blue boxes for area steering)
LEFT_STRIP_ROI = (110, 135, 10, 145)
RIGHT_STRIP_ROI = (110, 135, 175, 310)

# 2. Orange Line Turn Detection ROI (Inner Magenta box)
TURN_ROI = (120, 150, 80, 240)

# 3. Outer Track Frame Boundary (Outer Magenta box)
FRAME_ROI = (40, 230, 30, 290)

# ============================================================
# HSV COLOR RANGES
# ============================================================
# Black / Dark Wall Mask (For measuring left/right side wall area)
WALL_HSV_LOW = np.array([0, 0, 0])
WALL_HSV_HIGH = np.array([180, 255, 70])

# Orange Turn Line Color Mask
ORANGE_HSV_LOW = np.array([5, 150, 150])
ORANGE_HSV_HIGH = np.array([20, 255, 255])

KERNEL = np.ones((3, 3), np.uint8)

# ============================================================
# HARDWARE INITIALIZATION
# ============================================================
picam2 = Picamera2()
config = picam2.create_preview_configuration(
    main={"size": (CAMERA_WIDTH, CAMERA_HEIGHT), "format": "RGB888"}
)
picam2.configure(config)
picam2.start()
time.sleep(1.0)

try:
   

# Initialize serial connection to ESP32
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    print("Serial connected.")
except Exception as e:
    ser = None
    print(f"Serial Warning: {e}")

# Navigation Tracking State
turn_count = 0
turn_detected_flag = False
last_send = 0.0

# ============================================================
# MAIN CONTROL LOOP
# ============================================================
try:
    while True:
        frame = picam2.capture_array()
        frame = cv.flip(frame, 0)
        hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)

        # 1. Generate Masks
        mask_wall = cv.inRange(hsv, WALL_HSV_LOW, WALL_HSV_HIGH)
        mask_wall = cv.morphologyEx(mask_wall, cv.MORPH_OPEN, KERNEL)

        mask_orange = cv.inRange(hsv, ORANGE_HSV_LOW, ORANGE_HSV_HIGH)
        mask_orange = cv.morphologyEx(mask_orange, cv.MORPH_OPEN, KERNEL)

        # 2. Extract ROI Slices & Calculate Pixel Areas
        ly1, ly2, lx1, lx2 = LEFT_STRIP_ROI
        ry1, ry2, rx1, rx2 = RIGHT_STRIP_ROI
        ty1, ty2, tx1, tx2 = TURN_ROI

        left_slice = mask_wall[ly1:ly2, lx1:lx2]
        right_slice = mask_wall[ry1:ry2, rx1:rx2]
        orange_slice = mask_orange[ty1:ty2, tx1:tx2]

        left_area = float(cv.countNonZero(left_slice))
        right_area = float(cv.countNonZero(right_slice))
        orange_area = float(cv.countNonZero(orange_slice))

        # 3. Steering Error Calculation
        error = left_area - right_area
        steer = error * KP
        servo_angle = int(np.clip(BASE_STEER + steer, 0, 180))

        # 4. Turn Latch & Counter Logic
        turn_detect = 1 if orange_area > ORANGE_AREA_THRESHOLD else 0
        if turn_detect == 1 and not turn_detected_flag:
            turn_count += 1
            turn_detected_flag = True
        elif turn_detect == 0:
            turn_detected_flag = False

        # 5. Serial Transmission
        message = f"A,{left_area:.0f},{right_area:.0f},{error:.1f},{servo_angle},{turn_count}\n"

        if ser and (time.time() - last_send > 0.05):
            ser.write(message.encode())
            last_send = time.time()

        # 6. Visual Overlay Telemetry (Matching Image)
        if SHOW_DEBUG:
            display_frame = frame.copy()

            # Outer Boundary ROI (Magenta)
            cv.rectangle(
                display_frame,
                (FRAME_ROI[2], FRAME_ROI[0]),
                (FRAME_ROI[3], FRAME_ROI[1]),
                (255, 0, 255),
                2,
            )

            # Left & Right Strip ROIs (Blue)
            cv.rectangle(display_frame, (lx1, ly1), (lx2, ly2), (255, 0, 0), 2)
            cv.rectangle(display_frame, (rx1, ry1), (rx2, ry2), (255, 0, 0), 2)

            # Turn ROI (Magenta)
            cv.rectangle(
                display_frame, (tx1, ty1), (tx2, ty2), (255, 0, 255), 1
            )

            # Top Left Telemetry Overlay
            cv.putText(
                display_frame,
                f"Left area: {left_area:.1f}",
                (5, 18),
                cv.FONT_HERSHEY_SIMPLEX,
                0.45,
                (0, 255, 0),
                1,
            )
            cv.putText(
                display_frame,
                f"Right area: {right_area:.1f}",
                (5, 33),
                cv.FONT_HERSHEY_SIMPLEX,
                0.45,
                (0, 255, 0),
                1,
            )
            cv.putText(
                display_frame,
                f"Error: {error:.1f}",
                (5, 48),
                cv.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 0, 255),
                1,
            )
            cv.putText(
                display_frame,
                f"Steer: {steer:.2f}",
                (5, 63),
                cv.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 255, 255),
                1,
            )

            # Top Right Telemetry Overlay
            cv.putText(
                display_frame,
                f"Turn detect: {turn_detect}",
                (200, 18),
                cv.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 0, 255),
                1,
            )
            cv.putText(
                display_frame,
                f"Turn count: {turn_count}",
                (200, 33),
                cv.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 0, 0),
                1,
            )
            cv.putText(
                display_frame,
                f"Orange area: {orange_area:.0f}",
                (200, 48),
                cv.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 0, 0),
                1,
            )

            cv.imshow("Area Steer Debug", display_frame)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

finally:
    picam2.stop()
    if ser:
        ser.close()
    cv.destroyAllWindows()